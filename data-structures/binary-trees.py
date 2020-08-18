#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:04:34 2020

@author: brianf

Binary Trees
"""
# from stack import Stack
# from queue import Queue

class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[0].value
        
    def __len__(self):
        return len(self.items)

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
        
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __repr__(self):
        return "<Node: {}>".format(self.value)
        
class BinaryTree():
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)
            
    def insert(self, values, index=0):
        'Level order insert'
        node = None
        if index < len(values):
            node = Node(values[index])
            if not self.root:
                self.root = node
            node.left = self.insert(values, index=index*2+1)
            node.right = self.insert(values, index=index*2+2)
        return node
            
    def is_parent(self, node):
        return bool(node.left or node.right)
    
    def is_interior(self, node):
        return (not node == self.root) and self.is_parent(node)
    
    def is_leaf(self, node):
        return (not node == self.root) and not self.is_interior(node)
        
    def print_tree(self, traversal_method):
        if traversal_method == 'preorder':
            return self.preorder_traverse(self.root)
        elif traversal_method == 'inorder':
            return self.inorder_traverse(self.root)
        elif traversal_method == 'postorder':
            return self.postorder_traverse(self.root)
        elif traversal_method == 'levelorder':
            return self.levelorder_traverse(self.root)
        elif traversal_method == 'reverseorder':
            return self.reverse_levelorder_traverse(self.root)
        else:
            print(f'{traversal_method} is not supported')
            
    def preorder_traverse(self, node):
        'root -> left -> right'
        if not node:
            return []
        return (
            [node.value] +
            self.preorder_traverse(node.left) +
            self.preorder_traverse(node.right)
        )
    
    def inorder_traverse(self, node):
        'left -> root -> right'
        if not node:
            return []
        return (
            self.inorder_traverse(node.left) +
            [node.value] +
            self.inorder_traverse(node.right)
        )
    
    def postorder_traverse(self, node):
        'left -> right -> root'
        if not node:
            return []
        return (
            self.postorder_traverse(node.left) +
            self.postorder_traverse(node.right) +
            [node.value]
        )
    
    def levelorder_traverse(self, node):
        'level by level, left to right'
        if not node:
            return
        queue = Queue()
        queue.enqueue(node)
        traversal = []
        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_traverse(self, node):
        if not node:
            return
        stack = Stack()
        queue = Queue()
        queue.enqueue(node)
        traversal = []
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

            
        while len(stack) > 0:
            node = stack.pop()
            traversal.append(node.value)
        return traversal
        
#%% Testing
#             1
#        2        3
#     4     5  6     7
#    8 9  10
tree = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

root_parent = tree.is_parent(tree.root)     # True
parent = tree.is_parent(tree.root.left)     # True
interior = tree.is_interior(tree.root.left) # True
root_leaf = tree.is_leaf(tree.root)         # False
leaf = tree.is_leaf(tree.root.left.left)    # False

print(tree.print_tree('preorder'))          # 1-2-4-8-9-5-10-3-6-7
print(tree.print_tree('inorder'))           # 8-4-9-2-10-5-1-6-3-7
print(tree.print_tree('postorder'))         # 8-9-4-10-5-2-6-7-3-1
print(tree.print_tree('levelorder'))        # 1-2-3-4-5-6-7-8-9-10
print(tree.print_tree('reverseorder'))      # 8-9-10-4-5-6-7-2-3-1    