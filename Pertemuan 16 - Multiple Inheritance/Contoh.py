#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:24:35 2019

@author: rafliano
"""
class Team:
    def setTeam(self,team):
        self.team = team
    
    def showTeam(self):
        print(self.team)


class Tipe_Hero:
    def setTipe(self,tipe):
        self.tipe = tipe
    
    def showTipe(self,):
        print(self.tipe)
    
    
class Hero(Team,Tipe_Hero):
    
    def __init__(self,name,health):
        self.name = name
        self.health = health

Ucup = Hero('Ucup',100)
Ucup.setTeam("Merah")
Ucup.setTipe("panglima perang")

Ucup.showTeam()
Ucup.showTipe()