#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:04:34 2020

@author: brianf

Binary Trees
"""

import math
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
        self.parent = None
        
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
        
    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def num_nodes(self):
        return len(self.preorder_traverse(self.root))
    
    def is_balanced(self, node):
        'Balanced if for every node, a subtree\'s height does not differ by more than 1'
        if not node:
            return True
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        if (abs(right_height - left_height) <= 1
               and self.is_balanced(node.left)
               and self.is_balanced(node.right)):
            return True
        return False
    
class MaxHeapNodes(BinaryTree):
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return node
        
        if self.root.value >= node.value:
            # Normal insert.
            node.parent = self.root
            if not self.root.left:
                self.root.left = node
            elif not self.root.right:
                self.root.right = node
            return node
        # Swap the nodes.
        old_root = self.root
        node.left = old_root.left
        node.right = old_root.right
        self.root = node
        
        if not self.root.left:
            self.root.left = old_root
        elif not self.root.right:
            self.root.right = old_root
        return node
    
class MaxHeapIndex:
    def __init__(self):
        self.nodes = []
        
    def insert(self, value):
        self.nodes.append(value)
        index = len(self.nodes) - 1
        parent_index = math.floor((index-1)/2)
        parent_value = self.nodes[parent_index]
        
        while index > 0 and value > parent_value:
            self.nodes[parent_index], self.nodes[index] = value, parent_value
            index = parent_index
            parent_index = math.floor((index-1)/2)
            parent_value = self.nodes[parent_index]
        return self.nodes
    
    def insert_multiple(self, elements):
        for element in elements:
            self.insert(element)
    
    def max(self):
        return self.nodes[0]
    
    def pop(self):
        root = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        index = 0
        left_child_idx = 2*index + 1
        right_child_idx = 2*index + 2
        
        while max(left_child_idx, right_child_idx) < len(self.nodes) - 1:
            swap_index = left_child_idx
            if self.nodes[left_child_idx] < self.nodes[right_child_idx]:
                swap_index = right_child_idx
                
            if self.nodes[swap_index] < self.nodes[index]:
                return root
            
            self.nodes[swap_index], self.nodes[index] = self.nodes[index], self.nodes[swap_index]
            index = swap_index
            left_child_idx = 2*index + 1
            right_child_idx = 2*index + 2
        return root
    
    def top_n_elements(self, n):
        return [self.pop() for _ in range(n)]
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

print(tree.height(tree.root))               # 3
print(tree.height(tree.root.left.right))    # 1
print(tree.height(tree.root.right.right))   # 0
print(tree.num_nodes())                     # 10

print(tree.is_balanced(tree.root))          # True