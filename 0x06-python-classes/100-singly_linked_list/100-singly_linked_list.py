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
        if not isinstance(value, Node) and value is not None:
            return TypeError("next_node must be a Node object")
        self.__next_node = value

"""
A SinglyLinkeList class
"""


class SinglyLinkedList:
    """ A class that defines a singly linked list """
    def __init__(self):
        """ Initialize the class attribute """
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.date < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
