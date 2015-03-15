""" Route calculations """
import dbclient
    
def graph_region_jumps():
    """ Returns a graph of jumps between regions
        Graph format:
        `
         {
          'r1': ['r2', 'r3'],
          'r2': ['r1', 'r3', 'r4'],
          'r3': ['r1', 'r2'],
          'r4': ['r2']
          ...
         }
        `
    """
    rj_graph = {}
    for jump in dbclient.list_region_jumps():
        print "from " + str(jump[0]) + " to " + str(jump[1])
        if jump[0] not in rj_graph:
            print "adding from: " + str(jump[0])
            rj_graph[jump[0]] = []
        
        print "adding to: " + str(jump[1])
        rj_graph[jump[0]].append(jump[1])

    return rj_graph

def shortest_region_routes(start_name, finish_name):
    """ Returns a list of shortest routes between two regions
        Each route is a list of region names
        If start and finish match, [start, finish] is returned
    """
    if start == finish: return [start, finish]
    

def shortest_routes(start, finish):
    """ Returns a list of shortest routes between two systems
        Each route is a list of system names
        If start and finish match, [start, finish] is returned
    """
    if start == finish: return [start, finish]
    
    

         
