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
            x (int, optional): [x coordinates of new rectangle]. Defaults to 0.
            y (int, optional): [y coordinates of new rectangle]. Defaults to 0.
            id ([int], optional): [identity of new rectangle]. Defaults to None.
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
        self.__width = value

    @property
    def height(self):
        """returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value for height"""
        self.__height = value
        
    @property
    def x(self):
        """returns x value"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets the new value for x"""
        self.__x = value
        
    @property
    def y(self):
        """returns y value"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """sets the new value for y"""
        self.__y = value
