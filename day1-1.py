# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:58:32 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())
