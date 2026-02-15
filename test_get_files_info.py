import unittest
import os
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        print("Results for current directory")
        result = get_files_info("calculator", ".")

        print(result, "\n")

        self.assertIsNotNone(result)
        self.assertIn("main.py", result)
        self.assertIn("tests.py", result)
        self.assertIn("pkg", result)

    def test_pkg_dir(self):
        print("Results for current directory")
        result = get_files_info("calculator", "pkg")

        print(result, "\n")

        self.assertIsNotNone(result)
        self.assertIn("calculator.py", result)
        self.assertIn("render.py", result)

    def test_bin_dir(self):
        print("Results for current directory")
        result = get_files_info("calculator", "/bin")
        print(result, "\n")
        self.assertIn("outside the permitted working directory", result)

    def test_parent_dir(self):
        print("Results for current directory")
        result = get_files_info("calculator", "../")
        print(result, "\n")
        self.assertIn("outside the permitted working directory", result)

if __name__ == "__main__":
    unittest.main()