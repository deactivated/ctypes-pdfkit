import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

    
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pdfkit',
      version="0.1",
      author="Mike Spindel",
      author_email="deactivated@gmail.com",
      license="MIT",
      keywords="pdf pdfkit ctypes",
      url="http://github.com/deactivated/ctypes-pdfkit",
      description='An experiment in accessing PDFKit via ctypes.',
      packages=find_packages(exclude=['ez_setup']),
      long_description=read('README.rst'),
      zip_safe=False,
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Environment :: MacOS X",
          "Programming Language :: Python"])
