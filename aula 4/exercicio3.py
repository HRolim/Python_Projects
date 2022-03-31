print("==Conversor de anos para dias==")

idade = int(input("Insira sua idade expressa em anos "))
meses = int(input("Quantos meses se passaram desde seu último aniversário "))
dias = int(input("Quantos dias se passaram desde seu último aniversário "))


idade1 = idade * 365
meses1 = meses * 30

idadeFinal = idade1 + meses1 + dias

print("Sua idade em dias é de: ",idadeFinal)

