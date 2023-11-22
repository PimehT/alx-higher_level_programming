#!/usr/bin/python3
""" Defining a class """


class Node:
    """ class Node """

    def __init__(self, data, next_node=None):
        """
        Initializes the node with data and sets next to None.
        Args:
        data (int): integer data to store in node
        next_node (Node): reference to next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieve data """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set data to new value
        Args:
        value (int): new value to set
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set next node to new value
        Args:
        value (Node): new node to set
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" defining a new class """


class SinglyLinkedList:
    """ Singly linked list class """

    def __init__(self):
        """ initialize the singly linked class """
        self.__head = None

    def sorted_insert(self, value):
        """ Insert new value into a sorted linked list
        Args:
        value (int): value to insert
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """ Enabling list to be printed one node data per line """
        result = []
        current_node = self.__head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)
