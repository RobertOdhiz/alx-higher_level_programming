#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, nxt=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            nxt (Node): The next node of the new Node.
        """
        self.data = data
        self.nxt = nxt

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def nxt(self):
        """Get/set the nxt of the Node."""
        return (self.__nxt)

    @nxt.setter
    def nxt(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("nxt must be a Node object")
        self.__nxt = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.nxt = None
            self.__head = new
        elif self.__head.data > value:
            new.nxt = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.nxt is not None and
                    tmp.nxt.data < value):
                tmp = tmp.nxt
            new.nxt = tmp.nxt
            tmp.nxt = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.nxt
        return ('\n'.join(values))
