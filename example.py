def dividir(dividendo, divisor):
    print(dividir.resultado)
    return dividendo / divisor


def testa_divisao(divisor):
    try:
        resultado = dividir(10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} é {resultado}")
    except ZeroDivisionError:
        print("Erro de divisão por zero tratado")


try:
    testa_divisao(0)
except AttributeError:
    print("Erro de atributo")

print("Programa encerrado")
