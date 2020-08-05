#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""

from abc import ABC,abstractmethod

class Button(ABC):
    
    def __init__(self,set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    @property
    @abstractmethod
    def link(self):
        pass
    
    
class PushButton(Button):
    
    def click(self):
        print("Go To: {}".format(self.link))
    
    @Button.link.setter
    def link(self,input):
        self.__link = input
    
    @link.getter
    def link(self):
        return self.__link
    
tombol1 = PushButton("www.kasetgaming.blogspot.com")
tombol1.click()