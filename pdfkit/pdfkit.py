"""
Experiments in accessing PDFKit with ctypes.
"""

import ctypes

from .cocoa import *


pdfkit = ctypes.CDLL('/System/Library/Frameworks/Quartz.framework/Frameworks/PDFKit.framework/PDFKit')


class PDFDocument(ObjCObj):
    @classmethod
    def from_path(cls, url):
        url = NSURL.from_path(url)
        doc = cls()
        doc.send('initWithURL:', url)
        doc.send('autorelease')
        return doc
