import json

with open("dados.json", encoding = 'utf-8') as meu_json:
    dados = json.load(meu_json)

menor = float("inf")
maior = 0
media = 0
cont = 0
for i in dados:

    if (i['valor'] > 0 and i['valor'] < menor):
        menor = i['valor']
        dia = i['dia']
    
    if (i['valor'] > maior):
        maior = i['valor']
        dia2 = i['dia']
    
    if (i['valor'] > 0):
        cont += 1
        media = media + i['valor']
        
media = media/cont
cont = 0
lista = []
for j in dados:
    if( j['valor'] > media):
        lista.append(j['dia'])
        cont += 1

print("O menor valor de faturamento no mês foi no dia", dia, "com valor:", menor)
print("O maior valor de faturamento no mês foi no dia", dia2, "com valor:", maior)
print("O número de dias com faturamento maior que a média mensal:", cont, "dias")
print("Dias específicos: ", *lista)
