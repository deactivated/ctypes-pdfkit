"""
Experiments in accessing PDFKit with ctypes.
"""

import ctypes

from .cocoa import *


pdfkit = ctypes.CDLL('/System/Library/Frameworks/Quartz.framework/Frameworks/PDFKit.framework/PDFKit')


class PDFPage(ObjCObj):
    @property
    def text(self):
        return self.send("string")
    

class PDFDocument(ObjCObj):
    @classmethod
    def from_path(cls, url):
        url = NSURL.from_path(url)
        doc = cls()
        doc.send('initWithURL:', url)
        doc.send('autorelease')
        return doc

    @property
    def page_count(self):
        return self.send('pageCount', raw=True)
    
    @property
    def document_attributes(self):
        nsd = self.send('documentAttributes')
        return dict(nsd)

    def write_to_file(self, path):
        return self.send('writeToFile:', path)

    @property
    def pages(self):
        for i in range(self.page_count):
            page = self.send("pageAtIndex:", i)
            yield page
