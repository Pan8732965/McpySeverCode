# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:01:32 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

time.sleep(3)
#樓梯
for i in range(1,20):
    """mc.setBlock(x+i,y-1+i,z,109)
    mc.setBlock(x+i,y-1+i,z+1,109)
    mc.setBlock(x+i,y-1+i,z+2,109)"""
    mc.setBlocks(x+i,y-1+i,z,x+i,y-1+i,z+2,109)
#上面的草地
mc.setBlocks(x+i+1,y-1+i,z,x+i+3,y-1+i,z+2,2)
