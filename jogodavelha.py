import random

def jogo_da_velha_inteligente():
    tabuleiro = [" " for _ in range(9)]
    
    def mostrar_tabuleiro():
        print()
        print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
        print("--+---+--")
        print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
        print("--+---+--")
        print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print()
    
    def checar_vencedor(jogador):
        combinacoes = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for c in combinacoes:
            if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
                return True
        return False
    
    def jogada_computador():
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                if checar_vencedor("O"):
                    return i
                tabuleiro[i] = " "
        
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                if checar_vencedor("X"):
                    tabuleiro[i] = "O"
                    return i
                tabuleiro[i] = " "
        
        if tabuleiro[4] == " ":
            tabuleiro[4] = "O"
            return 4
        
        cantos = [0,2,6,8]
        random.shuffle(cantos)
        for i in cantos:
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                return i
        
        laterais = [1,3,5,7]
        random.shuffle(laterais)
        for i in laterais:
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                return i

    jogador_atual = "X"  
    rodadas = 0

    while rodadas < 9:
        mostrar_tabuleiro()

        if jogador_atual == "X":
            pos = input("Escolha uma posição (1-9): ").strip()
            if not pos.isdigit():
                print("Digite um número de 1 a 9!")
                continue
            pos = int(pos) - 1
            if pos < 0 or pos > 8:
                print("Escolha inválida! Digite de 1 a 9.")
                continue
            if tabuleiro[pos] != " ":
                print("Posição ocupada! Tente outra.")
                continue
            tabuleiro[pos] = "X"
        else:
            pos = jogada_computador()
            print(f"Computador jogou na posição {pos + 1}")

        rodadas += 1

        if checar_vencedor(jogador_atual):
            mostrar_tabuleiro()
            if jogador_atual == "X":
                print("Parabéns! Você venceu! 🏆")
            else:
                print("O computador venceu! 😢")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    mostrar_tabuleiro()
    print("Empate! 🤝")


jogo_da_velha_inteligente()
