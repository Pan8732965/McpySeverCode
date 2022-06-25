# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:38:27 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

"""a=0
while a<6:
    print('hello'+str(a))
    a=a+1
while True:
      time.sleep(2)
      steps=200
      #teps=random.randint(1,30)
      mc.player.setTilePos(x+steps,y,z)"""
#blocks=mc.getBlock(x,y-1,z)
if mc.getBlock(x,y-1,z)==12:
    #由0和81隨機取一個
    target=random.choice([0,81])
    mc.setBlock(x,y,z,target)
else:
    #由1到8隨機取一個
    target = random.randint(1,8)
    mc.setBlocks(x,y,z,x+5,y,z+5,38,target)