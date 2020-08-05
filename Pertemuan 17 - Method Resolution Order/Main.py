#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""

# method resolution order // multiple inherintance

class A:
    
    def show(self):
        print('ini adalah show A')

class B:
    
    def show(self):
        print('ini adalah show B')

class C(B,A):
    pass


objek = C()
objek.show()
#help(objek)