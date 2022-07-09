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
    r=random.choice(range(1,5)) #隨機選數
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)#往x方向蓋
        x=x+4 #程式幫我們虛擬我們傳送到x+4的位置，然後繼續在新位置(x+4)的位置加蓋
        #print("x:"+str(x))
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,1)#往x方向蓋
        x=x-4
        #print("x:"+str(x))
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,1)#往z方向蓋
        z=z+4
        #print("z:"+str(z))
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,1)#往z方向蓋
        z=z-4
        #print("z:"+str(z))
# mc.postToChat(str(x)+","+str(y)+","+str(z))

#時間魔法師
"""
while True:
    mc.executeCommand("time add 50") #指令打在引號裡
    sleep(0.05)
"""


