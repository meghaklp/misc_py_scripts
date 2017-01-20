# DOCXtoPDF.py

# Author: Vasudev Ram - http://www.dancingbison.com
# Copyright 2012 Vasudev Ram, http://www.dancingbison.com

# This is open source code, released under the New BSD License -
# see http://www.opensource.org/licenses/bsd-license.php .

import sys
import os
import os.path
import string
from textwrap import TextWrapper
from docx import opendocx, getdocumenttext
import fpdf
import traceback


def docx_to_pdf(infilename, outfilename):

    # Extract the text from the DOCX file object infile and write it to 
    # a PDF file.

    try:
        infil = opendocx(infilename)
    except Exception, e:
        print "Error opening infilename"
        print "Exception: " + repr(e) + "\n"
        sys.exit(1)

    paragraphs = getdocumenttext(infil)
    pdf = fpdf.FPDF()
    pdf.add_page();
    pdf.set_font('Arial','',10);

    wrapper = TextWrapper(width=70, drop_whitespace=False)

    # For Unicode handling.
    new_paragraphs = []
    for paragraph in paragraphs:
        new_paragraphs.append(paragraph.encode("utf-8"))

    for paragraph in new_paragraphs:
        lines = wrapper.wrap(paragraph)
        # i = 0
        # for line in lines:
        #     print(line)
        #     pdf.text(0,i,line)
        #     i = i+1;
        pdf.write(len(lines),paragraph)
        pdf.ln(2*len(lines))
    pdf.output(outfilename,"F")

def usage():
    return "Usage: python DOCXtoPDF.py infile.docx outfile.txt\n"

def main():
    try:
        # Check for correct number of command-line arguments.
        if len(sys.argv) != 3:
            print "Wrong number of arguments"
            print usage()
            sys.exit(1)
        infilename = sys.argv[1]
        outfilename = sys.argv[2]

        # Check for right infilename extension.
        infile_ext = os.path.splitext(infilename)[1]
        if infile_ext.upper() != ".DOCX":
            print "Input filename extension should be .DOCX"
            print usage()
            sys.exit(1)

        # Check for right outfilename extension.
        outfile_ext = os.path.splitext(outfilename)[1]
        if outfile_ext.upper() != ".PDF":
            print "Output filename extension should be .PDF"
            print usage()
            sys.exit(1)

        docx_to_pdf(infilename, outfilename)

    except Exception, e:
        sys.stderr.write("Error: " + repr(e) + "\n")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

# EOF