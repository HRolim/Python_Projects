print("\n=+Delta real ou irracional  +=")

A = int(input("\nDigite aqui o valor do coeficiente A: "))
B = int(input("Digite aqui o valor do coeficiente B: "))
C = int(input("Digite aqui o valor do coeficiente C: "))

delta = B*B - 4*A*C

if  delta >= 0:
    delta = delta**0.5 

    numPos = -B + delta
    numPos = numPos / 2*A

    numNeg = -B - delta 
    numNeg = numNeg / 2*A
    print("As raízes da equação são:",numPos,"e",numNeg)


elif delta < 0:
    print("Não há raízes reais, pois o delta é menor que zero")


else:
    print("tente novamente")

