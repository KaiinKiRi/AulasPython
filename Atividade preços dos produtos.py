produtos = ["Leite","Arroz","Feijão","Queijo","Macarrão","Shampoo","Biscoito","Margarina","Creme","Suco"]
preco = []
print(produtos)
for p in produtos:
    preco.append(float(input("Informe o valor do primeiro produto "+p+" : ")))
soma = sum(preco)
print("O somatório dos preços é igual a:",soma)
print("O maior preço é: ",max(preco))
print("O menor preço é: ",min(preco))

        
