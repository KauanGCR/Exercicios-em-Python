fname = input('Insira o nome do arquivo: ')

if len(fname) < 1:
    fname = 'clown.txt'

hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: recuperar/criar/atualizar o contador de palavras
        di[w] = di.get(w,0) + 1

# print(di)

# encontrar as 5 palavra mais recorrentes

tmp = list()

for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

# print('Invertido:', tmp)
tmp = sorted(tmp, reverse=True)
#print('Classificado:', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)