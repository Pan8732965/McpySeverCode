# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:12:06 2022

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
for i in range(10):
    for j in range(5):
        plantTree(x+i*5, y+j*4, z)
    


