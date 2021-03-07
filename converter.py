import PyPDF2

ob = PyPDF2.PdfFileReader(//enter pdf file in single quotes//)

tx=""

for i in range(13,16):
    tx+= ob.getPage(i).extractText()

with open("text.txt","w",encoding='utf-8') as f:
    f.write(tx)
