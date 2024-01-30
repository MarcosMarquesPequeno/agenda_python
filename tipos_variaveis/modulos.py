from meu_modulo import saudacao, dobro
import math  # res = math.sqrt(raiz_quadrada)
from math import sqrt
print("\nExemplo de importacao de um modulo padrao:")

raiz_quadrada = int(input("Digite um numero, calcular raiz quadrada: "))
res = sqrt(raiz_quadrada)
print(f"Raiz quadrada : {res}")

print("\nExemplo de criacao e utilizacao de um modulo personalizado:")
mensagem = saudacao("Marcos")
resultado = dobro(5)

print(mensagem)
print(resultado)
