# Lista colecao de elemento mutaveis
# Declaracao
minha_lista = [1, 2, 3, 4, 5, "rocktseat", True, False]

print("minha lista: ", minha_lista)
print("minha_lista[0]: ", minha_lista[0])
print("minha_lista[0]: ", minha_lista[5])
print("slice > minha_lista[1:7]: ", minha_lista[1:7])  # slices
print("slice > minha_lista[:6]: ", minha_lista[:6])
print("slice > minha_lista[2:]: ", minha_lista[2:])

# Alterar item da lista
minha_lista[0] = "python"

# Metodos de lista
# Metodo .append(): add elemento ao final da lista
minha_lista.append(6)
print("append(6):", minha_lista)

# Metodo .index() retorna o indice do elemento igual oa valor expecificado
indice = minha_lista.index(6)
print("indexdo elemento 6:", indice)

# Metodo .insert() insere um elemento em um idixe expecifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10)", minha_lista)

# Metodo .pop() remove e retorna um elemento de um indice expecifico
elemento_removido = minha_lista.pop(3)
print("elemento removido", elemento_removido)
print("Apos o .pop(3)", minha_lista)

# Metodo .remove() remover o primeiro elemento com o valor expecificado
minha_lista.remove(True)
print("Apos o .remove(True)", minha_lista)

# Metodo .sort() organizar em ordem crescente
lista_sort = [3, 4, 5, 1, 11, 66, 787, 5, 97, 23, 41, 56]
lista_sort.sort()
print("Apos o .sorte", lista_sort)
