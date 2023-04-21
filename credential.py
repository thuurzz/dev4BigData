import os
from dotenv import load_dotenv

# carrega as variáveis do arquivo .env
load_dotenv()

# acessa as variáveis do arquivo .env como se fossem variáveis normais em Python
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

print({
    client_id, client_secret, redirect_uri
})