import requests
import json

def converter(valor, de, para):
    api = requests.get(f'https://economia.awesomeapi.com.br/{de}-{para}/')

    if api.status_code == 200:
        response = api.json()
        calculo = float(response[0]['bid']) * valor
        return round(calculo,2)
    else:
        return None
    
print("=== Conversor de moedas ===")
print("Principais moedas disponíveis: USD, BRL, EUR, JPY, BTC, ETH, DOGE, ETC.")

valor = float(input("valor: "))
de = input("converter de (código): ")
para = input("converter para (código): ")

cotacao = converter(valor, de, para)

if cotacao is not None:
    print(f'{valor} {de} é equivalente a {cotacao} {para}')
else:
    print("Erro: moeda inválida")    