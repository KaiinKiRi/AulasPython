## -----------------------------------------------------
#    Projeto: Jogo da Velha
#    Disciplina: Lógica de Programação
#    Participantes:
## -----------------------------------------------------

def criaMatriz():
    mat = [    [1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]
              ]
    return mat

def apresentaMatriz(mat):
    print(mat[0][0], "|", mat[0][1], "|", mat[0][2])
    print("-" * 10)
    print(mat[1][0], "|", mat[1][1], "|", mat[1][2])
    print("-" * 10)
    print(mat[2][0], "|", mat[2][1], "|", mat[2][2])
    return

def posicaoOcupada(mat, posicao):
    linha = (posicao-1)//3
    coluna = (posicao-1)%3
    if mat[linha][coluna] in ["X","O"]:
        return True
    else:
        return False

def registraJogada(mat, posicao, jogador):
    linha = (posicao-1)//3
    coluna =(posicao-1)%3
    mat[linha][coluna] = jogador
    return mat

def trocaJogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"
        

def verificaGanhador(mat, jogador):
    combinacoes = [
        [(0, 0), (0, 1), (0, 2)],  # Linha 1
        [(1, 0), (1, 1), (1, 2)],  # Linha 2
        [(2, 0), (2, 1), (2, 2)],  # Linha 3
        [(0, 0), (1, 0), (2, 0)],  # Coluna 1
        [(0, 1), (1, 1), (2, 1)],  # Coluna 2
        [(0, 2), (1, 2), (2, 2)],  # Coluna 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal secundária
    ]

    for comb in comb:
        valores_comb = [mat[pos[0]][pos[1]] for pos in comb]
        if all(valor == jogador for valor in valores_comb):
            return True 
    return False

## ----- Final das funções do usuário

## ----- Programa Principal  
print("*** JOGO DA VELHA *** \n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras:")
print("        a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print("        b) Os números de 1 a 9 representam os espaços que estão livres.")
print("            Você só poderá escolher as posições livres.")
print("        c)  O vencedor será o primeiro Jogador a preencher uma linha, uma coluna ou uma diagonal.")

matriz = criaMatriz()
jogador = "X"                
c = 0
while c < 10:              
    print()
    apresentaMatriz(matriz)
    print()
    posicao = int(input("(Jogador " + jogador + ") Informe a posição desejada : "))
    matriz = registraJogada(matriz, posicao, jogador)
    jogador = trocaJogador(jogador)
    if posicaoOcupada(matriz, posicao):
        print("\nVocê não pode escolher uma posição que já está ocupada. Tente novamente.")
        continue
    else:
         print("Opção válida!")    
    c += 1
# Final do while
# Final do programa
