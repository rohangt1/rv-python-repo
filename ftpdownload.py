import ftplib
import io
a = 1
b = 2
c = a + b
session = ftplib.FTP('ftp.cwac.in','cwacin','$Rv01111996')
localfile = open("OUTPUT11.docx", 'wb')
#localfile = io.BytesIO()
# def callback(data):
#     localfile.write(data)
session.retrbinary("RETR OUTPUT11.docx", localfile.write)
localfile.close()                                    # close file and FTP
session.quit()