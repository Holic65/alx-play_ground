#!/usr/bin/python3
''' A class rectangle definition'''

class Rectangle(Base):
    '''class rectangle initialization'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init of rectangle class'''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

