# if
idade = int(input("Quantos anos voce tem?"))
if idade >= 18:
    print("Maior de idade 1")
else:
    print("Menor de idade 1")

if idade == 19:
    print("Tem 19 anos 2")

if idade < 18:
    print("Menor de idade <= 3")

if idade != 10:
    print("Nao tem 10 anos 4")

# else
if idade >= 18:
    print("Maior de idade else")
elif idade >= 12:
    print("adolecente")
else:
    print("Menor de idade else")

mensagem ="Pode tirar a carteira de habilitacao" if idade >= 18 else "voce nao pode tirar a carteira de habilitacao"
print(mensagem)
