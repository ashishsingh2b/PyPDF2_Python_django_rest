# from PyPDF2 import PdfReader

# # path = '2224127341.pdf'
# path ='c11558c8-5354-499d-b2f3-9a5a561dc383.pdf'
# with open(path, 'rb') as f:
#     pdf = PdfReader(f)
#     information = pdf.metadata  # Access metadata as an attribute, not a method

#     # Print the metadata
#     print(information)


# from PyPDF2 import PdfReader

# # Path to the PDF file
# path = 'c11558c8-5354-499d-b2f3-9a5a561dc383.pdf'

# with open(path, 'rb') as f:
#     pdf = PdfReader(f)
#     metadata = pdf.metadata  # Access metadata as an attribute
    
#     # Print each metadata key and value
#     print("PDF Metadata:")
#     for key, value in metadata.items():
#         print(f"{key}: {value}")



from PyPDF2 import PdfReader

# Path to the PDF file
path = 'O_Son_.pdf'

with open(path, 'rb') as f:
    pdf = PdfReader(f)
    metadata = pdf.metadata  # Access metadata as an attribute
    
    # Print each metadata key and value
    print("PDF Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
