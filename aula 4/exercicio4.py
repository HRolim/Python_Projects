print("Calcule o valor de uma prestação")

prestacao = int(input("Insira o valor da prestação "))
juros = int(input("Insira a porcentagem de juros "))
atraso = int(input("Insira a quantidade de dias de atraso "))

multa = juros/100
atualizado = prestacao + (prestacao*multa*atraso)

print("o valor atualizado da dívida é de",atualizado)