#TO get total pages inside of pdf

# import PyPDF2

# f= open('O_Son_.pdf','rb')

# pdf= PyPDF2.PdfReader(f)

# print(len(pdf.pages))

# f.close()

import PyPDF2

# Open the PDF file
f= open('O_Son_.pdf', 'rb')
    # Read the PDF file
pdf = PyPDF2.PdfReader(f)

    # Get the first page
page = pdf.pages[10]

    # Extract text from the first page
print(page.extract_text())

    # Print the extracted text
f.close()
