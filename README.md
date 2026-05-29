# ServerProxyNavegador

Um código que simula o comportamento de um servidor Proxy e atua como intermediário na navegação, bloqueando ou permitindo o acesso ao site ou também filtrando palavras proibidas.


## Instalação de dependências 

Para instalar o Flask é necessário criar um ambiente virtual através do comando: ```py -m venv venv```, ativá-lo por meio da instrução ```.\venv\scripts\activate``` e para a sua instalação deve-se utilizar o ```pip install flask```.

Para as demais bibliotecas que não são padrão do python, como a requests deve-se usar o comando ```pip install requests```.


## Como executar o Proxy

Para iniciar o Proxy é necessário apenas executar o arquivo ```app.py```, e então na url do seu navegador digitar a porta ```http://localhost:8080/``` + o site que se deseja acessar, por exemplo: ```http://localhost:8080/http://guthib.com```e se estiver bloqueado entrará em uma página específica para os sites bloqueados que apenas diz 'Não' no centro da tela. Além disso, se o site conter algumas das palavras proibidas do arquivo words.json seu conteúdo será filtrado e se o site não tiver algumas das palavras contidas no arquivo words.json seu conteúdo será mostrado no arquivo log.json como permitido.

## Arquivo de logs
Ao acessar o site as requisições recebidas são armazenadas em um arquivo log.json que armazena requisições no formato: **horário, url do site e a ação executada (permitido, bloqueado ou filtrado)**.
