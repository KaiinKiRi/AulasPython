#Exemplo 2 - Vetor
frutas = ["Goiaba","Uva","Laranja","Limão"]
print(frutas)
n = int(input("Digite um número de  1 a 4: "))
if n > 4 or n < 1:
    print("O valor informado é inválido!")
else:
    print("Sugestão do dia: ",frutas[n-1])
