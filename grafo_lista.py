from collections import defaultdict
import os
import time


class Grafo(object):

    def __init__(self, arestas, direcionado=False):
        self._grafo = defaultdict(set)
        self._direcionado = direcionado
        self.adiciona_arestas(arestas)


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
        self._grafo[k].discard(u)

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
arestas = [('A', 'B'), ('B', 'C'), ('A', 'C')]

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
    print("12:sair \n \n")
    u = int(input('Digite sua opção: '))

    if (u ==1):
        os.system('cls');
        print(grafo._grafo)  # Imprimir grafo
        time.sleep(3)
        os.system('cls');

    elif(u ==2):
        os.system('cls');
        u = input('Digite o vertice a adicionar: ')
        Grafo.adiciona_vertice(grafo,u) #Adiciona vertice P
        time.sleep(3)
        os.system('cls');

    elif(u ==3):
        os.system('cls');
        u = input('Digite o vertice a deletar: ')
        Grafo.del_vertice(grafo, u)  # Deleta u
        time.sleep(3)
        os.system('cls');

    elif (u ==4):
        os.system('cls');
        print(Grafo.get_vertices(grafo))  # Imprimi arestas'''
        time.sleep(3)
        os.system('cls');

    elif (u ==5):
        os.system('cls');
        x = input('Digite a 1 aresta: ')
        y = input('Digite a 2 aresta: ')
        Grafo.adiciona(grafo, x, y)  # Adiciona aresta entre u e v
        time.sleep(3)
        os.system('cls');

    elif (u ==6):
        os.system('cls');
        x = input('Digite a 1 aresta: ')
        y = input('Digite a 2 aresta: ')
        Grafo.del_aresta(grafo, x, y) #Deleta aresta entre U x V
        time.sleep(3)
        os.system('cls');

    elif (u ==7):
        os.system('cls');
        print(Grafo.get_arestas(grafo)) #Imprime as arestas
        time.sleep(3)
        os.system('cls');

    elif (u ==8):
        os.system('cls');
        x = input('Fonte: qual o vertices?')
        print(Grafo.fonte(grafo, x))  # Verifica se A é fonte
        time.sleep(3)
        os.system('cls');

    elif (u ==9):
        os.system('cls');
        x = input('Sumidouro: qual o vertices?')
        print(Grafo.sumidouro(grafo, x))  # Verifica se é sumidouro
        time.sleep(3)
        os.system('cls');

    elif (u ==10):
        os.system('cls');
        x = input('Grau de entrada: qual o vertice?')
        print(Grafo.grau_entrada(grafo, x))  # Verifica e imprime o grau de entrada
        time.sleep(3)
        os.system('cls');

    elif (u ==11):
        os.system('cls');
        x = input('Grau de saida: qual o vertice?')
        print(Grafo.grau_saida(grafo, x))  # Verifica e imprime o grau de saida
        time.sleep(3)
        os.system('cls');

    elif (u ==12):
        m = False
