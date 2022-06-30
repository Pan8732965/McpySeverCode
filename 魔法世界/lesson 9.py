# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:19:28 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
pos=mc.player.getPos()

def buildPyramid(x,y,z):
    base = 10
    height = (base//2)+1
    for i in range(height): #用來跑金字塔高度
    