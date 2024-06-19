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
    if matriz[linha][coluna] == posicao:
        return False
    else:
        return True

def registraJogada(mat, posicao, jogador):
    linha = (posicao-1)//3
    coluna =(posicao-1)%3
    matriz[linha][coluna] = jogador
    return mat

def trocaJogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"
        

def verificaGanhador(mat, jogador):
    return

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
    # Final do if     
    c += 1
# Final do while
# Final do programa
