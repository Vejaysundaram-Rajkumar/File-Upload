import os
import win32api
import win32print
from PyPDF2 import PdfReader

# Set the file path of the PDF file to print
pdf_file = r'D://College//iquest//File-Upload//sample.pdf'

# Set the print preferences
preferences = {
    'copies': 2,       # number of copies to print
    'duplex': 'long',  # duplex printing: 'long' for landscape, 'short' for portrait, None for no duplex
    'color': True      # True for color, False for black and white
}

# Get the default printer name
printer_name = win32print.OpenPrinter("EPSON L130 Series")
# Open the PDF file and read its contents
with open(pdf_file, 'rb') as f:
    pdf_reader = PdfReader(f)
    num_pages = len(pdf_reader.pages)

    # Create a new print job
    job_id = win32print.StartDocPrinter(printer_name, 1, ('test print job', None, 'RAW'))

    # Set the print job properties
    #properties = win32print.GetPrinter(printer_name)['pDevMode'].Duplex = win32print.
    win32print.SetJob(printer_name, job_id, 2)

    # Loop through each page of the PDF file and print it
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        data = page.extractText()

        # Set the print job data
        win32api.SetJob(printer_name, job_id, 1, bytes(data.encode('utf-8')))

        # Send the print job to the printer
        win32print.StartPagePrinter(printer_name)
        win32print.WritePrinter(printer_name, bytes(data.encode('utf-8')))
        win32print.EndPagePrinter(printer_name)

    # End the print job
    win32print.EndDocPrinter(printer_name)