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
    s1 , s2 = i.split('|')
    s1 = s1[0:-1]
    s2 = s2[0:-1]
    return (s1, s2)

def sufixo(i):
    s1 , s2 = i.split('|')
    s1 = s1[1:]
    s2 = s2[1:]
    return (s1, s2)

def geraAdjLista(composicao):
    rotulo = {}
    grafo = {}
    saida = {}
    entrada = {}
    for x in composicao['sequencia']:
        rotulo[prefixo(x)] = x
        grafo[prefixo(x)] = []
        saida[prefixo(x)] = 0
        saida[sufixo(x)] = 0
        entrada[sufixo(x)] = 0
        entrada[prefixo(x)] = 0
    for x in composicao['sequencia']:
        grafo[prefixo(x)].append(sufixo(x))
        saida[prefixo(x)] += 1
        entrada[sufixo(x)] += 1
    return [grafo,saida,entrada, rotulo]

def encontraInicio(entrada, saida):
    mim = 0
    chave = list(entrada)[0]
    for i in (entrada):
        if entrada[i] - saida[i] <= mim:
            mim = entrada[i] - saida[i]
            chave = i
    return chave

def acha_caminho(grafo, entrada, saida, chave):
    caminho = []
    pilha = []
    while True:
        if len(pilha) == 0 and saida[chave] == 0:
            caminho.append(chave)
            break
        else:
            if saida[chave] == 0:
                caminho.append(chave)
                chave = pilha.pop()
            else:
                pilha.append(chave)
                viz = grafo[chave].pop()
                saida[chave] +=-1
                entrada[viz] +=-1
                chave = viz
    return caminho[::-1]

def remonta(d, caminho, rotulo):
    sequencia = ""
    for i in caminho:
        if sequencia == "":
            sequencia += rotulo[i].split("")
        else:
            sequencia += i[0][0]
    
    return sequencia + caminho[-1][0][1:] + caminho[-k][0][:k] + caminho[-k][1][:k] + caminho[-1][1]


composicao = abrirArquivo()
grafo, saida, entrada, rotulo = geraAdjLista(composicao)
chave_inicio = encontraInicio(entrada, saida)
#print(chave_inicio)
cami = acha_caminho(grafo, entrada, saida, chave_inicio)
print(cami)
sequencia = remonta(composicao['d'],cami, rotulo)
print(sequencia)
#for g in grafo:
#    print(g['adj'])
#gerasequencia(inicio,"")
#novo_grafo = deepcopy(grafo)
#seq = geraCaminho(novo_grafo, inicio)
#print(grafo)
#print(saida)
#print(entrada)
#print(inicio)


#print(cami)
#se = remonta(cami, composicao['d'])
#print(se)




"""

for g in grafo:
    print(g['ant'])
"""