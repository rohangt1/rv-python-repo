import ftplib
a = 1
b = 2
c = a + b
session = ftplib.FTP('ftp.cwac.in','cwacin','$Rv01111996')
file = open('OUTPUT11.docx','rb')                  # file to send
session.storbinary('STOR OUTPUT11.docx', file)     # send the file
file.close()                                    # close file and FTP
session.quit()