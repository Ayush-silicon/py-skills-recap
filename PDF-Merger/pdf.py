import PyPDF2

pdfiles = ['coding Pattern.pdf', 'Node-js interview questions.pdf']

merger = PyPDF2.PdfMerger()

for pdf in pdfiles:
    with open(pdf, 'rb') as pdf_file:
        merger.append(pdf_file)

with open('merged.pdf', 'wb') as output:
    merger.write(output)

merger.close()
print("PDF files merged successfully into 'merged.pdf'.")