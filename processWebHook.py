import flask
from docx2pdf import convert
import requests
# import ftplib
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
    # session = ftplib.FTP('ftp.cwac.in','cwacin','$Rv01111996')
    # URL = "https://cwac.in/init_certification_client_application/1645433053973/forms/OUTPUT11.docx"
    # response = requests.get(URL)
    # open("output11.docx", "wb").write(response.content)
    # convert("OUTPUT11.docx")
    # convert("OUTPUT11.docx", "OUTPUT11.pdf")
    # file = open('OUTPUT11.pdf','rb')                  # file to send
    # session.storbinary('STOR OUTPUT11.pdf', file)     # send the file
    # file.close()                                    # close file and FTP
    # session.quit()
    #convert("my_docx_folder/")
    #convert("OUTPUT11.docx", "OUTPUT11.pdf")
    return "Converted docx to pdf__now"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()