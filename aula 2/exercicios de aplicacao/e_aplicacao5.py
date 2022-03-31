print("Conversão de dólar e real")

dolar = float(input("\nQual o valor do dólar hoje? "))


equ = 1 * dolar
print("Então 1 dólar equivale a R$", equ)

equ1 = 1 / dolar
print("\nE 1 real equivale a U$:",equ1)


qntDolar = float(input("\nQual a quatidade de reais a serem convertidos para dólares? "))
con = qntDolar / dolar
print("Então, R$",qntDolar,"equivale a U$",con)


qntReal = float(input("\nQual a quatidade de dólares a serem convertidos para Reais "))
con = qntReal * dolar
print("Então, U$",qntReal,"equivale a R$",con)