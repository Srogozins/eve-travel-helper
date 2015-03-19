""" Route calculations """


from dbclient import api as universe


def graph_region_jumps():
    """Returns a graph of jumps between regions, represented as
    a dict of `from` region IDs mapped to lists of `to` region IDs
    Example output:
    `{10000001: [10000011, 10000012, 10000028,
                 10000030, 10000036, 10000047],
      10000002: [10000003, 10000016, 10000027,
                 10000029, 10000032, 10000033,
                 10000042],
      10000003: [10000002, 10000010, 10000029,i
                 10000034],
      ...
     }`

    """
    rj_graph = {}
    for rj in universe.list_region_jumps():
        if rj.fromID not in rj_graph:
            rj_graph[rj.fromID] = []

        rj_graph[rj.fromID].append(rj.toID)

    return rj_graph


def shortest_region_routes(start_name, finish_name):
    """ Returns a list of shortest routes between two regions
        Each route is a list of region names
        If start and finish match, [start, finish] is returned
    """
    if start_name == finish_name:
        return [start_name, finish_name]


def shortest_routes(start, finish):
    """ Returns a list of shortest routes between two systems
        Each route is a list of system names
        If start and finish match, [start, finish] is returned
    """
    if start == finish:
        return [start, finish]
