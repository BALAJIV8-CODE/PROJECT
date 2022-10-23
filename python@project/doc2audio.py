import pyttsx3 
import PyPDF2 

pdf_file = open('/home/mr__kali008/Dropbox/python@project','rb')
read_pdf = PyPDF2.pdfFileReader(pdf_file, strict = flase)

num_of_page = read_pdf.getNumPages()

engine = pyttsx3.init()

page = read_pdf.getPage(i)a

page_content = page.extractText()

