#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Example driver file for demonstrating LinkedList functionality.

This file creates a LinkedList instance and performs insertion,
recursive sum, recursive search, and recursive reverse operations.
"""

from linked_list import LinkedList


if __name__ == "__main__":
    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)

    # 3) Display the list to verify insertion
    print("Initial list:")
    ll.display()  # Expected: 20 -> 10 -> 5

    # 4) Call recursive_sum and print the result
    total = ll.recursive_sum()
    print(f"Recursive sum: {total}")

    # 5) Call recursive_search with a target and print result
    target = 10
    found = ll.recursive_search(target)
    print(f"Search for {target}: {found}")

    # 6) Call recursive_reverse, then display the reversed list
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()  # Expected: 5 -> 10 -> 20
