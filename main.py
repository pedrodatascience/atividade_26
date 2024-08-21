def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

#progrma principal
if __name__ == '__main__':
    try:
        n = int(input('Informe um numero unteiro positivo: '))

        if n >= 0:
            print(f'O fatorial de {n} é {fatorial(n)}.')
            
        else:
            print(f'Não existe fatorial de {n}.')
    except:
        print('Não foi possível calcular o fatorial')