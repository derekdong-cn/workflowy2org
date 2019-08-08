class Converter:
    
    def convert(self, input_stream, output_stream):

        num = 0
        for line in input_stream:
            num += 1

            # Bullets start with dash ("-"), perhaps with leading spaces.
            # "Text lines" (bullet sub-elements) should never start with a dash
            # charater ... note this will fail if the text line does in fact start
            # with a dash, but that shouldn't occur often.  Solving that
            # Correctly would require a parser, which seems
            # like needless complication.
            is_text_line = (line.strip().find("-") != 0)
            if is_text_line:
                output_stream.write(line.strip().replace('"', '') + "\n")
                continue

            dash = line.find("-")

            line_text = line[dash + 1:].strip()
            wfDone = "[COMPLETE]"
            if line_text.startswith(wfDone):
                line_text = line_text.replace(wfDone, "DONE", 1) # replace a single occurrence

            bullet = '*' * (dash // 2 + 1)
            output_stream.write(bullet + " " + line_text + "\n")
