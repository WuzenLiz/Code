import sys
from collections import defaultdict
import requests
from bfs import Queue, bfs, getPath

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    __slots__ = ('name', 'neighbours')
    def __str__(self):
        result = self.name + ' : '
        for n in self.neighbours:
            result += n.name + ', '
        return result[:-1]


def buildWordGraph():
    dict_url='https://raw.githubusercontent.com/lorenbrichter/Words/master/Words/en.txt'
    dict_file=requests.get(dict_url)
    w = {}
    open('\words.txt', 'wb').write(dict_file.content)
    f = open('words.txt')
    words = f.read().split('\n')
    for word in words:
        for i in range(len(word)):
            wcard = word[:i] + '*' + word[i + 1:]
            if wcard in w:
                w[wcard].append(word)
            else:
                w[wcard] = [word]
    for key in w:
        wordlist = w[key]
        for w1 in wordlist:
            for w2 in wordlist:
                if w1 != w2:
                    inputGraph(w1, w2)


def inputGraph(word1, word2):
    if word1 not in Graph:
        node = Node(word1)
        node.neighbours.append(Node(word2))
        Graph[word1] = node
    else:
        neighbours = Graph[word1].neighbours
        if word2 not in [x.name for x in neighbours]:
            neighbours.append(Node(word2))
    if word2 not in Graph:
        node = Node(word2)
        node.neighbours.append(Node(word1))
        Graph[word2] = node
    else:
        neighbours = Graph[word2].neighbours
        if word1 not in [x.name for x in neighbours]:
            neighbours.append(Node(word1))

if __name__ == '__main__':
    dem=0
    Graph = {}
    buildWordGraph() 
    word1 = str(input("Nhap xau can chuyen: "))
    word2 = str(input("Nhap xau ket qua: "))
    if len(sys.argv) > 1:
        word1=sys.argv[1]
        word2=sys.argv[2]
    if word1 in Graph:
        start = Graph[word1]
        if word2 in Graph:
            finish=Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors) 
            str = ''
            for p in path:
                str += p + ' -> '
                dem+=1
            print ("Mat %d buoc de chuyen doi" % dem)
            print (str[:-3])
            
        else:
             print(word2,"khong ton tai tron tu dien!") 
    else:
        print(word1,"khong ton tai trong tu dien!")
