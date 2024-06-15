def parImpar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
entrada = input("Digite um numero inteiro: ")

try:
    numero = int(entrada)
    resultado = parImpar(numero)
    print(f"O numero {numero} é {resultado}")
    
except:
    print("Erro: Digite um numero inteiro")    
       