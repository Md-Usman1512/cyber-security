from mcpi.minecraft import Minecraft
from mcpi import block as bl, vec3

import sys
import os
import time
import math
import random


mc = Minecraft.create()

sys.path.append(".")
from Road import Road

# Assignment 1 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

mc = Minecraft.create()
mc.postToChat("Village Generating...")

generate_road = Road()
generate_road.gen_road()


mc.postToChat("Village Generated")