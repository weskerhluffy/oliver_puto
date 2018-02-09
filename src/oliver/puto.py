'''
Created on 09/02/2018

@author: 

XXX: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/
'''

import logging
from collections import namedtuple
from sys import stdin

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

class nodo():
    def __init__(self, idx, tv, tc):
        self.idx = idx
        self.tiempo_visto = tv
        self.tiempo_consumido = tc
    def __repr__(self):
        return "{}:{}:{}".format(self.idx, self.tiempo_visto, self.tiempo_consumido)
consulta = namedtuple("consulta", "tipo x y")

def oliver_puto_topocaca(nodos, lista_adjacencia):
    ya_vistos = set()
    pila_caca = []
    nodo_act = nodos[1]
    pila_caca.append(nodo_act)
    ya_vistos.add(nodo_act)
    tiempo = 0
    
    while pila_caca:
        nodo_act = pila_caca.pop()
        if(nodo_act.tiempo_visto == -1):
            nodo_act.tiempo_visto = tiempo
            pila_caca.append(nodo_act)
            for vecino in lista_adjacencia[nodo_act.idx]:
                if(vecino not in ya_vistos):
                    pila_caca.append(vecino)
                    ya_vistos.add(vecino)
        else:
            nodo_act.tiempo_consumido = tiempo
        tiempo += 1

def oliver_puto_core(nodos, lista_adjacencia, queries):
    oliver_puto_topocaca(nodos, lista_adjacencia)
    resultados = []
    for consulta in queries:
        padre = None
        hijo = None
        if consulta.tipo:
            padre = nodos[consulta.y]
            hijo = nodos[consulta.x]
        else:
            padre = nodos[consulta.x]
            hijo = nodos[consulta.y]
        assert padre.idx != hijo.idx or (padre.tiempo_visto == hijo.tiempo_visto and padre.tiempo_consumido == hijo.tiempo_consumido), "padre {} hijo {}".format(padre, hijo)
        resultado = padre.tiempo_visto <= hijo.tiempo_visto and padre.tiempo_consumido >= hijo.tiempo_consumido
        resultados.append(resultado)
    return resultados
        
def caca_comun_lee_linea_como_num():
    return int(stdin.readline().strip())

def caca_comun_lee_linea_como_monton_de_numeros():
    return list(map(int, stdin.readline().strip().split(" ")))

def oliver_puto_main():
    nodos_tam = caca_comun_lee_linea_como_num()
    nodos = []
    consultas = []
    lista_adjacencia = []
    for idx in range(nodos_tam + 1):
        nodo_nuevo = nodo(idx, -1, -1)
        nodos.append(nodo_nuevo)
        lista_adjacencia.append([])
    for _ in range(nodos_tam - 1):
        a, b = caca_comun_lee_linea_como_monton_de_numeros()
        lista_adjacencia[a].append(nodos[b])
        lista_adjacencia[b].append(nodos[a])
    consultas_tam = caca_comun_lee_linea_como_num()
    for _ in range(consultas_tam):
        consulta_nueva = consulta(*caca_comun_lee_linea_como_monton_de_numeros())
        consultas.append(consulta_nueva)
#    logger_cagada.debug("lso ndos {} consultas {}".format(nodos, consultas))
    res = oliver_puto_core(nodos, lista_adjacencia, consultas)
#    logger_cagada.debug("el res {}".format(res))
    for resu in res:
        if resu:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        oliver_puto_main()
