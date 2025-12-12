#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Implementation of a singly linked list using recursion.

This module defines:
- A Node class to store data and a pointer to the next node
- A LinkedList class that supports insertion, recursive sum,
  recursive search, and recursive reverse operations
"""


class Node:
    """
    Represents a single node in a linked list.
    Each node stores data and a reference to the next node.
    """

    def __init__(self, data):
        # Store the provided data in the node
        self.data = data

        # Initialize next as None since the node
        # is not yet connected to another node
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects.
    Several operations are implemented using recursion.
    """

    def __init__(self):
        # Head points to the first node in the list
        # An empty list has head set to None
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        # Create a new node with the provided data
        new_node = Node(data)

        # Point the new node to the current head
        new_node.next = self.head

        # Update head to the new node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        # Create the new node
        new_node = Node(data)

        # If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Traverse the list until the last node
        current = self.head
        while current.next:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

    def recursive_sum(self):
        """
        Recursively calculate the sum of all node data.
        """

        def helper(node):
            # Base case: if we've reached the end of the list
            if node is None:
                return 0

            # Recursive case: current node's data
            # plus the sum of the remaining list
            return node.data + helper(node.next)

        # Start recursion from the head
        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        """

        def helper(prev, current):
            # Base case: once current is None,
            # prev is the new head of the reversed list
            if current is None:
                return prev

            # Save the next node before changing pointers
            next_node = current.next

            # Reverse the link
            current.next = prev

            # Recurse with updated pointers
            return helper(current, next_node)

        # Update head to the new head returned by helper
        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        Recursively search for a target value in the list.
        Returns True if found, otherwise False.
        """

        def helper(node):
            # Base case: reached end of list without finding target
            if node is None:
                return False

            # If current node matches the target, return True
            if node.data == target:
                return True

            # Otherwise, continue searching the rest of the list
            return helper(node.next)

        # Start recursion from the head
        return helper(self.head)

    def display(self):
        """
        Print the contents of the list in order for debugging.
        """
        values = []
        current = self.head

        # Traverse the list and collect node data
        while current:
            values.append(str(current.data))
            current = current.next

        # Display list in readable format
        print(" -> ".join(values) + " -> None")
