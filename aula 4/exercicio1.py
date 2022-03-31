print("==Calcule o volume do tronco de uma pirâmide==")

alt = int(input("Insira o valor da altura do tronco da pirâmide "))
Bmenor = int(input("Insira o valor da base menor pirâmide "))
Bmaior = int(input("Insira o valor da base maior pirâmide "))


volume = alt/3 * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("o volume da pirâmide é: ",volume)
