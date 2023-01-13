#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle

        Args:
            width ([int]): [width of rectangle]
            height ([int]): [heigth of rectangle]
            x (int): [x coordinates of new rectangle]. Defaults to 0.
            y (int): [y coordinates of new rectangle]. Defaults to 0.
            id ([int]): [identity of new rectangle]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """returns x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the new value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the new value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
