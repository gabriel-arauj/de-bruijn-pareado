import sys

# Abrindo arquivo kdmer
def abrirArquivo():
    try:
        caminho = sys.argv[1]
    except:
        print("Passe o arquivo como arguemento na chamada do programa!" )
        exit()
    try:
        f = open(caminho, 'r')
    except:
        print("Arquivo não encontrado!!")
        exit()
    k, d= caminho.split("d")
    k = int(k.split('k')[1])
    d = int(d.split("mer.txt")[0])
    x = f.read()
    ls = x.strip('][').replace('\'', "").replace(" ", "").split(',')
    return {'k':k,'d':d,'sequencia':ls}


def prefixo(i):
    s1 , s2 = i['rotulo'].split('|')
    s1 = s1[0:-1]
    s2 = s2[0:-1]
    return (s1, s2)

def sufixo(i):
    s1 , s2 = i['rotulo'].split('|')
    s1 = s1[1:]
    s2 = s2[1:]
    return (s1, s2)


def geraAdjLista(composicao):
    grafo = []
    for x in composicao['sequencia']:
        grafo.append({'rotulo':x, 'adjlist':[], 'ant':[]})
    tam = len(grafo)
    ini = []
    for i in range(tam):
        for j in range(tam):
            if j==i:
                continue 
            if prefixo(grafo[j]) == sufixo(grafo[i]):
                grafo[i]['adjlist'].append(j)
            if prefixo(grafo[i]) == sufixo(grafo[j]):
                grafo[i]['ant'].append(j)
    return grafo

def gerasequencia(i, sequencia):
    ini = grafo[i]['rotulo'].split('|')[0]
    if sequencia == "":
        sequencia += ini
    else:
        sequencia += ini[-1]
    adjlist = grafo[i]['adjlist']
    if adjlist != []:
        for prox in adjlist:
            gerasequencia(prox, sequencia)
    else:
        sequencia += grafo[i]['rotulo'].split('|')[1]
        print(sequencia)

def encontraInicio(grafo):
    tam = len(grafo)
    inicio = -1
    for i in range(tam):
        if grafo[i]['ant'] == []:
            inicio = i
    return inicio

def geraCaminho(grafo, inicio):
    pass
composicao = abrirArquivo()
grafo = geraAdjLista(composicao)
inicio = encontraInicio(grafo)
gerasequencia(inicio,"")



"""
print(grafo)
for g in grafo:
    print(g['ant'])
"""