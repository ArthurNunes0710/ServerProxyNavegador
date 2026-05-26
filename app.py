from flask import Flask , render_template , url_for , request , redirect , session
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"] )
def inicio():
    if request.method == "POST":
    
        url =  request.form.get("url")    

        return redirect(f"/{url}")

    return render_template("inicio.html")


@app.route("/<path:url>", methods=["GET", "POST"] )
def proxy(url):
    if request.method == "GET":
    
        resposta = requests.get(url)    

        return resposta.text



app.run(host='0.0.0.0', port=8080)