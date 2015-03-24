""" Route calculations """
import networkx as nx
from dbclient import api as universe


class Singleton(type):
    """ Singleton metaclass boilerplate """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            superclass = super(Singleton, cls)
            cls._instances[cls] = superclass.__call__(*args, **kwargs)
        return cls._instances[cls]


class JumpGraphProvider():
    """ This class is intended to provide necessary graphs while avoiding
    unnecessary calls to DB.
    """
    __metaclass__ = Singleton

    def __init__(self):
        self._rjg = None

    def _graph_region_jumps(self):
        """ Returns an undirected graph with nodes representing Regions and
        edges representing jumps between them
        """
        RJG = nx.Graph()
        for rj in universe.list_region_jumps():
            RJG.add_edge(rj.fromID, rj.toID)

        return RJG

    @property
    def region_jump_graph(self):
        if self._rjg is None:
            self._rjg = self._graph_region_jumps()

        return self._rjg
