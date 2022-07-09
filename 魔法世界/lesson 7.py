# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:07:05 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
pos=mc.player.getPos()

#點石成金
"""while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("You get "+str(block)+" block")
        mc.setBlock(x,y,z,41)"""
#告示牌
# mc.setSign(x,y,z,63,0,"Hello","World","HAHA","OWO")
#天降雞雨
"""while True:
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    y=pos.y+40
    mc.spawnEntity(x,y,z, 80)
    time.sleep(0.1)"""
#爆破弓箭
while True:
    hits = mc.events.pollProjectileHits() # <--代表弓箭拋射物發射的事件  mc.events.pollBlockHits 是去偵測hit的一塊塊方塊的
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.createExplosion(x,y,z)
        #mc.player.setTilePos(x,y,z)
        #mc.spawnEntity(x,y,z,99)
    