from PyPDF2 import PdfReader, PdfWriter

# Open the existing PDF
pdf = PdfReader('page 5.pdf')

# Create a PdfWriter object to write the encrypted PDF
writer = PdfWriter()

# Add pages to the writer
for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    writer.add_page(page)

# Encrypt the PDF with a user password and an optional owner password
user_password = 'pass@123'
owner_password = None  # If you want an owner password, set it here (e.g., 'ownerpass')
writer.encrypt(user_password, owner_password, use_128bit=True)

# Write the encrypted PDF to a new file
with open('passwordpdfile.pdf', 'wb') as out:
    writer.write(out)

print("PDF encryption completed successfully.")
