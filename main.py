import random

def jogar():
    usuario = input("Selecione sua escolha:\n"
                    "1-) Pedra\n"
                    "2-) Papel\n"
                    "3-) Tesoura\n"
                    "R: ")

    computador = random.choice(['1', '2', '3'])
    if usuario == computador:
        return print('Empate')

    elif ganhou(usuario, computador):
        return print("Você ganhou!")

    print("Você perdeu!")

def ganhou(jogador, oponente):
    if (jogador == '1' and oponente == '3') or (jogador == '2' and oponente == '1') or (jogador == '3' and oponente == '2'):
        return True

jogar()