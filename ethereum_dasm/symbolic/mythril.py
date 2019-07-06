#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
from mythril.analysis.symbolic import SymExecWrapper
from mythril.ethereum.evmcontract import EVMContract

from collections import defaultdict


class DiGraph(object):

    def __init__(self):
        self._graph = defaultdict(list)
        self._conditions = {}
        self._first_added = None

    @property
    def nodes(self):
        """ returns the vertices of a graph """
        return list(self._graph.keys())

    @property
    def edges(self):
        """ returns the edges of a graph """
        edges = []
        for vertex, neighbours in self._graph.items():
            for neighbour in neighbours:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_node(self, vertex):
        if not self._first_added:
            self._first_added = vertex  # remember first vertex
        self._graph[vertex] = []

    def add_edge(self, frm, to, condition):
        if not self._first_added:
            self._first_added = frm  # remember first vertex

        self._graph[frm].append(to)
        self._conditions[(frm, to)] = condition

    def iterate_graph(self, start=None):
        start = start or self._first_added

        yield start
        # {start:[vertex1,vertex2,...]
        for vertex in self._graph[start]:
            for v in self.iterate_graph(vertex):
                yield v

    def __repr__(self):
        return "<%s nodes:%d edges:%d>" %(self.__class__.__name__,
                                          len(self.nodes),
                                          len(self.edges))

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self._graph
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def find_path(self, start_vertex, end_vertex, _path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        _path = _path or []
        graph = self._graph
        _path = _path + [start_vertex]
        if start_vertex == end_vertex:
            return _path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in _path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               _path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, _path=None):
        """ find all paths from start_vertex to
            end_vertex in graph """
        _path = _path or []
        graph = self._graph
        _path = _path + [start_vertex]
        if start_vertex == end_vertex or (
                not end_vertex and not graph[start_vertex]):  # start_vertex == [] <-- no more vertices
            return [_path]
        if start_vertex not in graph:
            return []
        paths = []

        for vertex in graph[start_vertex]:
            if vertex not in _path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     _path)
                for p in extended_paths:
                    paths.append(p)
        return paths


class MythrilSymExecGraph(DiGraph):

    def __init__(self):
        super().__init__()

    def get_block_and_state_by_address(self, address, prn_cmp=None):
        if not prn_cmp:
            prn_cmp = lambda x, y: x == y

        # find all basicblocks that contain instructions from a specific address
        for n in self.nodes:
            for s in n.states:
                instr = s.get_current_instruction()
                if prn_cmp(instr["address"], address):
                    yield n, s
                    break

    def get_block_and_state_by_instruction_name(self, name, prn_cmp=None):
        """

        # find all pushes
        print(list(s.get_current_instruction() for b,s in graph.get_block_and_state_by_instruction_name("PUSH",prn_cmp=lambda x,y:x.startswith(y))))

        :param name:
        :param prn_cmp:
        :return:
        """
        if not prn_cmp:
            prn_cmp = lambda x, y: x == y

        # find all basicblocks that contain instructions from a specific address
        for n in self.nodes:
            for s in n.states:
                instr = s.get_current_instruction()
                if prn_cmp(instr["opcode"], name):
                    yield n, s
                    break

    def get_block_by_uid(self, uid):
        return next(b for b in self.nodes if b.uid == uid)

    def get_streams(self, start=None):
        """
        Get all possible paths/forks/execution streams from starting block end of execution

            Example:
                for stream in graph.get_streams(graph.get_basicblock_by_uid(0)):
                    print([s.uid for s in stream])

                [0, 1]
                [0, 2, 3, 33, 35, 36, 38]
                [0, 2, 3, 33, 35, 37]
                [0, 2, 3, 34]
                [0, 2, 4, 5, 29, 31, 32]
                [0, 2, 4, 5, 30]
                [0, 2, 4, 6, 7, 25, 27, 28]
                [0, 2, 4, 6, 7, 26]
                [0, 2, 4, 6, 8, 9, 11, 13, 14, 16, 18, 20, 21, 23]
                [0, 2, 4, 6, 8, 9, 11, 13, 14, 16, 18, 20, 21, 24]
                [0, 2, 4, 6, 8, 9, 11, 13, 14, 16, 18, 20, 22]
                [0, 2, 4, 6, 8, 9, 11, 13, 14, 16, 19]
                [0, 2, 4, 6, 8, 9, 11, 13, 14, 17]
                [0, 2, 4, 6, 8, 9, 11, 13, 15]
                [0, 2, 4, 6, 8, 9, 12]
                [0, 2, 4, 6, 8, 10]


        :param start:
        :return:
        """
        start = start or self.get_block_by_uid(0)
        return self.find_all_paths(start_vertex=start, end_vertex=None)

    def get_stream_by_block(self, block, start=None):
        start = start or self.get_block_by_uid(0)

        all_streams = self.get_streams(start=start)

        result_streams = []

        for s in all_streams:
            if block in s:
                result_streams.append(s)
                continue
        return result_streams

    def iterate_blocks(self, start):
        start = start or self.get_block_by_uid(0)

        return self.iterate_graph(start=start)

    def iterate_blocks_and_states(self):
        for node in self.nodes:
            for state in node.states:
                yield node, state


def symbolic_execute(code, address):
    contract = EVMContract(code)
    sym = SymExecWrapper(contract=contract, address=address, strategy="dfs")

    # populate graph object
    graph = MythrilSymExecGraph()
    for n in sym.nodes.values():
        # g.add all nodes - just in case one is not connected which should not happen
        graph.add_node(n)

    for e in sym.edges:
        graph.add_edge(sym.nodes[e.node_from], sym.nodes[e.node_to], e)

    """
    print(graph.iterate_graph())
    print(sorted([x.uid for x in graph.nodes]))
    print(graph._first_added.uid)
    print(next(graph.get_basicblocks_by_address(0)))
    print(graph.get_basicblock_by_uid(0))
    print(list(n.uid for n in graph.iterate_graph(graph.get_basicblock_by_uid(0))))

    print(graph.find_all_paths(graph.get_basicblock_by_uid(0), graph.get_basicblock_by_uid(37)))
    print(graph.find_all_paths(graph.get_basicblock_by_uid(0),None))
    print("streams")
    for stream in graph.get_streams(graph.get_basicblock_by_uid(0)):
        print([s.uid for s in stream])
    
    print(list(s.get_current_instruction() for b,s in graph.get_block_and_state_by_instruction_name("PUSH",prn_cmp=lambda x,y:x.startswith(y))))

    print(graph.get_stream_by_block(block=graph.get_block_by_uid(2)))
    """
    # only work on the graph from now
    return graph
