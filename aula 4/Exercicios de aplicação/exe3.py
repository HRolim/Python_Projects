print("=+ Calcule seu desconto +=")

value = int(input("qual o valor de suas compras? "))

if value >= 200:
    finaValue = value - (value*0.2)
    print("Você recebeu um desconto de 20% e o novo valor é de:",finaValue)
else:
    finaValue = 200 - value
    print("Você não possui desconto, gaste mais",finaValue,"$para recener um desconto")