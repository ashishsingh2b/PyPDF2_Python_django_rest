import img2pdf

img= 'peals.jpeg'

f =open('pealspdf.pdf','wb')
f.write(img2pdf.convert(img))
f.close()