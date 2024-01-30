""" No CMD utlizando o comando python3 para entrar no modo interativo 
nome.upper()            retorna tudo em maiusculo sem alterar os valores;
nome.lower()            retorna o nome minusculo sem alterar os valores; 
nome.count("o")         contar quantas vezes determinada letra se repete;
nome.find("o")          encontrar a possicao da letra
nome.encode()           codificar a variavel em byte
nome.decode()           decotificar a variavel que esta em byte
nome.replace("a", "b")  substituir letras da variavel

"""

nome_completo = "Marcos Marques"

nome_completo_aspas = """Marcos 
Marques"""

nome_completo_quebra = "Marcos \
Marques"

nome = "Marcos "
sobrenome = "Marques"

# Formatacao
print("1 Nome completo:", nome_completo)
print("2 Nome completo:" + nome_completo)
print("3 Nome completo:" + nome_completo + " " "Pequeno Junior")
print("4 Nome completo:" + nome_completo, "Pequeno Junior")
print("5 Nome completo:", nome_completo_aspas)
print("6 Nome completo:", nome_completo_quebra)
print("7 Nome completo: %s" % nome_completo_quebra)
print("8 Nome completo: %s %s" % (nome, sobrenome))  # segura
print(f"9 Nome completo:{nome} {sobrenome}")  # visivelmente agradavel
print("10 Nome completo: {} {}".format(nome, sobrenome))
