#******* create vertex with heuristic values *****#
def add_vertex(v,h):
    global vertices
    global noOfVertices
    global huresticValue 
    global graph
    if v in vertices:
        print("The vertex "+str(v)+" is already exist")
    else:
        vertices.append(v)
        noOfVertices=noOfVertices+1
        huresticValue.append(0)
        huresticValue[v]=h
        #print("a new vertex added")
        for vertex in graph:
            vertex.append(0)
        empty = []
        for i in range(noOfVertices):
            empty.append(0)
        graph.append(empty)

#******** Defining edge value *******#
def add_edge(v1,v2,e):
    global vertices
    global noOfVertices
    global graph
    if v1 not in vertices or v2 not in vertices:
        print("Invalid vertex !!")
    else:
        graph[v1][v2]= e  
        #print("new edge added") 

def print_graph():
    global graph
    global noOfVertices

    for i in range(noOfVertices):
        for j in range(noOfVertices):
            print(str(graph[i][j])+ " ")
        print("\n")

def aStarAlgo(startV,endV):
    global distance
    global graph
    global short_path
    short_distVertex = 0
    short_dist = 0
    distanceAdj = []
    distanceTot = []
    total_dist = 0
    for i in range(noOfVertices):
        distanceAdj.append(MAX_VAL)
        distanceTot.append(MAX_VAL)
    curVer=startV
    while(curVer!=endV):
        short_path.put(curVer)
        for i in range(noOfVertices):
            distanceAdj[i] = MAX_VAL
        for i in range(noOfVertices):
            if(graph[curVer][i]!=0):
                distanceAdj[i] = graph[curVer][i] + huresticValue[i]
        short_dist = min(distanceAdj)
        short_distVertex = distanceAdj.index(short_dist)    
        curVer = short_distVertex
        total_dist = total_dist + short_dist
    short_path.put(endV)

    print("The shortest distance is :"+str(total_dist))
    print("The path is:")
    while(short_path.empty()==False):
        print(str(short_path.get()))    

from queue import Queue
MAX_VAL = 100000 # initialize infinity
graph = []
vertices = []
huresticValue = []
noOfVertices = 0
short_path = Queue(maxsize=100)


#*******Define graph here*******#
add_vertex(0,5)    
add_vertex(1,3)
add_vertex(2,8)
add_vertex(3,1)
#add_vertex(1,7)

add_edge(1,2,4)
add_edge(0,1,3)
add_edge(0,2,5)
add_edge(2,1,2)
add_edge(1,3,1)
add_edge(3,2,1)
print_graph()
aStarAlgo(0,2)


