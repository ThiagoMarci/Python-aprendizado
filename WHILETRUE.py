from random import randint
v = 0
while True:
    print('=-'*20) 
    print('JOGO DA ESCOLHA PAR OU IMPAR')
    print('=-'*20)
    jogador = int(input('Digite um numero entre 0 e 10 :'))
    pc = randint(0,10)
    total = jogador + pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou IMPAR : [P/I]')).upper().strip()[0]

    if escolha == 'P':
        if total % 2 == 0:
            print ('WIN PARABENS')
            v += 1
        else:
            break
            print ('YOU LOSER') 
    elif escolha == 'I':
        if total % 2 == 1:
            print ('WIN PARABENS')
            v += 1
        else:
            break
            print ('YOU LOSER')
    print (f'Você jogou {jogador} e o pc jogou {pc} e o total foi {total}')
    print('jogue novamente........')
print(f'GAME OVER, VOCÊ VENCEU {v} VEZES')
