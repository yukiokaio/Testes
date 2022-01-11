n = int(input("Que termo deseja encontrar: "))
anterior = 0
proximo = 0
encontrou = False 

while(proximo <= n):
    if (proximo == n):
        print("O número", n, "pertence a sequência!")
        encontrou = True
        break
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1

if (encontrou == False):
    print("O número", n, "não pertence a sequência!")
