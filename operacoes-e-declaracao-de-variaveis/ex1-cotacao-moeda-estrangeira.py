#EXERCICIO 1: COTAÇÃO DE MOEDA ESTRANGEIRA

import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
dataDolar = requisicao.json()
requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
dataEuro = requisicao.json()
requisicao = requests.get('https://economia.awesomeapi.com.br/all/GBP-BRL')
dataLibra = requisicao.json()

precoDolar = float(dataDolar['USD']['bid'])
precoEuro = float(dataEuro['EUR']['bid'])
precoLibra = float(dataLibra['GBP']['bid'])

#print(precoDolar, precoEuro, precoLibra)

print("Digite a moeda que você deseja comprar")
print("1 - dolar")
print("2 - euro")
print("3 - libra")
moeda = int(input())

print("Digite o valor da moeda que você deseja comprar")
valor = float(input())

if moeda == 1:
    print("Você deve pagar ", precoDolar*valor, " reais")
elif moeda == 2:
    print("Você deve pagar ", precoEuro*valor, " reais")
elif moeda == 3:
    print("Você deve pagar ", precoLibra*valor, " reais")
else:
    print("Moeda não reconhecida")
