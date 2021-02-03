import pyttsx3
import PyPDF2
bok = open('test.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(bok)
pages = pdfReader.numPages
print(pages)
sp = pyttsx3.init()
for num in range(2, pages):
	pag = pdfReader.getPage(3)
	text = pag.extractText()
	sp.say(text)
	sp.runAndWait()