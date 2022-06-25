# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:49:10 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
# import time
mc = Minecraft.create()

mc.postToChat("I'm watching you!")
t=0;

while True:
    x,y,z= mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)+",Y:"+str(y)+",Z:"+str(z))
    