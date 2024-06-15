nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))
presencatotal = 100
aulasfrequentadas = float(input("Digite sua frequência: "))
presenca =  aulasfrequentadas / presencatotal * 100
print(float(presenca))
if nota >= 7 and presenca >= 75:
    print ("Aprovada")
else:
    print ("Reprovada")
