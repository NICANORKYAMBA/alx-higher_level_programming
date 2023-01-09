#!/usr/bin/python3
"""defines class that inherits from list"""


class MyList(list):
    """implements inheritance and printing of list"""

    def print_sorted(self):
        """returns sorted list in ascending order"""
        print(sorted(self))
