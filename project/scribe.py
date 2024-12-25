from os import listdir
from os.path import isfile, join


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
