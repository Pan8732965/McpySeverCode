# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 09:17:34 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from time import sleep
import random 


x,y,z = mc.player.getTilePos()

#圖騰

for i in range(20): #執行20次，有20個方塊
    r=random.randrange(1,5) #隨機選數
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
        print("x:"+str(x))
    if r==2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4
        print("x:"+str(x))
    if r==3:
        mc.setBlocks(x,y,z,z+4,y,z,1)
        z=z+4
        print("z:"+str(z))
    if r==4:
        mc.setBlocks(x,y,z,z-4,y,z,1)
        z=z-4
        print("z:"+str(z))
# mc.postToChat(str(x)+","+str(y)+","+str(z))

#時間魔法師
"""
while True:
    mc.executeCommand("time add 50") #指令打在引號裡
    sleep(0.05)
"""


