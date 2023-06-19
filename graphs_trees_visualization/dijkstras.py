from basicGraph import Graph

customDict = {
    "a": ["b","c"],
    "b": ["a","d","e"],
    "c": ["a","e"],
    "d": ["b","e","f"],
    "e": ["b","d","f"],
    "f": ["d","e"]
}

g1 = Graph(customDict)
