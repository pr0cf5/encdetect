#!/bin/sh
./hwp5.0.py ./plain.hwp
./hwp5.0.py ./enc.hwp
./msoffice.py ./plain.docx
./msoffice.py ./enc.docx
./pdf.py ./plain.pdf
./pdf.py ./enc.pdf
