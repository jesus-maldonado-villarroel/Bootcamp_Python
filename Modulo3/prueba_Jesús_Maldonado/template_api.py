from consumir_api import request_json

url = "https://aves.ninjas.cl/api/birds"
response = request_json(url)

lista_img = [(elemento['images']['main'], elemento['name']['spanish'],
              elemento['name']['english']) for elemento in response]
