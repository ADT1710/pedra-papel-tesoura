import random


def jogar():
    usuario = input("Selecione sua escolha:\n"
                    "1-) Pedra\n"
                    "2-) Papel\n"
                    "3-) Tesoura\n"
                    "R: ")
    printa_escolha("Jogador", usuario)

    computador = random.choice(['1', '2', '3'])
    printa_escolha("Computador", computador)

    if usuario == computador:
        return print('Empate')

    elif ganhou(usuario, computador):
        return print("Você ganhou!")

    print("Você perdeu!")


def printa_escolha(jogador,escolha):
    if escolha == "1":return print(f'{jogador} escolheu pedra.')
    elif escolha == "2":return print(f'{jogador} escolheu papel.')
    elif escolha == "3":return print(f'{jogador} escolheu tesoura.')


def ganhou(jogador, oponente):
    if (jogador == '1' and oponente == '3') or (jogador == '2' and oponente == '1') or (jogador == '3' and oponente == '2'):
        return True

jogar()