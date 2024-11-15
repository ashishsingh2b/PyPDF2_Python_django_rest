from PyPDF2 import PdfReader, PdfWriter

# Open the original PDF and the watermark PDF
pdf = PdfReader('singleson.pdf')
watermark = PdfReader('water.pdf')

# Create a writer object to write the output
writer = PdfWriter()

# Get the watermark page (assuming watermark.pdf has only one page)
watermark_page = watermark.pages[0]

# Loop through each page in the original PDF and apply the watermark
for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    page.merge_page(watermark_page)  # Use merge_page() in PyPDF2 3.x+
    writer.add_page(page)

# Write the result to a new PDF file
with open('newfile.pdf', 'wb') as out:
    writer.write(out)

print("Watermark applied successfully!")
