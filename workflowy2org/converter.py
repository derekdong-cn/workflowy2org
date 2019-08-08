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
            if line.isspace():
                continue
            dash = line.find("-")
            if dash == -1:
                raise Exception("Error at line " + str(num))

            line = line[dash + 1:].strip() # get line contents only
            if line.startswith(wfDone):
                line = line.replace(wfDone, orgDone, 1) # replace a single occurrence
            line = self.duplicate("*", dash // 2 + 1) + " " + line # build the new line

            output_stream.write(line + "\n")
