# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:07:05 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("You get "+str(block)+" block")