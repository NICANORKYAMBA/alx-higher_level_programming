#!/usr/bin/python3
""" writes a class that defines a square
    with a private instance attribute size
    Raises:
        TypeError: _size must be an integer_
        ValueError: _size should always be greater or equal to zero_

    Returns:
        _area_: _area of the square_
    """


class Square:
    """ represent a square """
    def __init__(self, size=0):
        """ initialize a square

        Args:
            size (int): new size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """" return size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the area of the square """
        return (self.__size * self.__size)
