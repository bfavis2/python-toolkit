#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:07:05 2020

@author: brianf

Directed Acyclic Graph (DAG)
"""
from collections import deque

class DAG():
    def __init__(self):
        self.graph = {}
    
    def add(self, node, to=None):
        if node not in self.graph:
            self.graph[node] = []
        if to:
            self.graph[node].append(to)
            if to not in self.graph:
                self.graph[to] = []
        # Validity check to make sure DAG remains acyclical
        # if len(self.sort()) > len(self.graph):
        #     raise('Exception')

    def in_degrees(self):
        'Returns the number of in-degrees for each node'
        self.degrees = {}
        for k in self.graph.keys():
            self.degrees[k] = 0
        for v in self.graph.values():
            for node in v:
                self.degrees[node] += 1
        return self.degrees
                
    def sort(self):
        '''
        Returns a list of the nodes ordered by ascending in-degrees
        Uses Kahn's Algorithm for a topological sort
        '''
        self.in_degrees()
        to_visit = deque()
        for node in self.graph:
            if self.degrees[node] == 0:
                to_visit.append(node)
        
        searched = []
        while to_visit:
            node = to_visit.popleft()
            for pointer in self.graph[node]:
                self.degrees[pointer] -= 1
                if self.degrees[pointer] == 0:
                    to_visit.append(pointer)
            searched.append(node)
        return searched