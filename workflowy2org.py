"""
Command-line script: converts a Workflowy text export to org-mode format.
"""

import workflowy2org
from workflowy2org.converter import Converter

IN_NAME = raw_input("What file are we converting? (full name) ")
OUT_NAME = IN_NAME + ".org"

C = Converter()
with open(IN_NAME) as instream:
    with open(OUT_NAME, 'w') as outstream:
        C.convert(instream, outstream)
C.print_warnings()
