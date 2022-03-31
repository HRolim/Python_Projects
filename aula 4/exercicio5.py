import math

print("Graus, radianos, seno, cosseno e tangente")

graus = int(input("Insira o valor em graus: "))

radiano = graus * math.pi/180

print("O valor do grau em radianos é:",radiano)
print("O valor do seno é de",math.sin(radiano))
print("O valor do cosseno é de",math.cos(radiano))
print("O valor do tangente é de",math.tan(radiano))