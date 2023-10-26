from grafoslib import *

print('Escolha uma das opcoes abaixo: ')
Opcoes = ['- Utilitzar um Grafo proprio (arquivo ou digitado)', '- Utilizar um Grafo pre-montado']
for i in range(len(Opcoes)):
        print (i, Opcoes[i])
Escolha1 = int(input('Insira sua escolha: '))
M = []
#-Escolha-1-----------------------------------------------------------------------------------------------------------------------------------------OK-#
if Escolha1 == 0:
    Opcoes = ['- Carregar um arquivo com as arestas','- Carregar um arquivo com a Matriz de Adjacencias', '- Digitar as arestas']
    print('Escolha uma das opcoes abaixo: ')
    for i in range(len(Opcoes)):
        print (i, Opcoes[i])
    Escolha = int(input('Insira sua escolha: '))
    ##-Escolha-1------------------------------------------------------------------------------------------------------------------------------------OK-#
    if Escolha == 0:
        nomearquivo = input('Insira o nome do arquivo: ')
        with open(nomearquivo, "r") as ins:
            v = []
            NArestas = 0
            for line in ins:
                v.append(line.lower())
                NArestas = NArestas + 1
        NVertices = NumVertices(v)
        M = CriaMatriz(NVertices)
        M = MatrizAdjacencias(v, M)
    elif Escolha == 1:
        nomearquivo = input('Insira o nome do arquivo: ')
        with open(nomearquivo, "r") as ins:
            l = [[int(num) for num in line.split(' ') if num != '\n'] for line in ins]        
        M = l
        print (M)

            
    ##-Escolha-2------------------------------------------------------------------------------------------------------------------------------------OK-#                
    elif Escolha == 2:
        NArestas = int(input('Numero de arestas: '))
        v = CriaAresta(NArestas)
        NVertices = NumVertices(v)
        M = CriaMatriz(NVertices)
        M = MatrizAdjacencias(v, M)

#-Escolha-2-----------------------------------------------------------------------------------------------------------------------------------------OK-#
elif Escolha1 == 1:
    Opcoes = ['- Qn (Cubico)', '- Kn (Completo) ou Pn (Caminho)', '- Cn (Circular) ou Wn (Roda)', '- Knn', '- Mycielski']
    print('Escolha uma das opcoes abaixo: ')
    for i in range(len(Opcoes)):
        print (i, Opcoes[i])
    Escolha = int(input('Insira sua escolha: '))
    ##-Escolha-1------------------------------------------------------------------------------------------------------------------------------------OK-#
    if Escolha == 0:
        n = int(input('Digite um N para o Qn: '))
        M = CriaMatrizQn(n)
    ##-Escolha-2------------------------------------------------------------------------------------------------------------------------------------OK-#
    elif Escolha == 1:
        Opcoes = ['- Kn (Completo)', '- Pn (Caminho)']
        print('Escolha uma das opcoes abaixo: ')
        for i in range(len(Opcoes)):
            print (i, Opcoes[i])
        Escolha2 = int(input('Insira sua escolha: '))
        ###-Escolha-1-------------------------------------------------------------------------------------------------------------------------------OK-#   
        if Escolha2 == 0:
                n = int(input('Digite um N para o Kn: '))
                M = CriaMatrizKn(n)
        ###-Escolha-2-------------------------------------------------------------------------------------------------------------------------------OK-#
        elif Escolha2 == 1:
                n = int(input('Digite um N para o Pn: '))
                M = CriaMatrizPn(n)
    ##-Escolha-2------------------------------------------------------------------------------------------------------------------------------------OK-#
    elif Escolha == 2:
        Opcoes = ['- Cn (Circular)', '- Wn (Roda)']
        print('Escolha uma das opcoes abaixo: ')
        for i in range(len(Opcoes)):
            print (i, Opcoes[i])
        Escolha2 = int(input('Insira sua escolha: '))
        ###-Escolha-1-------------------------------------------------------------------------------------------------------------------------------OK-#
        if Escolha2 == 0:
                n = int(input('Digite um N para o Cn: '))
                M = CriaMatrizCn(n)
        ###-Escolha-2-------------------------------------------------------------------------------------------------------------------------------OK-#
        elif Escolha2 == 1:
                n = int(input('Digite um N para o Wn: '))
                M = CriaMatrizWn(n)
    ##-Escolha-3------------------------------------------------------------------------------------------------------------------------------------OK-#
    elif Escolha == 3:
        n = int(input('Digite um N para o Knm: '))
        m = int(input('Digite um M para o Knm: '))
        M = CriaMatrizKnm(n, m)
    ##-Escolha-4------------------------------------------------------------------------------------------------------------------------------------OK-#
    elif Escolha == 4:
        n = int(input('Digite um N para o Mn: '))
        M = Mycielski(n)
        
        
grafo1 = MatrizParaGrafo(M)
grafo1.AtualizaDesc()                
grafo1.AtualizaDesc()    
V = BFS(grafo1)
print('Informacoes gerais sobre o grafo: ')
print('\t 1 -',grafo1.nvertices,'vertices')
print('\t 2 -',grafo1.narestas,'arestas')
print('\t 3 - Bipartido =', str(ChecaBipartido(V)))
print('\t 4 - Numero de cores =', ColoracaoGuloso(grafo1),'(Metodo Guloso)')
Escolha = input('Deseja imprimir a Matriz de Adjacencia? S/N\n')
Escolha = Escolha.upper()
if Escolha == 'S':
    print(PrintMatriz(grafo1.nvertices, M))
    with open('out.txt', 'w') as f:
        print(PrintMatriz(grafo1.nvertices, M), file=f)
if ChecaBipartido(V):
    Escolha = input('Deseja imprimir os Vetores da Biparticao? S/N\n')
    Escolha.upper()
    if Escolha == 'S':
            printBFS(V)
Escolha = input('Deseja imprimir a Matriz da Arvore Geradora? S/N\n')
if Escolha == 'S':
        MArv = CriaArvore2(grafo1, M)
        print(PrintMatriz(grafo1.nvertices, MArv))
