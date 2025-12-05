import unittest
from unittest.mock import patch
import sys
from io import StringIO
import os

from src.day1 import main

class TestDay1Main(unittest.TestCase):
    @patch("src.day1.getUser_YesNo", return_value=True)
    def test_main_with_test_file(self, mock_getUser_YesNo):
        # Arrange: simulate command-line args
        sys.argv = ["program", os.path.join("input", "testInput.txt")]

        # Read expected output from testAnswer.txt
        with open(os.path.join("input", "testAnswer.txt"), "r") as f:
            expected_output = f.read().strip()

        # Capture stdout
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            output = fake_out.getvalue().strip()

        # Extract the last two lines of program output
        lines = output.splitlines()
        clicks_line = lines[-2]   # "Num Clicks: 3"
        zeroes_line = lines[-1]   # "Num Zeroes: 6"

        # Parse the numbers
        clicks = clicks_line.split()[-1]
        zeroes = zeroes_line.split()[-1]

        actual_output = f"{clicks}, {zeroes}"

        # Assert: check expected output matches
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
