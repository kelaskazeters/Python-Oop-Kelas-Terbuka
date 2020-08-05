#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""

class A:
    
    def method_A(self):
        print("ini adalah method A")

class B:
    
    def method_B(self):
        print("ini adalah method B")
    
class C(A,B):
    pass


objek = C()

objek.method_A()
objek.method_B()
