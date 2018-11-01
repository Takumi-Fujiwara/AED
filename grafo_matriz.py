import os
import time
import numpy as np

def get_vertices (matriz):
    for x in range(len(matriz)):
        print(x)
    return


def del_vertices (matriz, u):
    matriz = np.delete(matriz, np.s_[u-1:u:], 1)
    matriz = np.delete(matriz, u, 0)
    return matriz


def add_vertices(matriz):
    matriz = np.hstack((matriz, [[0]] * len(matriz)))  # Função para adicionar 0 no final de cada vetor
    matriz = np.vstack((matriz, [0] * len(matriz[0])))  # Função para adicionar um novo vetor com 0
    return matriz


def get_arestas (matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if(matriz[x, y]==1):
                print('Aresta: {}-{} \n'.format(x,y))


def del_arestas (matriz, u,v):
    matriz[u,v] = 0
    return


def add_arestas(matriz, u, v):
    matriz[u, v] = 1
    return


def fonte (matriz, u):
    for x in matriz[u]:
        if(x ==1):
            return False
    return True


def sumidouro (matriz, u):
    for x in range(len(matriz)):
        if(matriz[x,u] == 1):
            return False
    return True


def grau_entrada(matriz, u):
    count = 0
    for x in range(len(matriz)):
        if matriz[x,u] == 1:
            count += 1
    return count


def grau_saida (matriz, u):
    count = 0
    for x in matriz[u]:
        if(x == 1):
            count += 1
    return count


def imprimir (matriz):
    print(matriz)
    return


matriz = np.array([[0]])

x = True
while ( x == True):
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
        imprimir(matriz)
        time.sleep(2)
        os.system('cls');

    elif(u ==2):
        os.system('cls');
        matriz = add_vertices(matriz)
        time.sleep(2)
        os.system('cls');

    elif(u ==3):
        os.system('cls');
        v = int(input('Digite vertice: '))
        matriz = del_vertices(matriz,v)
        time.sleep(2)
        os.system('cls');
    elif (u ==4):
        os.system('cls');
        get_vertices(matriz)
        time.sleep(2)
        os.system('cls');

    elif (u ==5):
        os.system('cls');
        u = int(input('Digite o 1 vertice: '))
        v = int(input('Digite o 2 vertice: '))
        add_arestas(matriz,u,v)
        time.sleep(2)
        os.system('cls');

    elif (u ==6):
        os.system('cls');
        u = int(input('Digite o 1 vertice: '))
        v = int(input('Digite o 2 vertice: '))
        del_arestas(matriz,u,v)
        time.sleep(2)
        os.system('cls');

    elif (u ==7):
        os.system('cls');
        get_arestas(matriz)
        time.sleep(2)
        os.system('cls');

    elif (u ==8):
        os.system('cls');
        u = int(input('Digite o vertice: '))
        print(fonte(matriz, u))
        time.sleep(2)
        os.system('cls');

    elif (u ==9):
        os.system('cls');
        u = int(input('Digite o 1 vertice: '))
        print(sumidouro(matriz, u))
        time.sleep(2)
        os.system('cls');

    elif (u ==10):
        os.system('cls');
        u = int(input('Digite o 1 vertice: '))
        print(grau_entrada(matriz, u))
        time.sleep(2)
        os.system('cls');

    elif (u ==11):
        os.system('cls');
        u = int(input('Digite o 1 vertice: '))
        print(grau_saida(matriz, u))
        time.sleep(2)
        os.system('cls');

    elif (u ==12):
        x = False
