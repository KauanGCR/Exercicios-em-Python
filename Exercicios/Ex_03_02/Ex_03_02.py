# Exercise 2: Rewrite your pay program using try and except so that your
# ...program handles non-numeric input gracefully by printing a message
# ...and exiting the program.

sv = input('Informe o valor recebido por hora: ')
sh = input('Informe o tempo de trabalho: ')

try:
    xv = float(sv)
    xh = float(sh)

except:
    print('Erro! Por favor insira apenas números')
    quit()

print('Valor:', sv, 'Horas:', sh)

if xh > 40:
    print('Fez hora extra, receberá a mais!')
    pagnormal = xv * 40
    pagextra = (xh - 40) * (xv * 1.5)
    total = pagnormal + pagextra

else:
    print('Trabalhou conforme solicitado, receberá a quantia normal.')
    total = xv * xh

print('Pagamento: ', total)
