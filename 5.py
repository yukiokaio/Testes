text = input("Digite a string a ser invertida:")

text2 = ''

tam = len(text)

while tam:

    tam -= 1
    text2 += text[tam]


print("String invertida:", text2)
