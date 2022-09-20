from random import randint
from time import sleep
start = 0
while start != 3:
    maquina = randint(1, 99)
    pontosfacil = 20
    pontosmed = 10
    pontosdif = 5
    print('=-' * 20)
    print('\nBem Vindo ao Jogo dos Numeros\n')
    print('Dev - Vitor')
    print('=-' * 20)

    while True:
        try:
            start = int(input('\nDigite 1 para Começar, 2 Para Ajuda, 3 para sair\n'))
            if start == 2:
                print('O jogo funciona assim, a maquina escolhe um numero entre 1 e 99,\no seu objetivo é advinhar'
                      ' qual é esse numero,\nquanto mais rapido voce acertar, mais pontos você tem!')
                continue
            break

        except ValueError:
            print('\nValor Digitado Errado\n')
            continue
    if start == 1:
        while True:
            try:
                dificuldade = int(input('Digite qual a Dificuldade 1 para facil 2 para medio e 3 para dificil '))
            except ValueError:
                print('Valor Invalido')
            if dificuldade == 1:
                pontosjogo = pontosfacil
                break
            elif dificuldade == 2:
                pontosjogo = pontosmed
                break
            elif dificuldade == 3:
                pontosjogo = pontosdif
                break
            else:
                print('Valor digitado invalido')
                continue
        jogador = 0
        tentativas = 1
        pontosjogo = pontosjogo - 1
        print('A maquina esta pensando em um numero...')
        sleep(1)
        while jogador != maquina:
            try:
                jogador = int(input('Tente advinhar o Numero!: '))
            except ValueError:
                print('Valor Digitado Invalido')
            if pontosjogo == 0:
                print(f'Voce perdeu o numero era {maquina}')
                break
            if jogador < maquina:
                print(f'Você errou, o Numero é maior, restam {pontosjogo} tentativas')
                pontosjogo = pontosjogo - 1
                tentativas = tentativas + 1
            elif jogador > maquina:
                print(f'Você errou, o numero é menor, restam {pontosjogo} tentativas')
                pontosjogo = pontosjogo - 1
                tentativas = tentativas + 1
            else:
                print(f'Você acertou! o numero era {maquina}\n')
                print(f'Voce acertou utilizando {tentativas} parabens!\n')
                break
    else:
        print('Saindo...')
        sleep(1)
