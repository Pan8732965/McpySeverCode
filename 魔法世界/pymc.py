# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:14:43 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
time.sleep(5)

position = mc.player.getTilePos()
x=position.x
y=position.y
z=position.z

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.slee(0.5)
y=y+1
mc.player.setTilePos(x,y,z)