#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """A class Rectangle that defines a rectangle based on 0-rectangle.py"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the rectangle.
        Args:
            height(int)
            width(int)
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if type(value) != int:
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.__height)

    def __str__(self):
        """Draws the rectangle with the character #"""
        new_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += str(self.print_symbol)
                new_str += "\n"
            return new_str[:-1]

    def __repr__(self):
        """Returns a string representation to create a new instance"""
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """Prints 'Bye rectangle' when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns Rectangle with greatest area
            Args:
                rect_1 (Rectangle): firt Rectangle
                rect_2 (Rectangle): second Rectangle
            Raises:
                TypeError: If either rect_1 or rect_2 is not Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
