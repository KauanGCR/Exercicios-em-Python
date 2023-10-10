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
        di[w] = di.get(w, 0) + 1

# print(di)

# encontrar a palavra mais recorrente

largest = -1
theword = None

for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k #pegar/lembrar a palavra(key) mais recorrente

print('A palavra mais recorrente é:', theword, ', aparecendo', largest, 'vezes.')