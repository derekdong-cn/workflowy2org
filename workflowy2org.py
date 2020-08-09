"""
Command-line script: converts a Workflowy text export to org-mode format.
"""

import workflowy2org
from workflowy2org.converter import Converter

IN_NAME = input("What file are we converting? (full name) ")
OUT_NAME = IN_NAME + ".org"

C = Converter()
with open(IN_NAME, encoding="utf8") as instream:
    with open(OUT_NAME, 'w', encoding="utf8") as outstream:
        C.convert(instream, outstream)
C.print_warnings()
print()
print ("File converted! Output at", OUT_NAME)
