# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:19:28 2022

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
pos=mc.player.getPos()

"""def buildPyramid(x,y,z):
    base = 10
    height = (base//2)+1 # //為留整數部分
    for i in range(height): #用來跑金字塔高度
     x1=x+i
     y1=y+i
     z1=z+i
     
     x2=x+base-i
     #y2和y相同
     z2=z+base-i
     mc.setBlocks(x1,y1,z1,x2,y,z2,21)

mc.postToChat("start get pos")
x,y,z=mc.player.getTilePos()
buildPyramid(x, y, z) #或者buildyramid(x,y,z,20)"""

#串列
"""
line1=[]
line2=[]
line3=[]

for i in range(1,4):
    line1.append(1*i) #1的乘法
for i in range(1,4):
    line2.append(2*i) #2的乘法
for i in range(1,4):
    line3.append(3*i) #3的乘法
    
print(line1)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))
"""
# 自我複製

number=1 # 每次複製的量
x,y,z=mc.player.getTilePos()

for i in range(8): # 每次生成的量。總共生8批，禁止超過8批
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number*2

mc.postToChat("這次生成了" + str(number) + "隻蠹魚")
    
    