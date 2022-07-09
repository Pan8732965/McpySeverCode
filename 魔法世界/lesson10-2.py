# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 16:26:48 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

x,y,z = mc.player.getTilePos

for i in range(20): #執行20次，有20個方塊
    r=random.randrange(1,5) #隨機選數
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        z=z-4