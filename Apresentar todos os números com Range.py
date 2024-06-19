#Exemplo 1 - Matriz
moradores = ["Ana","Maria","Joana"]
apart = [["1001","1002","1003"],
         ["2001","2002","2003"],
         ["3001","3002","3003"]]
print(moradores[1])
for linha in range(3):
    for coluna in range(3):
        print(apart[linha][coluna])
