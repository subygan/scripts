#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
from icecream import ic


def merge(path, output_filename):
    merger = PdfFileMerger()

    ic(glob(path + os.sep + '*.pdf'))
    for pdffile in glob(path + os.sep + '*.pdf'):

        ic(pdffile)
        with open(pdffile, 'rb') as f :
            merger.append(f)
    merger.write("result.pdf")
    merger.close()
    exit(2)

    print("Start writing '%s'" % output_filename)
    with open(output_filename, "wb") as f:
        pass



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