#!/usr/bin/python3
"""Defines class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of Square

        Args:
            size ([int]): [new size of the square]
            x (int, optional): [x coordinates of square]. Defaults to 0.
            y (int, optional): [y coordinates of square]. Defaults to 0.
            id ([int], optional): [identity of the square]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return '[square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y,
                                                 self.height)
