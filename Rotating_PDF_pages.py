import PyPDF2

# Open the PDF file
with open('O_Son_.pdf', 'rb') as f:
    # Read the PDF file
    pdf = PyPDF2.PdfReader(f)
    
    # Create a writer object to save the rotated PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Rotate each page (here we rotate each page by 90 degrees clockwise)
    for page in pdf.pages:
        page.rotate(90)  # Rotate page by 90 degrees clockwise
        pdf_writer.add_page(page)

    # Write the rotated PDF to a new file
    with open('rotated_output.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print("PDF pages rotated successfully and saved as 'rotated_output.pdf'.")
