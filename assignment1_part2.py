#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 part 2"""

class Book:
    def __init__( x, author = '', title = '' ):
        x.a = author
        x.t = title
        return

    def display(x):
        """This fuction prints the book title and author"""
        print "%s, written by %s" % (x.a, x.t)
        return

firstbook = Book('Of Mice and Men', 'John Steinbeck')
secondbook = Book('To Kill a Mockingbird', 'Harper Lee')

firstbook.display()
secondbook.display()
