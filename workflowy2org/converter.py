"""
Conversion classes.
"""

class Converter(object):
    """
    Converts Workflowy text export to org-mode.
    """

    def __init__(self):
        """
        Constructor
        """
        self._has_notes = False


    def convert(self, input_stream, output_stream):
        """
        Converts Workflowy text export to org-mode.

        Args:
          input_stream: the Workflowy text export.
          output_stream: where converted text is written to.
        """

        self._has_notes = False

        for line in input_stream:

            # Bullets start with dash ("-"), perhaps with leading spaces.
            # "Text lines" (bullet sub-elements) should never start with a dash
            # character ... note this will fail if the text line does in fact start
            # with a dash, but that shouldn't occur often.  Solving that
            # correctly would require a parser, which seems
            # like needless complication.
            is_text_line = (line.strip().find("-") != 0)
            if is_text_line:
                self._has_notes = True
                output_stream.write(line.strip().replace('"', '') + "\n")
                continue

            dash = line.find("-")

            line_text = line[dash + 1:].strip()
            wf_complete = "[COMPLETE]"
            if line_text.startswith(wf_complete):
                line_text = line_text.replace(wf_complete, "DONE", 1) # replace a single occurrence

            bullet = '*' * (dash // 2 + 1)
            output_stream.write(bullet + " " + line_text + "\n")


    def print_warnings(self):
        """
        Print warnings to console.  Do nothing if no warnings.
        """

        if self._has_notes:
            warning = """WARNING: bullets with notes may not be exported correctly.

Workflowy allows you to add notes to bullets (with Shift-Enter).
These notes may contain lines that start with asterisks or dashes,
which currently confuse this exporter, and result in notes being converted
to bullets.  Please check the generated file, and if necessary update the
Workflowy bullet notes to remove these asterisks or dashes, and re-export.
"""
            print(warning)
