#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:44:18 2020

@author: brianf

Queue Data Structue: First in - First out
"""

class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self, item):
        if not self.is_empty():
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[0].value
        
    def __len__(self):
        return len(self.items)
