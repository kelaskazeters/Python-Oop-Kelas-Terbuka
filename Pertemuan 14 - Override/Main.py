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
        print("showInfo di class Hero")
        print("{} health: {}".format(
                self.name,
                self.health
                ))
    
class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\tHealth: {}".format(
                self.name,
                self.health
                ))

class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

axe.showInfo()
