def soma (a, b):
    return a + b

entrada1 = input("Digite o primeiro numero: ")
entrada2 = input("Digite o segundo numero: ")

try:
    numero1 = float(entrada1)
    numero2 = float(entrada2)
    resultado = soma(numero1, numero2)
    print(f"A soma de {numero1} e {numero2} é {resultado}")

except:
    print("Entrada inválida")  
    