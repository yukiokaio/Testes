faturamento = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88,
               'ES': 27165.48, 'OUTROS': 19849.53}

total = sum(faturamento.values())
percentual = 0

for i in faturamento:
    percentual = ((faturamento[i]/total)*100)
   
    print("O percentural de representação de(os)", i, "é:", round(percentual,2))

   
