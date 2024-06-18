def parImpar(resultado):
    if resultado % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


Numero1 = input("Digite o primeiro numero: ")
Numero2 = input("Digite o segundo numero: ")

try:
    numero1 = float(Numero1)
    numero2 = float(Numero2)
    resultado = (numero1 + numero2)
    resultado2 = parImpar(resultado)
    print(f"A soma de {Numero1} e {Numero2} é {resultado}")
    print(f"O numero {resultado} é {resultado2}")
    
except:
    print("Entrada inválida")  
    
