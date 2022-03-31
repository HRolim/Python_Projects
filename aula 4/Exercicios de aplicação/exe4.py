print("=+ despesas domesticas +=")

light = int(input("Qual o valor da conta de luz? "))
water = int(input("Qual o valor da conta de água? "))
phone = int(input("Qual o valor da conta de telefone? "))

# print("\x1b[2J\x1b[1;1H")

payment = int(input("Qual seu salário? "))

expenses = light + water + phone

if expenses < payment:
    final = payment - expenses
    print("Você vai conseguir pagar suas contas, e vai sobrar:",final,"$")

if expenses > payment:
    final = expenses - payment
    print("Você não vai conseguir pagar todas as contas. Será necessário mais",final,"$ para pagar tudo")

if expenses == payment:
    print("Todas as contas foram pagas, porém você está sem dinheiro")