from flask import Flask, render_template, request, redirect 
import requests
import json
from urllib.parse import urlparse
import re
from datetime import datetime

# função para escrever mensagens de aviso em um arquivo log.json sobre os resultados das requisições
def log(horario, url, acao):
    # formato das mensagens de log 
    arquivo_log = {
        "Horario": horario,
        "URL solicitada": url,
        "Acao executada": acao
    }

    try:
        with open("log.json", "r") as arquivo:
            msgs = json.load(arquivo) # carrega o conteúdo do arquivo log.json
    except:
        msgs = [] # cria uma lista de mensagens caso o arquivo esteja vazio

    msgs.append(arquivo_log) # adiciona a mensagem na lista

    with open("log.json", "w") as arquivo:
        json.dump(msgs, arquivo, ensure_ascii = False) # escreve as mensagens de log no arquivo log.json

with open("blocked.json", "r") as arquivo:
    domin = json.load(arquivo)

domin_bloq = domin["bloqueados"]

with open("words.json", "r") as arquivo:
    palavras = json.load(arquivo)

app = Flask(__name__)

@app.route("/<path:url>", methods=["GET", "POST"] )
def proxy(url):
    if request.method == "GET":
        
        d = urlparse(url).netloc
        if d in domin_bloq:
            # chama a função de escrever as mensagens de log no arquivo log.json e escreve o horário, url e que a url é bloqueada 
            log(datetime.now().strftime("%d/%m - %H:%M:%S"), url, "bloqueado")

            return render_template("bloqueado.html")
        
        resposta = requests.get(url)
        pagina = resposta.text   

        pagina_filtrada = False 
        
        for p, subs  in palavras.items():
            # busca pelas palavras proibidas no words.json e verifica se elas aparecem no site
            if re.search(p, pagina, re.IGNORECASE):
                pagina_filtrada = True 
            pagina = re.sub(p,subs,pagina,flags=re.IGNORECASE)
    
        if pagina_filtrada:
            log(datetime.now().strftime("%d/%m - %H:%M:%S"), url, "filtrado") # chama a função log e escreve no arquivo log.json o horário, url e que a url é filtrada

        else:
            log(datetime.now().strftime("%d/%m - %H:%M:%S"), url, "permitido") # chama a função log e escreve no arquivo log.json o horário, url e que o site é permitido 

        return pagina
    
app.run(host='0.0.0.0', port=8080)
