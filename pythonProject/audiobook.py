"""
here we are doing to convert txt file into audio file...
for that there is need of one module i.e pyttsx3
which is used to convert txt into audio format
"""
import pyttsx3 # Python Text to Speech module version x3
import PyPDF2  # Python PDF Reader
book=open('ms-17.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker= pyttsx3.init()
page=pdfReader.getPage(1)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
