#!/usr/bin/python
from msoffcrypto import *
import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: ./checkEnc.py <filename>")
		exit(1)
	f = open(sys.argv[1], "rb")
	crypt = OfficeFile(f)
	if crypt.is_encrypted():
		print("Encrypted file")
	else:
		print("Plain file")
	

