print("=+Calcule o Lucro+=")

nome = input("Insira o nome do produto: ")
valor = float(input("Insira o valor do produto: "))

if valor < 10.00:
    valor = valor + (valor * 0.7)
    print(nome,"terá o valor da venda de",valor)

elif 10.00 <= valor < 30.00:
    valor = valor + (valor *0.5)
    print(nome,"terá o valor da venda de",valor)

elif 30.00 <= valor < 50.00:
    valor = valor + (valor *0.4)
    print(nome,"terá o valor da venda de",valor)

elif valor >= 50.00:
    valor = valor + (valor *0.3)
    print(nome,"terá o valor da venda de",valor)