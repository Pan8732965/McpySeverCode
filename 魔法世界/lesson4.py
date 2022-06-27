# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:07:02 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

#get block &輕功水上漂

x,y,z=mc.player.getTilePos()
a=mc.getBlock(x,y-1,z+1)
b=mc.getBlock(x,y-1,z-1)
c=mc.getBlock(x-1,y-1,z)
d=mc.getBlock(x+1,y-1,z)

#while True:
    #mc.postToChat(str(a)+","+str(b)+","+str(c)+","+str(d))
if a==9 or b==9 or c==9 or d==9:
    mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,103)
    
    
"""while a==8 or a==9 or b==9 or c==8 or c==9 or d==8 or d==9:
    mc.setBlock(x+1,y-1,z+1,x-1,y-1,z-1,103)
    time.sleep(0.2)"""

# 小花
'''while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,55)
    time.sleep(0.2)'''
#水壩
"""
i=0
while i<20:
    mc.setBlocks(x+10,y-30,z,x-10,y+1,z,19)
    z=z-5
    i=i+1
    """