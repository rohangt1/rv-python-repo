import requests
URL = "https://cwac.in/init_certification_client_application/1645433053973/forms/auditor_notes_14001.docx"
response = requests.get(URL)
open("output11.docx", "wb").write(response.content)