#!/usr/bin/python3
"""
Module defines a singly linked list
"""

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self, head):
        self.__head = head
    
    def sorted_insert(self, value):
        pass
