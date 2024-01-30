pessoa = {"nome": "Joao", "idade": 30, "cidade": "Manaus"}
print("Dicionario:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

# Metodo: keys() retorno de todas a chaves do dicionario (transforma dicionario em lista)
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("primeira chave:", chaves[0])

# Metodo values() retorno de todas os valores do dicionario (transforma dicionario em lista)
valores = list(pessoa.values())
print("Todos os valores do dicionario:", valores)
print("primeiro valor:", valores[0])

# Metodo items() lista de tuplas contendo todos os pares chaves-valor (transforma dicionario em lista)
itens = list(pessoa.items())
print("lsita de tuplas contendo todos os pares chaves-valor:", itens)
print("primeiro chave-valor: %s = %s" % (itens[0][0], itens[0][1]))
