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
        self.__data = value
