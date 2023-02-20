class Graph:
    #implementation of a graph using pythong dictionaries
    def __init__(self, graphDict = None): 
        if graphDict is None:            
            graphDict = {}
        self.graphDict = graphDict   #if it already has values, it leaves it 

    def addEdge(self,start_vertex,goal_vertex): #draws/creates an edge between provided vertices
        if start_vertex not in self.graphDict.keys() and goal_vertex not in self.graphDict.keys(): #checks if both are vertices in the graph
            self.graphDict[start_vertex].append(goal_vertex)
            self.graphDict[goal_vertex].append(start_vertex)
            return True
        return False     

    def addVertex(self,vertex):
        if vertex not in self.graphDict.keys():#check if its already in the graph looking at the key names
            self.graphDict[vertex] = []
            return True #if added
        return False #if not added to the graph

    def bfs(self,start_vertex):
        visited = [start_vertex]                                     
        queue = [start_vertex]                                       
        while queue:#while queue is not empty 
            dq_vertex = queue.pop(0)
            print(dq_vertex)                                         
            for adj_vertex in self.graphDict[dq_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    queue.append(adj_vertex)

    def dfs(self,start_vertex):
        pass

customDict = {
    "a": ["b","c"],
    "b": ["a","d","e"],
    "c": ["a","e"],
    "d": ["b","e","f"],
    "e": ["b","d","f"],
    "f": ["d","e"]
}

myGraph = Graph(customDict)
myGraph.addEdge("e","a")
print(myGraph.graphDict)
myGraph.addVertex("k")
print(myGraph.graphDict)
myGraph.addEdge("e","k")
print(myGraph.graphDict)