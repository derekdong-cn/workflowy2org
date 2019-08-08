class Converter:
    
    # Return string `s` duplicated `i` times.
    def duplicate(self, s, i):
        ret = ""
        for j in xrange(i):
            ret += s
        return ret

    def convert(self, input_stream, output_stream):
        wfDone = "[COMPLETE]"
        orgDone = "DONE"

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

            line = line[dash + 1:].strip() # get line contents only
            if line.startswith(wfDone):
                line = line.replace(wfDone, orgDone, 1) # replace a single occurrence
            line = self.duplicate("*", dash // 2 + 1) + " " + line # build the new line

            output_stream.write(line + "\n")
