from flask import Flask, send_file
from flask_cors import CORS
import requests
import io

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    url = "https://www.mangasaki.org/sites/default/files/manga2/4/1011482//20240311053029391.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        print("loaded!")
    return send_file(
                     io.BytesIO(response.content),
                     attachment_filename='logo.jpeg',
                     mimetype='image/jpg'
               )

if __name__ == '__main__': 
    app.run()