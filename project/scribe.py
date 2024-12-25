from os import listdir
from os.path import isfile, join
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

    def directory_reader(self, directory_path: str) -> [str]:
        onlyfiles = [
            f for f in listdir(directory_path) if isfile(join(directory_path, f))
        ]
        return onlyfiles
    
    def text_extractor(self, file_path: str) -> str:
        print(f'Extracting text from file {file_path}')
        text = ''
        with pdfplumber.open(file_path) as pdf:
            pages = pdf.pages
            print(f'Number of pages: {len(pages)}')
            for i, page in enumerate(pages):
                print(f'Extracting text from page {i}')
                extracted_text = page.extract_text_simple(x_tolerance=3, y_tolerance=3)
                text += extracted_text
        return text


