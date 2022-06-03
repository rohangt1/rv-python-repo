import flask
from docx2pdf import convert
import aspose.words as aw
from urllib import request
import ftplib
import os
from flask import send_from_directory
app = flask.Flask(__name__)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():

    # remote_url = 'https://cwac.in/init_certification_client_application/1645433053973/forms/OUTPUT11.docx'
    # # Define the local filename to save data
    # local_file = 'OUTPUT11.docx'
    # # Download remote and save locally
    # request.urlretrieve(remote_url, local_file)

    # session = ftplib.FTP('ftp.cwac.in','cwacin','$Rv01111996')
    # # convert("OUTPUT11.docx")
    # # convert("OUTPUT11.docx", "OUTPUT11.pdf")
    # doc = aw.Document("OUTPUT11.docx")
    # doc.save("OUTPUT11.pdf")
    # file = open('OUTPUT11.pdf','rb')                  # file to send
    # session.storbinary('STOR OUTPUT11.pdf', file)     # send the file
    # file.close()                                    # close file and FTP
    # session.quit()
    return "Converted docx to pdf__now"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()