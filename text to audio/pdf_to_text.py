import PyPDF2  
    
# creating a pdf file object  
pdfFileObj = open(r'C:\Users\saket\Downloads\Documents\science\The Feynman Lectures on Physics, Volume 1_ Mainly Mechanics, Radiation, and Heat (The New Millennium Edition - Desktop Edition) ( PDFDrive ).pdf', 'rb')
    
# creating a pdf reader object  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
    
# printing number of pages in pdf file  
print(pdfReader.numPages)  

# creating a page object  
pageObj = pdfReader.getPage(3)  

# extracting text from page  
print(pageObj.extractText())

# closing the pdf file object  
pdfFileObj.close()