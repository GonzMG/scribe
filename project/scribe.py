from os import listdir
from os.path import isfile, join, getmtime, getctime
from datetime import datetime
from project.domain.file import File, FileId, Metadata
import uuid
import pdfplumber


class Scribe:
    def __init__(self, folders: [str]):
        self.folders_to_read = folders

        self.docs_found = 0
        self.docs_indexed = 0
        self.docs_read = 0

    def indexer(self):
        """Read all the PDF files from a folder/s, extract the textual
        layer and metadata, index it in ES"""
        folders = self.folders_to_read

        all_files = [
            f for directory in folders for f in self.directory_reader(directory)
        ]
        self.docs_found = len(all_files)

        return all_files

    def directory_reader(self, directory_path: str) -> [File]:
        files_to_return = []
        all_files = listdir(directory_path)
        for f in all_files:
            file_name = join(directory_path, f)
            if isfile(file_name):
                file = File(
                    FileId(uuid.uuid4()),
                    Metadata(
                        file_name, 
                        datetime.fromtimestamp(getctime(file_name)).strftime('%Y-%m-%d %H:%M:%S'), 
                        datetime.fromtimestamp(getmtime(file_name)).strftime('%Y-%m-%d %H:%M:%S')
                    ),
                    f
                )
                files_to_return.append(file)
                
        return files_to_return
    
    def text_extractor(self, file: File):
        path = file.metadata.path
        print(f'Extracting text from file {path}')
        text = ''
        with pdfplumber.open(path) as pdf:
            pages = pdf.pages
            print(f'Number of pages: {len(pages)}')
            for i, page in enumerate(pages):
                print(f'Extracting text from page {i}')
                extracted_text = page.extract_text_simple(x_tolerance=3, y_tolerance=3)
                text += extracted_text
        file.set_extracted_text(text)


