from datetime import date


def voto(n):
    if date.today().year - n < 16:
        return'Voto NEGADO'
    elif (date.today().year - n > 15) and (date.today().year - n < 18):
        return'Voto OPCIONAL'
    elif date.today().year - n > 64:
        return'Voto OPCIONAL'
    else:
        return'Voto OBRIGATORIO'


n1 = int(input('Digite seu ano de nascimento: '))
print(f'Com {date.today().year - n1} anos: {voto(n1)}.')
