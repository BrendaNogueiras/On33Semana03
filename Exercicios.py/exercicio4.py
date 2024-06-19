def idade (entrada):
 if entrada <= 15:
    return "Voce é menor de idade, não pode votar!"
 elif entrada < 18:
    return "Você pode votar, mas não é obrigatório"
 else:     
    return "Voce é obrigado a votar"
     
    
entrada = int(input("Digite sua idade: "))       

try:
    Idade = float(entrada)
    resultado = idade(entrada)
    print(resultado)
    
except:
    print("Digite um numero inteiro: ")

      
 
    



