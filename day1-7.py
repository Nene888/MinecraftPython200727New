# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:10:18 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z, =mc.player.getTilePos()
mc.setBlock(x,y-1,z,46)