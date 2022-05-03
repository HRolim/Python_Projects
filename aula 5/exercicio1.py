print("=+ Classe eleitoral+=")

age = int(input("Informe a sua idade: "))

if age <= 16:
    print("Você não pode tirar o título")

if age >= 18 and age <= 65:
    print("Você é um eleitor obrigatório e deve votar nas próximas eleições")

if age >= 16 and age == 17 or age < 65:
    print("Você é um eleitor facultativo, pode ou não votar")
