class Grafo:
    def __init__(self, vertices = []):
        self.vertices = vertices
        self.nvertices = len(vertices)
        self.narestas = 0

    def AdicionaNo(self, letra):
        novo_no = No(letra)
        self.vertices.append(novo_no)

    def AdicionaAresta(self, no1, no2):
        no1.vizinhos.append(no2)
        no2.vizinhos.append(no1)

    def AtualizaDesc(self):
        self.nvertices = len(self.vertices)

    def __str__(self):
        imp = ''
        for i in self.vertices:
            imp = imp + str(i)+'\n'
        return (imp)
class No:
    def __init__(self, letra):
        self.letra = letra
        self.vizinhos = []
        self.cor = 'branco'
        self.pai = None
        self.desc = 0

    def EleMesmo(self, outro):
        return self.letra == outro.letra

    def __str__(self):
        imp = str(self.letra)+': ['
        for i in self.vizinhos:
            if i == self.vizinhos[0]:
                 imp = imp + str(i.letra)
            else:
                 imp = imp +', '+str(i.letra)
        imp = imp + "]"
        return imp

def CriaAresta(E):
    v = []
    i = 0
    while (i < E):
        aresta = input('Insira a aresta: ')
        if(len(aresta) != 2):
            print('Uma aresta deve conter 2 vertices, talvez você tenha digitado errado.')
        else:
            i = i + 1
            aresta = aresta.lower()
            v.append(aresta)
    return v

def CriaMatriz(V):
    M = []
    for i in range(0,V):
        M.append(0)
        M[i] = []
        for j in range(0,V):
            M[i].append(0)
    return M

def MatrizAdjacencias(v, M):    
    for aresta in v:
        v1 = ord(aresta[0]) - 97
        v2 = ord(aresta[1]) - 97
        if(v1 != v2):
            M[v1][v2] = 1
            M[v2][v1] = 1
    return M
    
def PrintMatriz(V, M):
    String = ''
    for i in range(0,V):
        for j in range(0,V):
            if j == 0:
                String = String + str(M[i][j])
            else:
                String = String + ' '+str(M[i][j])
        if i != V-1:
            String = String + '\n'
    return String

def NumVertices(v):
    j = 0
    for i in v:
        if max(ord(i[0]) - 96, ord(i[1]) - 96)  > j:
            j = max(ord(i[0]) - 96, ord(i[1]) - 96)
    return j

def MatrizParaGrafo(M):
    grafo = Grafo([])
    for i in range(len(M)):
        grafo.AdicionaNo(chr(i+97))
    for i in range(len(M)):
        for j in range(len(M)):
            if j > i:
                if M[i][j] == 1 and not grafo.vertices[i].EleMesmo(grafo.vertices[j]):
                    grafo.AdicionaAresta(grafo.vertices[i], grafo.vertices[j])
                    grafo.narestas = grafo.narestas + 1
    return grafo

def BFS(Grafo):
    inf = Grafo.nvertices + 1
    Q = []
    for v in Grafo.vertices:
        v.desc = inf
    for v in Grafo.vertices:
        if v.cor == 'branco':
            v.cor = 'cinza'
            v.desc = 0
            Q.append(v)
        while (Q != []):
            u = Q.pop()
            for w in u.vizinhos:
                if (w.cor == 'branco'):
                    w.cor = 'cinza'
                    w.pai = u
                    w.desc = u.desc + 1
                    Q.append(w)
            u.cor = 'preto'
    V1 = []
    V2 = []
    for v in Grafo.vertices:
        if v.desc % 2 == 0:
            V2.append(v)
        else:
            V1.append(v)
    V = [V1, V2]
    return V

def printBFS(V):
    #---Necessário rodar BFS antes---#
    print ('V[1] = [', end='')
    for v in V[0]:
        if v == V[0][0]:
            print (v.letra, end='')
        else:
            print (', '+v.letra, end='')
    print (']')
    print ('V[2] = [', end='')
    for v in V[1]:
        if v == V[1][0]:
            print (v.letra, end='')
        else:
            print (', '+v.letra, end='')
    print (']')

def ChecaBipartido(V):
    #---Necessário rodar BFS antes---#
    for v1 in V[0]:
        for v2 in V[0]:
            if v1 in v2.vizinhos:
                return False
    for v1 in V[1]:
        for v2 in V[1]:
            if v1 in v2.vizinhos:
                return False
    return True

def CriaMatrizKn(n):
    M = CriaMatriz(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 0
            else:
                M[i][j] = 1
    return M

def CriaMatrizPn(n):
    M = CriaMatriz(n)
    for i in range(n):
        for j in range(n):
            if i == j + 1:
                M[i][j] = 1
                M[j][i] = 1
            elif i == j - 1 and (M[i][j] != 1 or M[j][i] != 1):
                M[i][j] = 1
                M[j][i] = 1
            else:
                M[i][j] = 0
    return M

def CriaMatrizCn(n):
    M = CriaMatriz(n)
    for i in range(n):
        for j in range(n):
            if i == j + 1:
                M[i][j] = 1
                M[j][i] = 1
            elif i == j - 1 and (M[i][j] != 1 or M[j][i] != 1):
                M[i][j] = 1
                M[j][i] = 1
            else:
                M[i][j] = 0
    M[0][n-1] = 1
    M[n-1][0] = 1
    return M

def CriaMatrizWn(n):
    M = CriaMatrizCn(n-1)
    for i in range(n-1):
        M[i].append(1)
    M.append([])
    for i in range(n):
        if i == n-1:
            M[n-1].append(0)
        else:
            M[n-1].append(1)
    return M

def CriaMatrizKnm(n, m):
    M = CriaMatriz(n+m)
    a = max(n, m)
    b = min(n, m)
    for i in range(a):
        for j in range(a, a+b):
            M[i][j] = 1
            M[j][i] = 1
    return M

def CriaMatrizIdn(n):
    M = CriaMatriz(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 1
    return M

def CriaMatrizQn(n):
    if n == 1:
        M = CriaMatrizKn(2)
    else:
        M2 = CriaMatrizIdn(2**n)
        M = CriaMatriz(2**n)
        M1 = CriaMatrizQn(n-1)
        
        m = 2**n
        for i in range(int((2**n)/2)):
            for j in range(int((2**n)/2)):
                M[i][j] = M1[i][j]
                M[(2**n)-i-1][(2**n)-j-1] = M1[i][j]
        for i in range(int((2**n)/2)):
            for j in range(int((2**n)/2)):
                M[int((2**n)/2) + i][j] = M2[i][j]
                M[i][int((2**n)/2) + j] = M2[i][j]
    return M

def ColoracaoGuloso(Grafo):
    n = 0
    for vertice in Grafo.vertices:
        if len(vertice.vizinhos) > n:
            n = len(vertice.vizinhos)
    n = n + 1
    return n

def Mycielski(m, n):
    if n == 1:
        M = CriaMatrizKn(m)
        return M
    elif n >= 2:
        M2 = Mycielski(n-1)
        M = CriaMatriz(2*len(M2)+1)
        M1 = CriaMatrizCn(len(M2))
        for i in range(len(M2)):
            for j in range(len(M2)):
                M[i][j] = M2[i][j]
        for i in range(len(M2), 2*len(M2)):
            for j in range(len(M2), 2*len(M2)):
                pass
        for i in range(len(M2), 2*len(M2)):
            M[i][2*len(M2)] = 1
            M[2*len(M2)][i] = 1
        for i in range(len(M2)):
            for j in range(len(M2)):
                M[len(M2) + i][j] = M1[i][j]
                M[i][j + len(M2)] = M1[i][j]
                
        return M

def CriaArvore(Grafo, M):
    Grafo.AtualizaDesc()
    n = Grafo.nvertices
    C = []
    M2 = CriaMatriz(n)
    for i in range(n):
        C.append(i)
    for i in range(n):
        if C[i] == 0:
            for j in range(n):
                if C[j] != 0 and M[i][j] == 1:
                    M2[i][j] = 1
                    M2[j][i] = 1
                    C[j] = 0
    return M2

def CriaArvore2(Grafo, M):
    Grafo.AtualizaDesc()
    n = Grafo.nvertices
    v =[]
    cont = 1
    ar = CriaMatriz(n)
    for i in range(n):
        v.append(0)
    while cont < n:
        for i in range(n):
            for j in range(i+1, n):
                if(M[i][j] == 1 and v[j] != 1):
                    v[i] = 1
                    ar[i][j] = 1
                    ar[j][i] = 1
                    cont = cont + 1
                    break
    return ar




    
