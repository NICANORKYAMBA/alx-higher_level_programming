#!/usr/bin/python3
"""writes a class that defines a rectangle with
    private instance attributes width and height

Raises:
    TypeError: both height and width must be integers
    ValueError: both height and width must be >= 0

Returns:
    values of height and width(new and original)
    rectangle area and perimeter
"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a rectangle

        args:
            width(int): new value of width. Defaults to 0.
            height(int): new value of height. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """returns area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__height == 0 and self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
