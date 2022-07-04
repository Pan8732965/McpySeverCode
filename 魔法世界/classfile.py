# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 21:12:55 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#獲取座標
position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z

mc.postToChat(str(x)+","+str(y)+","+str(z))

#設定角色座標
#mc.player.setTilePosition()



