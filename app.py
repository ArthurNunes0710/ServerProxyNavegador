from trabalho_web_proxy import app
from flask import Flask, request
import json
import datetime

@app.route("/bloqueado")
def site_bloqueado():
    # abrir o site - sem mostrar ao cliente
    with open("blocked.json") as arquivo:
        