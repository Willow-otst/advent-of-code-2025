import unittest
from unittest.mock import patch
import sys
from io import StringIO
import os

from src.day2 import main

class TestDay2Main(unittest.TestCase):
    @patch("src.day2.getUser_YesNo", return_value=True)
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

        print("out\n", output)

        # Extract the two printed sums
        lines = output.splitlines()
        sumPairIDs = lines[-2].split()[-1]      # from "ID Sum Pairs: ..."
        sumRepeatIDs = lines[-1].split()[-1]    # from "ID Sum Repeats: ..."

        # Assert: check expected output matches
        actual_output = f"{sumPairIDs},{sumRepeatIDs}"
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
