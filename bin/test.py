import sys

from pdfkit import *


if __name__ == '__main__':
    with NSAutoreleasePool():
        doc = PDFDocument.from_path(sys.argv[1])
        attrs = doc.send('documentAttributes')
        for a, b in attrs.items():
            print a, b
