#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
from icecream import ic
from pathlib import Path

'''
usage:
`python3 merge.py -p ./ignore -o ./ignore/midsem.pdf`

This command merges all pdfs under the ./ignore directory, in alphabetical order and writes it to ./ignore/midsem.pdf 

'''


def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)

    ic(glob(path + os.sep + '*.pdf'))
    for pdffile in glob(path + os.sep + '*.pdf'):
        ic(pdffile)
        # with open(pdffile, 'rb') as f :
        merger.append(Path(pdffile))
    merger.write(output_filename)
    merger.close()


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
