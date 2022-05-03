print("=+ Calculadora +=")

num1 = float(input("Insira o primeiro número "))
num2 = float(input("Insira o segundo número "))

print("\x1b[2J\x1b[1;1H")
print("Selecione uma operação")
print("\n[1] - Adição")
print("[2] - Subtração")
print("[3] - MUltiplicação")
print("[4] - Divisão")
opcao = input("\nInsira a operação desejada ")

if opcao == '1':
    num3 = num1 + num2
    print("O resultado é",num3)

elif opcao == '2':
    num3 = num1 - num2
    print("O resultado é",num3)

elif opcao == '3':
    num3 = num1 * num2
    print("O resultado é",num3)

elif opcao == '4':
    num3 = num1 / num2
    print("O resultado é",num3)

else:
    print("Por favor, selecione uma opção válida")