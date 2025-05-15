#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 31 15:18:03 2022

@author: Vinod K. Batra
"""
import sys
from vpython import *

###########################################################
POLE_LENGTH = 6
DISKS = []
COLORS = [color.red, color.green, color.blue, color.orange, color.yellow, color.magenta]
deltaRadius = 0.1
j = 1
###############################################################

def setupDisks(numDisks, poleRadius=0.2):

    cylinder(color=color.white, pos=vector(-POLE_LENGTH, -4., -2),
             radius=poleRadius, length=POLE_LENGTH*2, axis=vector(1, 0, 0))

    cylinder(color=color.white, pos=vector(-POLE_LENGTH, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))
    cylinder(color=color.white, pos=vector(0, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))
    cylinder(color=color.white, pos=vector(POLE_LENGTH, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))

    text(text="Source", height=0.5, pos=vector(-7, 2.5, -2))
    text(text="Temp", height=0.5, pos=vector(-1, 2.5, -2))
    text(text="Destination", height=0.5, pos=vector(5, 2.5, -2))

    for i in range(numDisks):
        disk = ring(color=COLORS[i], radius=1-deltaRadius*i, thickness=0.3, pos=vector(-POLE_LENGTH, -3+i, -2),
                    axis=vector(0, -1, 0))
        DISKS.append(disk)
