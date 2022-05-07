#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def merge(path, output_filename):
    output = PdfFileWriter()
    f = glob(path + os.sep + '*.pdf')
    for pdffile in f[::-1]:
        print(pdffile)
        if pdffile == output_filename:
            continue
        print("Parse '%s'" % pdffile)
        document = PdfFileReader(open(pdffile, 'rb'))
        for i in range(document.getNumPages()):
            output.addPage(document.getPage(i))

    print("Start writing '%s'" % output_filename)
    with open(output_filename, "wb") as f:
        output.write(f)


if __name__ == "__main__":
    parser = ArgumentParser()

    # Add more options if you like
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="merged.pdf",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")

    args = parser.parse_args()
    merge(args.path, args.output_filename)