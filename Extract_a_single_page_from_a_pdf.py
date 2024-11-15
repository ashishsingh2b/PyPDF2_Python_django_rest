from PyPDF2 import PdfReader, PdfWriter

path = 'O_Son_.pdf'

pdf=PdfReader(path,'rb')

writer= PdfWriter()
writer.add_page(pdf.pages[3])  # Use pdf.pages[page] to get the page
writer.add_page(pdf.pages[4])  # Use pdf.pages[page] to get the page
writer.add_page(pdf.pages[5])  # Use pdf.pages[page] to get the page
writer.add_page(pdf.pages[6])  # Use pdf.pages[page] to get the page
writer.add_page(pdf.pages[7])  # Use pdf.pages[page] to get the page

with open('singleson.pdf','wb') as out:
    writer.write(out)
    