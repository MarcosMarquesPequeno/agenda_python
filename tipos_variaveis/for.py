lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print("lista:", elemento)

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print("tupla:", elemento)


pessoa = {"nome": "Joao", "idade": 30, "cidade": "Manaus"}
print("\n Dicionario - chaves:")
for chave in pessoa.keys():
    print(chave)

print("\n Dicionario - valor:")
for valor in pessoa.values():
    print(valor)

print("\n Dicionario - itens:")
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")

# range(): intervalo numerico
print("\n Utilizando a funcao range()")
for numero in range(3):
    print(numero)

# len()
print("\n Utilizando a funcao range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])

    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
        print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")
