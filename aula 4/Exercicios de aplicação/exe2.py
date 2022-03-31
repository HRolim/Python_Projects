noite = 45.00
manha = 37.50

print("=+ Calcule seu salário +=")


turn = input("Qual seu turno de trabalho? ")

while turn != "noite" and turn != "manha":
    if turn != "noite" and turn != "manha":
        turn = input("Por favor, digite um valor válido! (manha ou noite)")
    else:
       break

if turn == "noite":
    salario = 20 * noite
else:
    salario = 20 * manha

print("Seu salário atual é de", salario)