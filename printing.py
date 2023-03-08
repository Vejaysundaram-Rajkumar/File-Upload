import subprocess

file_path = "D://College//iquest//File-Upload//sample.pdf"
printer_name = "EPSON L130 Series"  

print_command = 'rundll32.exe printui.dll,PrintUIEntry /k /n "{}" /o "Color=1" /o "Collate=1" /o "StapleLocation=0" /o "Duplex=2" /h "{}"'.format(printer_name, file_path)
subprocess.Popen(print_command, shell=True)
