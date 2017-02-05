#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 assignment part 1"""

def listDivide(numbers,divide=2):
        """The function returns the number of elements in the numbers'
        'list that are divisible by divide.
        Args:
                numbers(list): list of divisible numbers
                divide(int): this should have a default value of 2

        Return:
                int: returns interger from the division result
        Example:
                >>> listDivide([1,2,3,4,5])
                2
                >>> listDivide([30,54,63,98,100], divide=10)
                2
        """
        div = 0
        for num in numbers:
                if num % divide == 0:
                        div += 1
        return div

class ListDivideException(Exception):
        pass

def testListDivide():

        try:
                listDivide([1,2,3,4,5])
        except:
                raise ListDivideException('Unknown Issue')
        try:
                listDivide([2,4,6,8,10])
        except:
                raise ListDivideException('Unknown Issue')
        try:
                listDivide([30,54,63,98,100], divide=10)
        except:
                raise ListDivideException('Unknown Issue')
        try:
                listDivide([])
        except:
                raise ListDivideException('Unknown Issue')
        try:
                listDivide([1,2,3,4,5],1)
        except:
                raise ListDivideException('Unknown Issue')
        return

testListDivide()
