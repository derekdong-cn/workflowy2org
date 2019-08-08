import unittest
from io import StringIO

import workflowy2org
from workflowy2org.converter import Converter

class ImportTests(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def convert_and_check(self, input_text, expected_output_text):
        infile = StringIO(input_text)
        outfile = StringIO()

        c = Converter()
        c.convert(infile, outfile)
        self.assertEqual(expected_output_text, outfile.getvalue())


    def test_single_line(self):
        self.convert_and_check(u"- a", u"* a\n")


    def test_multiple_lines(self):
        input_text = u"""
- To Do
  - [COMPLETE] Rent a truck
    - [COMPLETE] call them
  - Run every day
    - Set a schedule
    - Stop procrastinating
  -
  -
  - [COMPLETE] Buy drumkit
- ideas
"""

        expected_output = u"""* To Do
** DONE Rent a truck
*** DONE call them
** Run every day
*** Set a schedule
*** Stop procrastinating
** 
** 
** DONE Buy drumkit
* ideas
"""

        self.convert_and_check(input_text, expected_output)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
