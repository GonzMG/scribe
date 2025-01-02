import os
import tempfile
import unittest

from project.scribe import Scribe
from project.domain.file import File, Metadata, FileId
import uuid


class TestScribe(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()

        # Create some test files
        self.test_files = ["test1.pdf", "test2.pdf", "test3.txt", "test4.doc"]
        for file_name in self.test_files:
            with open(os.path.join(self.test_dir, file_name), "w") as f:
                f.write("test content")

        # Initialize Scribe with test directory
        self.scribe = Scribe([self.test_dir])

    def tearDown(self):
        # Clean up temporary directory and files
        for file_name in self.test_files:
            os.remove(os.path.join(self.test_dir, file_name))
        os.rmdir(self.test_dir)

    def test_directory_reader(self):
        # Test directory_reader method
        files = self.scribe.directory_reader(self.test_dir)

        # Check if all test files are found
        self.assertEqual(len(files), 2)
        for result_file in files:
            self.assertIn(result_file.name, self.test_files)

    def test_indexer(self):
        test_files_path = os.path.join(os.path.dirname(__file__), 'files')
        scribe = Scribe([test_files_path])
        # Test indexer method
        scribe.indexer()

        # Verify that files were found
        self.assertEqual(scribe.docs_found, 1)

    def test_empty_directory(self):
        # Create empty directory
        empty_dir = tempfile.mkdtemp()
        empty_scribe = Scribe([empty_dir])

        # Test directory_reader with empty directory
        files = empty_scribe.directory_reader(empty_dir)
        self.assertEqual(len(files), 0)

        # Clean up
        os.rmdir(empty_dir)

    def test_extract_text(self):
        test_files_path = os.path.join(os.path.dirname(__file__), 'files')
        scribe = Scribe([test_files_path])
        path = os.path.join(test_files_path, 'Lorem_ipsum.pdf')
        file = File(FileId(uuid.uuid4), Metadata(path), 'Lorem_ipsum.pdf')
        scribe.text_extractor(file)
        self.assertIsNotNone(file.extracted_text)


if __name__ == "__main__":
    unittest.main()
