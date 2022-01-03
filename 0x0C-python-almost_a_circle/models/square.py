#!/usr/bin/python3
"""Module square
This class Square that inherits from Rectangle
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class describing a square
    
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
        All inherit from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """This function initializes a square instance

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__width)
    
    @property
    def size(self):
        """It retrieves the size attribute"""

        return self.__width
    
    @size.setter
    def size(self, value):
        """This function sets the size attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if type(value) <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value
        self.__height = value
    
    def update(self, *args, **kwargs):
        """Update the square class and assign attributes
        
        Args:
            - id attribute
            - size attribute
            - x attribute
            - y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """Update the class Square and returns the dictionary representation of a Square"""

        my_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

        return my_dict