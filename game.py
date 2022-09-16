from time import sleep
import random

pontosmaquina = 0
pontosjogador = 0
print('-=' * 15)
print('Bem vindo ao Pedra Papel e Tesoura')
print('Dev - Vitor')

while True:

    print('-=' * 15)
    print (f'Seus Pontos atuais são: {pontosjogador}')
    print (f'Pontos atuais da Maquina: {pontosmaquina}')
    print('-=' * 15)
    start = int(input('Vamos começar? Digite 1 para começar o jogo e qualquer tecla para sair: '))
    if start == 1:
        nomes = ['Pedra', 'Papel', 'Tesoura']
        maquina = random.randint(1,3)
        jogador = int(input('Digite\n1 para Pedra\n2 para Papel\n3 para Tesoura\n'))
        print('Pedra')
        sleep(1)
        print('Papel')
        sleep(1)
        print('e Tesoura...')
        sleep(1)
        print(f'A maquina jogou {nomes[maquina - 1]} e Voce jogou {nomes[jogador -1]}')
        if maquina == 1:
            if jogador == 1:
                print('Deu empate :|')
            elif jogador == 2:
                print('Voce venceu !')
                pontosjogador = pontosjogador +1
            elif jogador == 3:
                print('Voce perdeu :(')
                pontosmaquina = pontosmaquina + 1
            else:
                print('Valor Inválido')
        if maquina == 2:
            if jogador == 1:
                print('Você perdeu :(')
                pontosmaquina = pontosmaquina + 1
            elif jogador == 2:
                print('Deu empate :|')
            elif jogador == 3:
                print('Voce Venceu')
                pontosjogador = pontosjogador + 1
            else:
                print('Valor Inválido')
        if maquina == 3:
            if jogador == 1:
                print('Você Venceu!')
                pontosjogador = pontosjogador + 1
            elif jogador == 2:
                print('Voce Perdeu :(')
                pontosmaquina = pontosmaquina + 1
            elif jogador == 3:
                print('Deu empate :|')
            else:
                print('Valor Inválido')
    else:
        break
