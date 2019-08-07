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

        for num, line in enumerate(input_stream):
            if line.isspace():
                break
            dash = line.find("-")
            if dash == -1:
                print("Error at line " + str(num))
                break

            line = line[dash + 1:].strip() # get line contents only
            if line.startswith(wfDone):
                line = line.replace(wfDone, orgDone, 1) # replace a single occurrence
            line = self.duplicate("*", dash // 2 + 1) + " " + line # build the new line
        
            output_stream.write(line + "\n")
