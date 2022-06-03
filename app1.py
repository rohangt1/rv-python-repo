import os
import comtypes.client
wdFormatPDF = 17

#in_file = os.path.abspath("H:\Business Works\Source Code\Ruby\OUTPUT11.docx")
in_file = os.path.abspath("OUTPUT11.docx")
#out_file = os.path.abspath("H:\Business Works\Source Code\Ruby\OUTPUT11.pdf")
out_file = os.path.abspath("OUTPUT11.pdf")

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()