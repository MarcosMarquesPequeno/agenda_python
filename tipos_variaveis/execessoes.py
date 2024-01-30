try:
    numero = int(input("Digite um neumro inteiro: "))
    resultado = 10 / numero

except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operacao finalizada!")
