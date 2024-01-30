def saudacao(nome):
    print(f"Olá, : {nome}!")


print("chamando funcao")
saudacao("marcos")

# Funcao com retorno


def quadrado(n):
    res = n**2
    return res


print("chamando funcao quadrado")
res_quadrado = quadrado(5)
print(res_quadrado)

# Funcao com multiplos parametros


def soma(n1, n2):
    res = n1 + n2
    return res


print("chamando funcao com multiplos")
res_soma = soma(5, 4)
print(res_soma)
