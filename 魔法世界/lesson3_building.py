# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:00:42 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# mc.player.setTilePos(1.5,1.5,1.5)
time.sleep(3)
x,y,z = mc.player.getTilePos()
mc.postToChat("You are located on X:"+str(x)+",Y:"+str(y)+",Z:"+str(z))
width=10
height=5
length=6
blocktype=4
air=0

mc.setBlocks(x,y,z,x+width,y+height,z+length,blocktype)
time.sleep(3)
#mc.setBlocks(x,y,z,x+width,y+height,z+length,0) # outside material
mc.setBlocks(x + 1,y + 1,z + 1,x + width - 1 ,y + height - 1 ,z + length - 1, 0)# inside air
#why
'''mc.setBlock(x,y,z,206)
mc.setBlock(x,y+1,z,206)
mc.setBlock(x,y+2,z,206)
mc.setBlock(x,y+3,z,206)
mc.setBlock(x,y+4,z,206)
mc.setBlock(x,y+5,z,206)
mc.setBlock(x,y+6,z,206)
mc.setBlock(x,y+7,z,206)
mc.setBlock(x,y+8,z,206)
mc.setBlock(x,y+9,z,206)'''

# mc.setBlocks(x,y,z,x+100,y,z,152)

'''mc.setBlock(x,y-1,z,206)
time.sleep(1)
mc.setBlock(x,y-1,z+1,206)
time.sleep(1)
mc.setBlock(x+1,y-1,z+1,206)
time.sleep(1)
mc.setBlock(x+2,y-1,z+1,206)
time.sleep(1)
mc.setBlock(x+2,y-1,z,206)
time.sleep(1)
mc.setBlock(x+2,y-1,z-1,206)
time.sleep(1)
mc.setBlock(x+1,y-1,z-1,206)
time.sleep(1)
mc.setBlock(x,y-1,z-1,206)
time.sleep(1)
mc.setBlock(x+1,y-1,z,11)'''

'''mc.setBlocks(x,y-1,z+1,x+2,y-1,z-1,206)
time.sleep(2)
mc.setBlock(x+1,y-1,z,11)'''


