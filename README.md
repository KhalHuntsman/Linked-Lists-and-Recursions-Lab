# Recursive Linked List Lab

## Overview
This lab introduces fundamental data structures and algorithmic concepts
through the implementation of a singly linked list in Python.
The focus is on understanding node-based structures, recursion, and
analyzing time and space complexity for common operations.

---

## Project Structure

Linked-Lists-and-Recursions-Lab/

Linked-Lists-and-Recursions-Lab/linked_list.py

Linked-Lists-and-Recursions-Lab/main.py

Linked-Lists-and-Recursions-Lab/tests/

Linked-Lists-and-Recursions-Lab/tests/__init__.py

Linked-Lists-and-Recursions-Lab/tests/test_linked_list.py

Linked-Lists-and-Recursions-Lab/README.md


- linked_list.py contains the Node and LinkedList class implementations
- main.py serves as a driver file to demonstrate linked list operations
- tests/test_linked_list.py holds automated unit tests for linked list behavior
- README.md provides an overview of the lab and its functionality

## Application Overview
The linked list implementation supports the following operations:

Insert at Front
- Adds a new node to the beginning of the list.
- Updates the head pointer accordingly.

Insert at End
- Traverses the list to append a new node at the end.
- Handles insertion into an empty list.

Recursive Sum
- Uses recursion to calculate the sum of all node values.
- Returns 0 for an empty list.

Recursive Search
- Uses recursion to determine whether a target value exists in the list.
- Returns True if found, otherwise False.

Recursive Reverse
- Reverses the linked list in-place using recursion.
- Updates the head pointer to the new front of the list.

Display
- Traverses the list and prints its contents in a readable format.
- Used for debugging and verification.

## Key Concepts Covered
- Singly linked list data structures
- Node-based memory relationships
- Recursive algorithms and base cases
- Time and space complexity analysis
- In-place data structure manipulation

## Running the Tests

From the project root use the following:
- python -m unittest

## General project notes

Project passed through ChatGPT to review recursion logic, validate linked
list behavior, and assist in drafting this README.md file. The README.md
was reviewed and edited for clarity, consistency, and alignment with lab
requirements prior to submission.
