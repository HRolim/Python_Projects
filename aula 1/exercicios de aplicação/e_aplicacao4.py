from xml.etree.ElementTree import C14NWriterTarget


print("Cálculo de Bhaskara")
print("\nPara começar, você deve ter em mãos os valores dos coeficientes A,B e C")

A = int(input("Digite aqui o valor do coeficiente A: "))
B = int(input("Digite aqui o valor do coeficiente B: "))
C = int(input("Digite aqui o valor do coeficiente C: "))

delta = B*B - 4*A*C

raiz = delta ** 0.5

numPos = -B + raiz
raiz1 = numPos / 2*A

numNeg = -B - raiz 
raiz2 = numNeg / 2*A


print("As raizes da equação são:",raiz1,"e",raiz2)

