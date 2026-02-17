import unittest
import os
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_write_lorem_ipsum(self):
        print("Results for current directory")
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result, "\n")

        self.assertIn("Successfully wrote to", result)

    def test_write_more_lorem(self):
        print("Results for current directory")
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result, "\n")

        self.assertIn("Successfully wrote to", result)

    def test_write_not_allowed(self):
        print("Results for current directory")
        with self.assertRaises(Exception) as ctx:
            write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(ctx.exception, "\n")

        self.assertIn("Error:", str(ctx.exception))
        self.assertIn("is outside the permitted working directory", str(ctx.exception))

if __name__ == "__main__":
    unittest.main(verbosity=2)