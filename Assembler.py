import sys
from copy import deepcopy


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
        grafo.append({'rotulo':x, 'adj':[], 'ant':[], 'saida':0, 'entrada':0})
    tam = len(grafo)
    ini = []
    for i in range(tam):
        for j in range(tam):
            if j==i:
                continue 
            if prefixo(grafo[j]) == sufixo(grafo[i]):
                grafo[i]['adj'].append(j)
                grafo[i]['saida'] += 1
            if prefixo(grafo[i]) == sufixo(grafo[j]):
                grafo[i]['ant'].append(j)
                grafo[i]['entrada'] += 1
    return grafo

def encontraInicio(grafo):
    tam = len(grafo)
    inicio = -1
    for i in range(tam):
        if grafo[i]['ant'] == []:
            inicio = i
    return inicio

def remonta(s, d):
    tam = len(s)
    se = ""
    for i in range(tam):
        ini = grafo[s[i]]['rotulo'].split('|')[0]
        fin = grafo[s[i]]['rotulo'].split('|')[1]
        if se == "":
            se += ini
        else:
            se += ini[-1]
        if i==tam-1:
            se += grafo[s[i-d]]['rotulo'].split('|')[1][:d]
            se += fin
    return se


def gerasequencia(i, sequencia):
    ini = grafo[i]['rotulo'].split('|')[0]
    if sequencia == "":
        sequencia += ini
    else:
        sequencia += ini[-1]
    adjlist = grafo[i]['adj']
    if adjlist != []:
        for prox in adjlist:
            gerasequencia(prox, sequencia)
    else:
        sequencia += grafo[i]['rotulo'].split('|')[1]
        print(sequencia)

def geraCaminho(grafo, inicio):
    if inicio == -1:
        inicio = grafo[inicio]['adj'].pop()
    if grafo[inicio]['adj'] == []:
        return [inicio]
    return [inicio]+geraCaminho(grafo, grafo[inicio]['adj'].pop())

def acha_caminho(grafo, v):
    caminho = []
    pilha = []
    if v == -1:
        v = 0
    while True:
        print("pi",pilha)
        print("cam",caminho)
        saida = grafo[v]['saida']
        if len(pilha) == 0 and saida == 0:
            caminho = [v] + caminho
            break
        else:
            if saida == 0:
                caminho = [v] + caminho
                v = pilha.pop()
            else:
                pilha.append(v)
                grafo[v]['saida'] = -1
                v = grafo[v]['adj'].pop()
                grafo[v]['entrada'] = -1
            
    return caminho

    

composicao = abrirArquivo()
grafo = geraAdjLista(composicao)
inicio = encontraInicio(grafo)
for g in grafo:
    print(g['adj'])
#gerasequencia(inicio,"")
#novo_grafo = deepcopy(grafo)
#seq = geraCaminho(novo_grafo, inicio)
print(grafo)
print(inicio)

cami = acha_caminho(grafo, inicio)
print(cami)
se = remonta(cami, composicao['d'])
print(se)




"""

for g in grafo:
    print(g['ant'])
"""