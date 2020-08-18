#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:04:34 2020

@author: brianf

Binary Trees
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

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_method):
        if traversal_method == 'preorder':
            return self.preorder_traversal(self.root, '')
        elif traversal_method == 'inorder':
            return self.inorder_traversal(self.root, '')
        elif traversal_method == 'postorder':
            return self.postorder_traversal(self.root, '')
        elif traversal_method == 'levelorder':
            return self.levelorder_traversal(self.root)
        else:
            print(f'{traversal_method} is not supported')
            
    def preorder_traversal(self, start, traversal):
        'Checks Root -> Left Subtree -> Right Subtree'
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal[:-1]
    
    def inorder_traversal(self, start, traversal):
        'Checks Left Subtree -> Root -> Right Subtree'
        if start:
            traversal = self.preorder_traversal(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal[:-1]

    def postorder_traversal(self, start, traversal):
        'Checks Left Subtree -> Right Subtree -> Root'
        if start:
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal[:-1]
    
    def levelorder_traversal(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    