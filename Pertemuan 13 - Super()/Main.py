#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.health))
    
class Hero_intelligent(Hero):
    def __init__(self,name):
        #Hero.__init__(self,name,100)
        super().__init__(name,100)
        super().showInfo()

class Hero_strength(Hero):
    def __init__(self,name):
        #Hero.__init__(self,name,200)
        super().__init__(name,200)
        super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')