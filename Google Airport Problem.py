# what are the number of connections you need to make to get from a starting airport to any other airport

airports = ["BGI","CDG","DEL","DOH","DSM","EWR","EYW","HND","ICN",
            "JFK","LGA","LHR","ORD","SAN","SFO","SIN","TLV","BUD"]

routes = [
    ["DSM","ORD"],
    ["ORD","BGI"],
    ["BGI","LGA"],
    ["SIN","CDG"],
    ["CDG","SIN"],
    ["CDG","BUD"],
    ["DEL","DOH"],
    ["DEL","CDG"],
    ["TLV","DEL"],
    ["EWR","HND"],
    ["HND","ICN"],
    ['ICN','JFK'],
    ["HND","JFK"],
    ["JFK","LGA"],
    ["EYW","LHR"],
    ["LHR","SFO"],
    ["SFO","SAN"],
    ["SFO","DSM"],
    ["SAN","EYW"]
]

startingAirport = 'LGA'

def treeify(func):
    def wrapper(node, airports, routes, hq):
        airportsDict = dict()

        for i in airports:
            airportsDict[i] = TreeNode(i)
        for i in airportsDict.keys():
            for v in routes:
                if i in v[0]:
                    if airportsDict[i].parent and airportsDict[i].parent.parent is airportsDict[v[1]].parent:
                        airportsDict[i].leaf = airportsDict[i].parent
                        airportsDict[i].parent = airportsDict[v[1]]
                    else:
                        airportsDict[i].parent = airportsDict[v[1]]
                elif (not airportsDict[i].parent) and (routes[-1] == v):
                    airportsDict[i].root = airportsDict[i]       

        
        node = airportsDict[node]
        hq = airportsDict[hq]

        return func(node, airports, routes, hq)

    return wrapper

class TreeNode:
    def __init__(self, key, root = None, parent = None, leaf = None):
        self.key = key
        self.root = root
        self.parent = parent
        self.leaf = leaf

@treeify
def numOfConnections(node, airports, routes, hq): # node is starting point
    """
    node: destination node
    hq: where all the planes are starting at
    """
    counter = 0
    next_node = node
    while True:        
        if hq is next_node:
            return counter
        elif hq.leaf is next_node:
            return counter
        elif next_node.parent:
            next_node = next_node.parent           
        elif next_node.leaf:
            next_node = next_node.leaf     
        else:
            counter += 1
            return counter
    
print(numOfConnections('DSM',airports,routes,startingAirport))