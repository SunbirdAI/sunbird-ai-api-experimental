import unittest
import os
from fastapi import HTTPException
from app.file_translate.utils import validate_uploaded_file, \
    parse_filename, create_txt_file, DATA_FOLDER, get_chunks


class TestUtils(unittest.TestCase):

    def test_validate_uploaded_file(self):
        test_case = {'file_type': 'txt', 'file_size': 2 * 1024 * 1024}
        self.assertIsNone(
            validate_uploaded_file(
                file_type=test_case['file_type'],
                file_size=test_case['file_size']
            )
        )

        test_case = {
            'file_type': 'pdf',
            'file_size': 2 * 1024 * 1024 + 1
        }
        with self.assertRaises(HTTPException):
            validate_uploaded_file(
                file_type=test_case['file_type'],
                file_size=test_case['file_size']
            )

    def test_parse_filename(self):
        test_filenames = ["test_1.txt", "test_2.pdf", "test3.test.txt"]
        test_names = ['test_1', 'test_2', 'test3.test']
        test_exts = ['txt', 'pdf', 'txt']

        for index, test in enumerate(test_filenames):
            self.assertEqual(
                parse_filename(test_filenames[index]),
                (test_names[index], test_exts[index])
            )

    def test_create_txt_file(self):
        # file are created in data folder /data
        test_txt = "Test this function"
        filename = "test"
        filepath = f'{DATA_FOLDER}/{filename}.txt'

        create_txt_file(
            text=test_txt,
            filename=filename
        )

        self.assertTrue(os.path.exists(filepath))
        with open(file=filepath, mode='r') as f:
            self.assertEqual(test_txt, f.read())

        os.remove(filepath)

    def test_get_chunks(self):
        test_data = [
            {
                'text': "data test",
                'chunk_size': 5,
                'expected_chunks': ['data', 'test']
            },

            {
                'text': "data test",
                'chunk_size': 11,
                'expected_chunks': ['data test']
            },

            {
                'text': "data test data",
                'chunk_size': 11,
                'expected_chunks': ['data test', 'data']
            }

        ]

        for test_case in test_data:
            self.assertEqual(
                get_chunks(
                    test_case['text'],
                    test_case['chunk_size']
                ),
                test_case['expected_chunks']
            )
