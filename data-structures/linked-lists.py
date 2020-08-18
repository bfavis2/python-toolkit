#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:50:06 2020

@author: brianf

Linked Lists
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def __getitem__(self, index):
        counter = 0
        cur_node = self.head
        while counter < index:
            cur_node = cur_node.next
            counter += 1
        return cur_node
        
    def __len__(self):
        counter = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            counter += 1
        return counter
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
        else:
            split_start = self[index - 1]
            split_end = split_start.next
            split_start.next = new_node
            new_node.next = split_end
            
    def pop(self, index):
        old_node = self[index]
        if index == 0:
            self.head = self.head.next
            return old_node
        else:
            split_start = self[index - 1]
            split_end = self[index + 1]
            split_start.next = split_end
            return old_node

class CircularLinkedList(SinglyLinkedList):
    'A singly linked list where the last node points back to the head'
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = self.head
            
    def print_list(self):
        print(self.head)
        cur_node = self.head.next
        while cur_node != self.head:
            print(cur_node)
            cur_node = cur_node.next
        
        
#%% Testing
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(0, 'head')
ll.insert(3, 'between 2 and 3')
popped = ll.pop(2)
ll.print_list()
print('*' * 20)
print(f'Length: {len(ll)}')
print(f'Popped: {popped.data}')
