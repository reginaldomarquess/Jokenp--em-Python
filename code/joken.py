'''Crie um programa que faça o computador jogar Jokenpô com você'''
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
while True:
    computador = randint(0, 2)
    # Nessa linha eu fiz o computador puxar os "itens" que estavam entre parênteses (Pedra, Papel, Tesoura) ao invés de "0 a 2"
    # Itens {itens} na posição computador [computador] = {itens[computador]}
    # print(f'O computador escolheu {itens[computador]}')
    print('======================================================')
    print('Jogo do Jokenpô!!\nO computador irá jogar com você. Tente vencê-lo!')
    print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    print('======================================================')

    jogador = int(input('Qual é a sua jogada? '))
    if jogador not in [0, 1, 2]:
        print('Jogada \33[0;31;41mINVÁLIDA\33[m')
    else:
        print('Jo')
        sleep(0.5)
        print('Ken')
        sleep(0.5)
        print('Pô!!!')
        print('-=' * 20)
        print(f'O computador jogou {itens[computador]}')
        print(f'O jogador jogou {itens[jogador]}')
        print('-=' * 20)

    if computador == 0:  # se o computador jogou Pedra
        if jogador == 0:
            print('EMPATE🤪')
        elif jogador == 1:
            print('O JOGADOR VENCEU🎉')
            break  # Sai do loop quando o jogador vencer
        elif jogador == 2:
            print('O COMPUTADOR VENCEU 🦾')
        else:
            print('JOGADA \33[0;31;41mINVÁLIDA\33[m')

    elif computador == 1:  # se o computador jogou Papel
        if jogador == 0:
            print('O COMPUTADOR VENCEU 🦾')
        elif jogador == 1:
            print('EMPATE🤪')
        elif jogador == 2:
            print('O JOGADOR VENCEU🎉')
            break  # Sai do loop quando o jogador vencer
        else:
            print('JOGADA INVÁLIDA')

    elif computador == 2:  # se o computador jogou Tesoura
        if jogador == 0:
            print('O JOGADOR VENCEU🎉')
            break  # Sai do loop quando o jogador vencer
        elif jogador == 1:
            print('O COMPUTADOR VENCEU 🦾')
        elif jogador == 2:
            print('EMPATE🤪')
