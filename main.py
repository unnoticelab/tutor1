from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder='templates')

@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route("/sakti")
def sakti_page():
    title = "Sakti"
    return render_template("index.html", title=title)

@app.route("/monev")
def monev_page():
    title = "monev"
    return render_template("index.html", title=title)

@app.route("/input")
def input_page():
    title = "input"
    return render_template("index.html", title=title)

@app.route("/kirim", methods=['POST'])
def send_data():
    with open("test.txt", "a") as f:
        f.write(request.form['nama'] + "," + request.form['nomor']) 
        f.write("\n")

    return "Data terkirim"

@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files['file']

    filename = secure_filename(file.filename)

    file.save(os.path.join("uploads", filename))

    with open(os.path.join("uploads", filename), "r") as f:
        for line in f:
            with open("test.txt", "a") as g:
                g.write(line)

    return "File terupload"

if __name__ == "__main__": 
    app.run(debug=False)
