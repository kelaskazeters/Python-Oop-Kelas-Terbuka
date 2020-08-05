#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""

# membuat class abstract
# abc= abstract base class
from abc import ABC,abstractmethod


class Button(ABC):
    
    
    @abstractmethod
    def click(self):
        print("button click")

class PushButton(Button):
    
    def click(self):
        print("push button click")

class RadioButton(Button):
    
    def click(self):
        print("radio button click")

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()