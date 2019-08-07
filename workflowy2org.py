import workflowy2org
from workflowy2org.converter import Converter

in_name = raw_input("What file are we converting? (full name) ")
out_name = in_name + ".org"

c = Converter()
with open(in_name) as instream:
    with open(out_name, 'w') as outstream:
        c.convert(instream, outstream)
