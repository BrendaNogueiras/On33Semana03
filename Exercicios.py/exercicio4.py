def idade (entrada):

 if idade <= 15:
    return "Voce é menor de idade, não pode votar!"
 elif idade < 18:
    return "Você pode votar, mas não é obrigatório"
 else:     
    return"Voce é obrigado a votar"
     
    
entrada = input("Digite sua idade: ")        

try:
    entrada = float(idade)
    resultado = (idade)
    print(resultado)
    
except:
    print("Digite um numero: ")

      
 
    



