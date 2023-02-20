class Graph:
    #implementation of a graph using pythong dictionaries
    def __init__(self, graphDict = None): 
        if graphDict is None:            
            graphDict = {}
        self.graphDict = graphDict   #if it already has values, it leaves it 

    def addEdge(self,start_vertex,goal_vertex): #draws/creates an edge between provided vertices
        self.graphDict[start_vertex].append(goal_vertex)


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
print(myGraph.graphDict["e"])