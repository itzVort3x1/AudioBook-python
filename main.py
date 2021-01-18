import pyttsx3
import PyPDF2

file = open('<Add a file with .pdf extension here>', 'rb')
fileReader = PyPDF2.PdfFileReader(file)
number_of_pages_in_file = fileReader.numPages
print(number_of_pages_in_file)
siri = pyttsx3.init()
page = fileReader.getPage('Add a page number from where you want it to start')
file_text = page.extractText()
siri.say(file_text)
siri.runAndWait()