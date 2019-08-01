#!/usr/bin/python
from pdfrw import PdfReader
import sys

if __name__ == "__main__":
	enc = False
	if len(sys.argv) != 2:
		print("usage: ./checkEnc.py <filename>")
		exit(1)
	
	pdfobj = PdfReader(sys.argv[1])
	for x in pdfobj.keys():
		if "Encrypt" in x:
			enc = True
			break
	if enc:
		print("Encrypted file")
	else:
		print("Plain file")
