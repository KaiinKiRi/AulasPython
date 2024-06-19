#Exemplo 2 - Vetor
frutas = ["Goiaba","Uva","Laranja","Limão"]
print(frutas)
n = int(input("Digite um número de  0 a 3: "))
if n > 3 or n < 0:
    print("O valor informado é inválido!")
else:
    print("Sugestão do dia: ",frutas[n])
