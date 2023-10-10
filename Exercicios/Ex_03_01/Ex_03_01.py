#Exercise 1: Rewrite your pay computation to give the employee 1.5
#...times the hourly rate for hours worked above 40 hours.

sv = input('Informe o valor recebido por hora: ')
sh = input('Informe o tempo de trabalho: ')
xv = float(sv)
xh = float(sh)

if xh > 40:
    print('Fez hora extra, receberá a mais!')
    pagnormal = xv * 40
    pagextra = (xh - 40) * (xv * 1.5)
    total = pagnormal + pagextra

else:
    print('Trabalhou conforme solicitado, receberá a quantia normal.')
    total = xv * xh

print('Pagamento: ', total)