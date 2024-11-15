from PyPDF2 import PdfReader, PdfWriter

path = 'singleson.pdf'

pdf=PdfReader(path,'rb')

print("The file splitting into pages")

for i in range(len(pdf.pages)):
    writer=PdfWriter()
    writer.add_page(pdf.pages[i])
    #writer.add_page(pdf.pages[i])


    output= f'page {i + 1}.pdf'
    with open(output,'wb') as out:
        writer.write(out)

print("Page Spliting Done")