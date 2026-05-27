from flask import Flask , render_template , url_for , request , redirect , session
import requests
import json
from urllib.parse import urlparse
import re

with open("blocked.json", "r") as arquivo:
    domin = json.load(arquivo)

domin_bloq = domin["bloqueados"]

with open("words.json", "r") as arquivo:
    palavras = json.load(arquivo)


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
        


        d = urlparse(url).netloc
        if d in domin_bloq:
            return render_template("bloqueado.html")

        resposta = requests.get(url)
        pagina = resposta.text    
        
        for p, subs  in palavras.items():
            pagina = re.sub(p,subs,pagina,flags=re.IGNORECASE)

        return pagina



app.run(host='0.0.0.0', port=8080)
