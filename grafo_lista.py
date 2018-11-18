from collections import defaultdict
from collections import deque
import os


class Grafo(object):

    def __init__(self, arestas, direcionado=False):
        self._grafo = defaultdict(set)
        self._direcionado = direcionado
        self.adiciona_arestas(arestas)


    def busca_profundidade(self, u):
        """Realiza uma busca em profundiade e apresenta sua floresta predecessor"""
        core = defaultdict(set)
        father = defaultdict(set)
        final = defaultdict(int)
        des = defaultdict(int)

        for x in list(self._grafo.keys()):      # Adiciona informações a todos os vertices
            core[x].add('B')
            father[x]
            des[x]

        time = 0
        des, father, core, final, time = self.dfs_visit(u, des, father, core, final, time)
        for x in list(self._grafo.keys()):
            if core[x] == {'B'}:
                des, father, core, final, time = self.dfs_visit(x, des, father, core, final, time)

        print('Tempo descoberto: ', des)
        print("Tempo finalizado: ", final)
        print('Vertices da floresta', father.keys())
        print('Floresta predecessor: ')
        for p in father:
            for q in father[p]:
                print(q, p)
        del core, father, des, final


    def dfs_visit(self,u,des,father,core,final,time):
        time = time + 1
        des[u] = time
        core[u] = 'G'
        for y in self._grafo[u]:
            if core[y] == {'B'}:
                father[y] = u
                des, father, core, final, time = self.dfs_visit(y, des, father, core, final, time)
        core[u] = 'P'
        time = time + 1
        final[u] = time
        return des, father, core, final, time



    def busca_largura(self, u):
        """ Realiza uma busca em largura, imprime a distancia em relação a u, imprime arvore menor caminho"""
        cor = defaultdict(set)                  #Inicia Dicionarios Cor, Distancia e Pai
        distancia = defaultdict(int)
        pai = defaultdict(set)
        arvore = defaultdict(set)

        for x in list(self._grafo.keys()):      # Adiciona informações a todos os vertices, menos a raiz indicada u
            if x == u:
                continue
            cor[x].add('B')
            distancia[x] = 0
            pai[x]

        cor[u].add('G')                         # Adiciona informações da raiz u
        distancia[u] = 0
        pai[u]
        fila = deque()
        fila.append(u)

        while fila:                             #Caso esteja vazia, retorna False
            v = fila.popleft()
            for y in self._grafo[v]:
                if cor[y] == {'B'}:
                    cor[y] = 'G'
                    distancia[y] = distancia[v] + 1
                    pai[y] = v
                    fila.append(y)
            cor[v] = 'P'

        for y in pai:                           #Monta um dicionario da arvore primeiro na extensão
            for x in pai[y]:                    #Arvore de menor caminho entre U e qualquer vertice
                if x == set():
                    continue
                arvore[x].add(y)

        print('Distancia do nodo', u, ':', distancia)
        print('NODO / PAI:', pai)
        print('Arvore em primeira extensão: ', arvore)
        return


    def get_vertices(self):
        """ Retorna vértices do grafo """
        return list(self._grafo.keys())


    def del_vertice(self, u):
        """Deleta vertice e remove conexões"""
        del self._grafo[u]
        for k in self._grafo:
            self._grafo[k].discard(u)


    def del_aresta(self,u,k):
        """Remove aresta entre u - k """
        self._grafo[u].discard(k)


    def get_arestas(self):
        """ Retorna arestas do grafo """
        return [(k, v) for k in self._grafo.keys() for v in self._grafo[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo """
        for u, v in arestas:
            self.adiciona(u, v)


    def adiciona(self, u, v):
        """ Adiciona uma aresta entre u e v """
        self._grafo[u].add(v)
        self._grafo[v]
        if not self._direcionado:
            self._grafo[v].add(u)


    def adiciona_vertice(self, u):
        """ Add um vertice """
        self._grafo[u]


    def conectado(self, u, v):
        """ Verifica se existe uma aresta entre u e v """
        return u in self._grafo and v in self._grafo[u]


    def fonte(self, u):
        """ Verifica se é uma Fonte: Retorna True/False """
        count = 0
        for x in self._grafo:
            for y in self._grafo[x]:
                if(y == u):
                    count+=1
        if(count == 0):
            return True
        else:
            return False


    def sumidouro(self,u):
        """ Verifica se existe alguma aresta de saida no vertice u """
        if (len(self._grafo[u])== 0):
            return True
        else:
            return False


    def grau_entrada(self,u):
        """ Verifica Todas as aparições de u """
        count = 0
        for x in self._grafo:
            for y in self._grafo[x]:
                if (y == u):
                    count += 1
        return count


    def grau_saida(self,u):
        """ Retorna o numero de elementos na saida de u """
        return (len(self._grafo[u]))


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._grafo))


#lista de arestas.
arestas = [('A', 'B'), ('B', 'C'), ('D', 'C'), ('A', 'D'), ('C', 'E')]

# Grafo
grafo = Grafo(arestas, direcionado=True)

m = True
while (m == True):
    print("1:imprimir ")
    print("2:adicionar vertice ")
    print("3:remover vertice ")
    print("4:visualizar vertices ")
    print("5:adicionar aresta ")
    print("6:remover aresta ")
    print("7:visualizar arestas ")
    print("8:fonte ")
    print("9:sumidouro ")
    print("10:grau entrada ")
    print("11:grau saida ")
    print("12:Busca em largura ")
    print("13:Busca em profundidade ")
    print("14:sair \n \n")

    u = input('Digite sua opção: ')
    if u == '':
        os.system('cls');
        continue
    u = int(u)


    if (u ==1):
        os.system('cls');
        print(grafo._grafo)  # Imprimir grafo
        input('pressione enter para continuar')
        os.system('cls');

    elif(u ==2):
        os.system('cls');
        u = input('Digite o vertice a adicionar: ')
        Grafo.adiciona_vertice(grafo,u) #Adiciona vertice P
        os.system('cls');

    elif(u ==3):
        os.system('cls');
        x = input('Digite o vertice a deletar: ')
        Grafo.del_vertice(grafo, x)  # Deleta vertice x
        os.system('cls');

    elif (u ==4):
        os.system('cls');
        print(Grafo.get_vertices(grafo))  # Imprimi arestas'''
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==5):
        os.system('cls');
        x = input('Digite a 1 aresta: ')
        y = input('Digite a 2 aresta: ')
        Grafo.adiciona(grafo, x, y)  # Adiciona aresta entre u e v
        os.system('cls');

    elif (u ==6):
        os.system('cls');
        x = input('Digite a 1 aresta: ')
        y = input('Digite a 2 aresta: ')
        Grafo.del_aresta(grafo, x, y) #Deleta aresta entre U x V
        os.system('cls');

    elif (u ==7):
        os.system('cls');
        print(Grafo.get_arestas(grafo)) #Imprime as arestas
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==8):
        os.system('cls');
        x = input('Fonte: Qual o vertices?')
        print(Grafo.fonte(grafo, x))  # Verifica se A é fonte
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==9):
        os.system('cls');
        x = input('Sumidouro: Qual o vertices?')
        print(Grafo.sumidouro(grafo, x))  # Verifica se é sumidouro
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==10):
        os.system('cls');
        x = input('Grau de entrada: Qual o vertice?')
        print(Grafo.grau_entrada(grafo, x))  # Verifica e imprime o grau de entrada
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==11):
        os.system('cls');
        x = input('Grau de saida: Qual o vertice?')
        print(Grafo.grau_saida(grafo, x))  # Verifica e imprime o grau de saida
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==12):
        os.system('cls');
        x = input('Busca em largura: Qual o vertice?')
        Grafo.busca_largura(grafo,x)  # Realiza uma busca em largura
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==13):
        os.system('cls');
        x = input('Busca em profundidade: Qual o vertice?')
        Grafo.busca_profundidade(grafo,x)  # Realiza uma busca em profundidade
        input('pressione enter para continuar')
        os.system('cls');

    elif (u ==14):
        m = False
