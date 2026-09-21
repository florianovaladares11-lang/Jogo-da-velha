def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

def validarVitoria(rodada):
    global parar    
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True     

    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
            
tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]

parar = False
rodada = "X"
Jogadas = 0

while parar == False:
    if Jogadas == 9:
            interface()
            print("Empate!")
            parar = True
    
    interface()

    linha = int(input("Digite a linha escolhida:"))
    coluna = int(input("Digite a coluna escolhida:"))

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        validarVitoria(rodada)
        Jogadas += 1
        rodada = "0"
    
    elif rodada == "0":
        tabuleiro[linha][coluna] = "0"
        validarVitoria(rodada)
        Jogadas += 1
        rodada = "X"

print("Fim de jogo!")
