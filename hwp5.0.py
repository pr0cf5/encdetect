#!/usr/bin/python
from olefile import *
import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: ./checkEnc.py <filename>")
		exit(1)
	f = open(sys.argv[1],"r")
	assert(isOleFile(f))
	oleobj = OleFileIO(f)
	dirs = oleobj.direntries

	found = False

	for x in dirs:
		if x is None:
			continue
		if x.name == "FileHeader":
			found = True
			break
	if not found:
		print("FileHeader entry not found!")
		exit(1)

	stream = oleobj.openstream("FileHeader")
	metadata = stream.read()
	signature = "HWP Document File"
	if not signature == metadata[:len(signature)]:
		print("Provided file is not an HWP5.0 Document")
		exit(1)
	encflag = ord(metadata[36]) & 2
	if encflag:
		print("Encrypted file")
	else:
		print("Plain file")
	

	f.close()
