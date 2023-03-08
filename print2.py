import win32print

# specify the file you want to print
filename = 'path/to/your/sample.pdf'

# create a printer handle
printer_handle = win32print.OpenPrinter('EPSON L130 Series')

# set the printing preferences
preferences = {"Color": win32print.DMCOLOR_COLOR,  # can be DMCOLOR_MONOCHROME for black and white
               "Duplex": win32print.DMDUP_SIMPLEX,  # can be DMDUP_VERTICAL for vertical duplex
               "Copies": 2}  # number of copies

# create a devmode object and update it with the printing preferences
devmode = win32print.GetDefaultPrinterDevMode()
devmode.Color = preferences["Color"]
devmode.Duplex = preferences["Duplex"]
devmode.Copies = preferences["Copies"]

# start the print job
job_info = (filename, None, {"DevMode": devmode})
job_id = win32print.StartDocPrinter(printer_handle, 1, job_info)

# print the file
win32print.StartPagePrinter(printer_handle)
with open(filename, 'rb') as f:
    win32print.WritePrinter(printer_handle, f.read())
win32print.EndPagePrinter(printer_handle)

# end the print job
win32print.EndDocPrinter(printer_handle)

# close the printer handle
win32print.ClosePrinter(printer_handle)
