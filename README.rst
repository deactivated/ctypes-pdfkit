=============================================================
ctypes-pdfkit - An experiment in accessing PDFKit via ctypes.
=============================================================

  Do not confuse the presence of a README for an indication that this
  code is production worthy or even particularly useful.

Apple includes a sophisticated PDF manipulation API with Mac OS X,
called PDFKit [#]_.  This repo includes some experimental code that
illustrates how to access it using the `ctypes` FFI in Python.

It's worth noting that it is also straightforward to use PDFKit via
the PyObjC bridge.  If you're seriously interested in using PDFKit via
Python in a production-level system, you will probably be better off
using that.

Sample Usage
============

::

  import sys
  from pdfkit import PDFDocument

  with NSAutoreleasePool():
      doc = PDFDocument.from_path(sys.argv[1])
      attrs = doc.send('documentAttributes')
      for a, b in attrs.items():
          print a, b


.. [#] http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/QuartzFramework/Classes/PDFDocument_Class/Reference/Reference.html
