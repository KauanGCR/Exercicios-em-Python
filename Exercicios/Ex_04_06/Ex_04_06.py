# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called
# ...computepay which takes two parameters (hours and rate).

def computar(valor, horas):
    print('Computando:', valor, horas)
    if horas > 40:
        print('Fez hora extra, receberá a mais!')
        pagnormal = valor * 40
        pagextra = (horas - 40) * (valor * 1.5)
        total = pagnormal + pagextra

    else:
        print('Trabalhou conforme solicitado, receberá a quantia normal.')
        total = valor * horas

    return total


sv = input('Informe o valor recebido por hora: ')
sh = input('Informe o tempo de trabalho: ')
xv = float(sv)
xh = float(sh)

pagamento = computar(xv, xh)

print('Pagamento: ', pagamento)
