# Exercise 2: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# ...print out the total, count, and average of the numbers. If the user enters anything other than a
# ...number, detect their mistake using try and except and print an error message and skip to the next number.

contador = 0
soma = 0.0

while True:
    num = input('Insira um número:')

    if num == 'parar':
        break

    try:
        fnum = float(num)

    except:
        print('Erro! Valor inválido.')
        continue

    print(fnum)
    contador = contador + 1
    soma = soma + fnum

print('Tudo pronto!')
print('Total:', soma, 'Contagem:', contador, 'Média:', soma/contador)
