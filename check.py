import fitz
pdf_doc = fitz.open("D://College//iquest//File-Upload//resume.pdf")
for page_num in range(pdf_doc.page_count):
    page = pdf_doc.load_page(page_num)
    images = page.get_image_list()
    if len(images) > 0:
        print(".")
    else:
        print("no")