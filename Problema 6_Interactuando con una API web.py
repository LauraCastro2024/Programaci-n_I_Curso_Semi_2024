import requests 
import json
# Hacemos una solicitud GET a la API de CoinDesk para obtener el precio actual de
Bitcoin
respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
# Convertimos la respuesta a JSON
datos = respuesta.json()
# Obtenemos el precio actual de Bitcoin en USD
precio_bitcoin = datos['bpi']['USD']['rate']
# Imprimimos el precio actual
print(f"El precio actual de Bitcoin es: {precio_bitcoin} USD")