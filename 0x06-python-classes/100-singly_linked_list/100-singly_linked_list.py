#!/usr/bin/python3
""" 100-singly_linked_list.py """


class Node:
    """
    A class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Initializes class attributes """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ gets the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ sets the data """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ gets the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next node """
        if is not isinstance(next_node, Node):
            return TypeError("next_node must be a Node object")
        self.__next_node = value
