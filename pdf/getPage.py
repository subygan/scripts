from argparse import ArgumentParser
from glob import glob
import os
from icecream import ic

from PyPDF2 import PdfFileReader, PdfFileWriter

# Note: index starts at 1 and is inclusive of the end.
# The following will extract page 3 of the pdf file.


def getPage(path, output_filename, start, end):
    pdfs = {path: ({'start': int(start), 'end': int(end)},)}

    for pdf, segments in pdfs.items():
        pdf_reader = PdfFileReader(open(path, 'rb'))
        for segment in segments:
            pdf_writer = PdfFileWriter()
            start_page = segment['start']
            end_page = segment['end']
            for page_num in range(start_page - 1, end_page):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            if output_filename:
                output_filename = f'{output_filename}_{start_page}_page_{end_page}.pdf'
            else:
                output_filename = f'{pdf.split("/")[-1]}_{start_page}_page_{end_page}.pdf'

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)




if __name__ == "__main__":
    parser = ArgumentParser()

    # Add more options if you like
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")

    parser.add_argument("-s", "--start-page",
                        dest="start_page",
                        default="1",
                        help="start page number to be gotten from")

    parser.add_argument("-e", "--end-page",
                        dest="end_page",
                        default="1",
                        help="end page to be gotten till")

    args = parser.parse_args()
    getPage(args.path, args.output_filename, args.start_page, args.end_page)