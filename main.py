from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
logging.basicConfig(level=logging.INFO)
    
## create document for extraction with configurations
pdf_document = Document(
    document_path=r" ",  #add path of pdf
    language="eng"
    )
pdf2text = PDF2Text(document=pdf_document)
content = pdf2text.extract()
length = len(content)
text = ''

for i in range(length):
    matter = content[i]["text"]
            
    text+=matter
    text = str(text).replace("[","")
    text = str(text).replace("]","")
    text = str(text).replace("\\n","")
    text = str(text).replace("\'", "")
        
    #open text file
    text_file = open(r"C:\Users\output.txt", "w", encoding="utf-8")
        
        #write string to file
    text_file.write(text)
    
 
#close file
    text_file.close()