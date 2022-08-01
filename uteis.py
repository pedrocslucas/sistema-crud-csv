def lerInt(txt):
    while True:
        try:
            op = int(input(txt))
        except ValueError:
            print('Digite um número inteiro...')
        else:
            break
    return op


