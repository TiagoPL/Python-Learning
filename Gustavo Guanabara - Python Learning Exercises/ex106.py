from time import sleep

c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7;30m')      # 6 - Branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('=' * (len(msg) + 4))
    print(msg)
    print('=' * (len(msg) + 4))
    print(c[0], end='')
    sleep(0.5)


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)
