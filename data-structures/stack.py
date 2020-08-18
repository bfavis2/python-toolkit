#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:42:22 2020

@author: brianf

Stack Data Structure: Last in - First out
"""

class Stack():
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def push(self, item):
        'Add an item to the top of the stack'
        self.items.append(item)
        
    def pop(self):
        'Return the top of the stack'
        return self.items.pop()
    
    def get_stack(self):
        'Returns the whole stack'
        return self.items
    
    def is_empty(self):
        'Bool to check if stack is empty'
        return self.items == []
        
    def peek(self):
        'Look at the top the stack'
        if not self.it_empty():
            return self.items[-1]