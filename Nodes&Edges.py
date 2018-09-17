import random

class Node(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        """assume src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self,src,dest,weight=1.0):
        self.src=src
        self.dest=dest
        self.weight=weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName()+'->('+str(self.weight)+')'+self.dest.getName()

class Digraph(object):
    """Digraph = Directed graph, the edges are unidirectional. the relationships
       between nodes should be parent nodes(sources) and child nodes(destinations)"""
    #nodes is a list of nodes in the graph
    #edges is a dictionary mapping each node to a list of its children
    def __init__(self):
        self.nodes=[]
        self.edges={}
    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('Duplicated node')
        else:
            self.nodes.append(node)
            self.edges[node]=[];
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName()+'->'+dest.getName()+'\n'
        return result[:-1] #omit the final new line

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)

def test1(kind):
        nodes =[]
        for name in range(10):
            nodes.append(Node(str(name)))
        g=kind()
        for n in nodes:
            g.addNode(n)
        g.addEdge(Edge(nodes[0],nodes[1]))
        g.addEdge(Edge(nodes[1],nodes[2]))
        g.addEdge(Edge(nodes[2],nodes[3]))
        g.addEdge(Edge(nodes[3],nodes[4]))
        g.addEdge(Edge(nodes[3],nodes[5]))
        g.addEdge(Edge(nodes[0],nodes[2]))
        g.addEdge(Edge(nodes[1],nodes[1]))
        g.addEdge(Edge(nodes[1],nodes[0]))
        g.addEdge(Edge(nodes[4],nodes[0]))
        print('The graph:')
        print(g)

#test1(Digraph)
#test1(Graph)

numCalls =0



def printPath(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i!=len(path)-1:
            result = result+'->'
    return result

def shortestPath(graph,start,end,toPrint,visited):
    
    global numCalls 
    numCalls+=1
    if toPrint:
        print(start,end)
    if not(graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph')
    path =[str(start)]
    
    if start==end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if(str(node) not in visited): #avoid cycle
            visited = visited +[str(node)] #new list
            #print(printPath(visited))
            newPath = shortestPath(graph,node,end,toPrint,visited)
            if (newPath==None):
                continue
            if (shortest ==None or len(newPath) < len(shortest)):
                shortest = newPath
    if (shortest !=None):
        path+=shortest
    else:
        path = None
    
    return path


def test2(kind,toPrint=False):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g=kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print ('The graph:')
    print (g)
    start = nodes[0]
    end = nodes[4]
    shortest = shortestPath(g, start, end, toPrint,[start])
    print ('The shortest path:')
    print (shortest)

#test2(Graph)
#test2(Digraph)

def bigTest1(kind,numNodes=25,numEdges=200,toPrint=False):
    nodes =[]
    for name in range(numNodes):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    for n in nodes:
        src = nodes[random.choice(range(0,len(nodes)))]
        des = nodes[random.choice(range(0,len(nodes)))]
        g.addEdge(Edge(src,des))
    print(g)
    start = nodes[0]
    end = nodes[4]
    shortest = shortestPath(g,start,end,toPrint,[start])
    print ('The shortest path:')
    print (shortest)

#bigTest1(Digraph)



##def dpShortestPath(graph,start,end,visited = [],memo ={}):
##    global numCalls
##    numCalls += 1
##    print(memo)
##    if not (graph.hasNode(start) and graph.hasNode(end)):
##        raise ValueError('Start or end not in graph')
##    path = [str(start)]
##    if start ==end:
##        return path
##    shortest = None
##    for node in graph.childrenOf(start):
##        if (str(node) not in visited):
##            print(visited)
##            visited= visited+[str(node)]
##            try:
##                newPath = memo[node,end]
##            
##                print('Key = ')
##                print(node,end)
##                print(newPath)
##            except:
##                newPath = dpShortestPath(graph, node, end,
##                                         visited, memo)
##            if newPath == None:
##                continue
##            if (shortest == None or len(newPath) < len(shortest)):
##                print('shortest = ',shortest)
##                shortest = newPath
##                memo[node, end] = newPath
##                for key in memo.keys():
##                    for item in key:
##                        print(item)
##                print('value = ',memo[node,end])
##                
##    if shortest != None:
##        path = path + shortest
##    else:
##        path = None
##    return path

def dpShortestPath(graph,start,end,visited=[],memo={}):
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or End not in graoh')
    path = [str(start)]
    if (start == end):
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited):
            visited = visited+[str(node)]
            try:
                newPath = memo[node,end]
            except:
                newPath = dpShortestPath(graph,node,end,visited,memo)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
                memo[node,end] = newPath

    if shortest !=None:
        path = path + shortest
    else:
        path = None
    return path


def test3(kind,toPrint=False):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print ('The graph:')
    print (g)
    start = nodes[0]
    end = nodes[4]
    #shortest = shortestPath(g, start,end,toPrint,[start])
    #print ('The shortest path:')
    #print (shortest)
    shortest = dpShortestPath(g, start, end)
    print ('The dpShortest path:')
    print (shortest)

test3(Digraph)


def bigTest2(kind, numNodes = 25, numEdges = 200,toPrint=False):
    global numCalls
    nodes = []
    for name in range(numNodes):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    for e in range(numEdges):
        src = nodes[random.choice(range(0, len(nodes)))]
        dest = nodes[random.choice(range(0, len(nodes)))]
        g.addEdge(Edge(src, dest))
    print (g)
    numCalls = 0
    start = nodes[0]
    end = nodes[4]
    shortest = shortestPath(g, start,end,toPrint,[start])
    print ('Number of calls to shortest path =', numCalls)
    print (shortest)
    numCalls = 0
    shortest = dpShortestPath(g, start, end)
    print ('Number of calls to dp shortest path =', numCalls)
    print (shortest)

#bigTest2(Digraph)
