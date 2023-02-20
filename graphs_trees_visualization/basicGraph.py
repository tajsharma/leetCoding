class Graph:
    #imeplementation of a graph using pythong dictionaries
    def __init__(self, graphDict = None): 
        if graphDict is None:            
            graphDict = {}
        self.graphDict = graphDict       #if it already has values, it leaves it 

    def addEdge(self,vertex,edge):
        self.graphDict[vertex].append(edge)


customDict = {
    "a": ["b","c"],
    "b": ["a","d","e"],
    "c": ["a","e"],
    "d": ["b","e","f"],
    "e": ["b","d","f"],
    "f": ["d","e"]
}

my = Graph(customDict)
