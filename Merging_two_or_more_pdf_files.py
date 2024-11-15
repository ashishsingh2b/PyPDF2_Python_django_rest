from PyPDF2 import PdfReader, PdfWriter

paths = ['myfilea.pdf', 'myfileb.pdf']

writer = PdfWriter()
print("Please wait, file merging is in progress...")

for i in paths:
    pdf = PdfReader(i)  # No need for 'rb' argument
    for page in range(len(pdf.pages)):  # Use len(pdf.pages)
        writer.add_page(pdf.pages[page])  # Use add_page() and index pdf.pages

with open('output.pdf', 'wb') as out:
    writer.write(out)

print("PDF merging completed successfully.")
