# Colecao ordenada( lista) e imutavel (nao pode mudar) de elementos
# Tupla se usa ()
tupla = (1, 2, 2, 3, 4)

print("tupla[0]:", tupla[0])
print("tupla[2]:", tupla[2])
print("tupla[-1]:", tupla[-1])

# Metodo .count()
contagem = tupla.count(2)
print("quantidade de vezes que o elemento 2 aparece", contagem)

# Metodo .index()
indice = tupla.index(2)
print("Indice da primeira ocorrencia do elemento 2:", indice)
