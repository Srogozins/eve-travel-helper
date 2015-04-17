"""Route calculations """
import networkx as nx
from .dbclient import api as universe


class Singleton(type):
    """Singleton metaclass boilerplate """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            superclass = super(Singleton, cls)
            cls._instances[cls] = superclass.__call__(*args, **kwargs)
        return cls._instances[cls]


class JumpGraphProvider():
    """ This class is intended to provide necessary graphs while avoiding
    unnecessary calls to DB.

    The graph attributes are hidden behind @property methods and load data
    DB when retrieved for the first time.

    Attributes:
        region_jump_graph (networkx.Graph): Graph of jump connections
            between regions.
        constellation_jump_graph (networkx.Graph): Graph of jump connections
            between constellations.
        system_jump_graph (networkx.Graph): Graph of jump connections
            between systems.

    """
    __metaclass__ = Singleton

    def __init__(self):
        self._rjg = None
        self._cjg = None
        self._sjg = None

    def _graph_region_jumps(self):
        """ Returns an undirected graph with nodes representing Regions and
        edges representing jumps between them
        """
        RJG = nx.Graph()
        for rj in universe.list_region_jumps():
            RJG.add_edge(rj.fromID, rj.toID)

        return RJG

    def _graph_constellation_jumps(self):
        """ Returns an undirected graph with nodes representing constellations
        and edges representing jumps between them
        """
        CJG = nx.Graph()
        for cj in universe.list_constellation_jumps():
            CJG.add_edge(cj.fromID, cj.toID)

        return CJG

    def _graph_system_jumps(self):
        """ Returns an undirected graph with nodes representing solar systems
        and edges representing jumps between them
        """
        SJG = nx.Graph()
        for sj in universe.list_system_jumps():
            SJG.add_edge(sj.fromID, sj.toID)

        return SJG

    @property
    def region_jump_graph(self):
        if self._rjg is None:
            self._rjg = self._graph_region_jumps()

        return self._rjg

    @property
    def constellation_jump_graph(self):
        if self._cjg is None:
            self._cjg = self._graph_constellation_jumps()

        return self._cjg

    @property
    def system_jump_graph(self):
        if self._sjg is None:
            self._sjg = self._graph_system_jumps()

        return self._sjg
