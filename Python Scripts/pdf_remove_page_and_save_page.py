# Author: Justin Yoo
# This script will remove the last page (or pages) of the PDF files located
# in file_path and save them separately as single page PDF files.

import os
import PyPDF2
import getpass

user_name = getpass.user()

file_path = 'C:/Users/' + user_name + '/Desktop/PDF Files/'

pdf_writer = PyPDF2.PdfFileWriter()

for pdf_file in os.listdir(file_path):
    pdf_file_object = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
    for page_number in range(1, pdf_reader.numPages):
        page_object = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page_object)

    pdf_output = open(file_name + ' Extracted Page.pdf', 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()