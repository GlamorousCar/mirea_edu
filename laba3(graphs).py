from collections import defaultdict
import graphviz
import collections
#импорт модулей

#Реализация класса граф
class Graph():
    def __init__(self):
        self.Graph=[]
    def first(self,v):
        for node in enumerate(self.Graph):
            if node[1][0] == v:
                return f'Вершина {node[1][1]} смежная с вершиной {v}, индекс {node[0]}'
                break
        else:
            return "-1 Не ясно какой именно индекс вершины нужно вернуть"
    def next(self,v,i):
        r = 0
        for node in enumerate(self.Graph):
            if node[1][0] == v:
                r+=1
                #print(f'Вершина {node[1][1]} смежная с вершиной {v}, индекс {node[0]}, {r}')
            if i+1 == r:
                return f'Индекс вершины, смежной с вершиной {v},следующий за индексом {i}: {node[0]}'
                break
        else:
            return -1
    def vertex(self,v,i):
        for node in enumerate(self.Graph):
            if node[1][0] == v and node[0] == i:
                return f'Вершина {node[1][1]} смежная с вершиной {v}, индекс {node[0]}'
                break
        else:
            return -1
    def add_v(self,node):
        self.Graph.append((node,))
        return True
    def add_e(self,v,w):
        self.Graph.append((v,w))
        return True
    def del_v(self,v):
        dellist = []
        for node in enumerate(self.Graph):
            if len(node[1])>1 and node[1][1] == v:
                dellist.append(node[0])
            if node[1][0] == v:
                dellist.append(node[0])
        for i in dellist:
            del self.Graph[i]
        return f'Вершина {v} удалена'
    def del_e(self,v,w):
        self.Graph.remove((v,w))
        return f'Дуга {(v,w)} удалена'
    def display(self):
        for keys,values in self.Graph:
            print(keys,":=>",values)
    def algorytm(self):

    def vizialize(self):
        g = graphviz.Digraph('G', filename='project.gv', engine='sfdp')
        for node in self.Graph:
            if len(node)>1:
                asa = tuple(map(str,node))
                g.edge(*asa)
            else:
                g.node(str(node[0]))
        return g
      
     
#проанализурем работу программы на данном графе
GraphData = [(0, 1), (0, 2), (0, 7), (1, 2), (1, 3), (2, 6), (3, 4), (3, 5), (4, 5), (4, 20), (5, 6), (6, 10), (7, 8), (7, 9), (8, 9), (8, 12), (9, 10), (10, 11), (10, 12), (11, 13), (11, 14), (12, 13), (13, 15), (14, 16), (14, 20), (15, 16), (15, 17), (16, 17), (16, 18), (16, 19), (17, 18), (18, 19), (19, 20)]
#создаем экзмепляр
test = Graph()
#добавляем узлы
for i in GraphData:
    test.add_e(i[0],i[1])

#Вывод работы основных функций
print("Граф представлен ввиде списка дуг:\n",test.Graph)
print('===========')
print("Функция First")
print(test.first(0))
print('===========')
print('Функция Next')
print(test.next(1,1))
print('===========')
print('Функция Vertex')
print(test.vertex(2,4))
print('===========')
print('Функция add_v')
print(test.add_v(21))
print('===========')
print('Функция add_e')
print(test.add_e(22,7))
print('===========')
print('Функция del_v')
print(test.del_v(21))
print('===========')
print('Функция del_e')
print(test.del_e(22,7))
print('===========')
#Визуализация нашего графа
test.vizialize()

#преобразование графа
graph = {}
for row in GraphData:
    if row[0] in graph:
        graph[row[0]].append(row[1])
    else:
        graph[row[0]] = [row[1]]
for i in graph.copy():
    for j in graph[i]:
        if j not in graph:
            graph[j]=[]
print(graph)


#класс друг, в котором реализован алогритм поиска всех путей 
class Graph :
    def __init__ (self):
        self.allpaths = []
    #принимает значения: граф, начальная вершина, конечная вершина
    def FindAllPaths (self, adjlist : Dict[int, List[int]] , src : int, dst : int):
        path = []
        path.append(src)
        print("Source : " + str(src) + " Destination : " +  str(dst))

        self.DFS (adjlist, src, dst, path)


        for path in self.allpaths:
            print("Path : " + str(path))
        self.allpaths.clear()
    #алгоритм DFS
    def DFS (self, adjlist : Dict[int, List[int]], src : int, dst : int, path : List[int]):
        if (src == dst):
            self.allpaths.append(copy.deepcopy(path))
        else:
            for adjnode in adjlist[src]:
                path.append(adjnode)
                self.DFS (adjlist, adjnode, dst, path)
                path.pop()

#{0: [2, 1, 3], 1: [3, 4], 3: [4], 4:[],2:[]}


g = Graph()
g.FindAllPaths(graph, 6, 16)

#Output
#Source : 6 Destination : 16
#Path : [6, 10, 11, 13, 15, 16]
#Path : [6, 10, 11, 14, 16]
#Path : [6, 10, 12, 13, 15, 16]
