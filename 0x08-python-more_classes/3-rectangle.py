#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """A class Rectangle that defines a rectangle based on 0-rectangle.py"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle.
        Args:
            height(int)
            width(int)
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.__height)

    def __str__(self):
        new_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += "#"
                new_str += "\n"
            return new_str[:-1]
