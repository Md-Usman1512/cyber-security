#   Python script for developing the house function.
#       Author: Liam :)
#       (premature thanks to Eray for terrain smoothing)
#   this was very fun to make

from mcpi.minecraft import Minecraft

from mcpi import block as bl, vec3

import time

import math

import random



mc = Minecraft.create()



#mc.saveCheckpoint()


#HOUSE FUNCTION
def House(x1, y1, z1) -> vec3.Vec3:
    #Init return value
    door_xyz = vec3.Vec3(-1) 

    #sets the far boundary corner (16x16 block area)
    x2 = x1 + 15
    z2 = z1 + 15



    #gets the block below the input coords and sets it as the ground block.
    #TODO: THIS will be obsolete with new terrain integration (having the house on stilts for corners that aren't level)
    ground = mc.getBlockWithData(x1, y1 - 1, z1)
    #CLEARS the ground and flattens everything
    mc.setBlocks(x1, y1 - 1, z1, x2, y1 - 1, z2, ground)
    mc.setBlocks(x1, y1, z1, x2, y1 + 15, z2, bl.AIR)



    #Randomises width and length of house
    x_len = random.randint(5, 11)
    z_len = random.randint(5, 11)

    #x_len = 9
    #z_len = 10

    #sets house x and z boundaries according to this randomised length
    h_x1 = x1 + 2
    h_z1 = z1 + 2
    h_x2 = x1 + x_len + 2
    h_z2 = z1 + z_len + 2

    #slab trim around house
    mc.setBlocks(h_x1 - 1, y1, h_z1 - 1, h_x2 + 1, y1, h_z2 + 1, bl.STONE_SLAB)

    #ceiling trim
    mc.setBlocks(h_x1 - 1, y1 + 4, h_z1 -1, h_x2 + 1, y1 + 4, h_z2 + 1, bl.STONE_SLAB)

    #walls
    rnd_wood = random.randint(0,3)
    mc.setBlocks(h_x1, y1 - 1, h_z1, h_x2, y1 + 4, h_z2, bl.WOOD_PLANKS.id, rnd_wood)
    mc.setBlocks(h_x1 + 1, y1, h_z1 + 1, h_x2 - 1, y1 + 3, h_z2 - 1, bl.AIR)

    #pillars
    mc.setBlocks(h_x1 - 1, y1, h_z1 - 1, h_x1 - 1, y1 + 4, h_z1 - 1, bl.WOOD.id, rnd_wood)
    mc.setBlocks(h_x1 - 1, y1, h_z2 + 1, h_x1 - 1, y1 + 4, h_z2 + 1, bl.WOOD.id, rnd_wood)
    mc.setBlocks(h_x2 + 1, y1, h_z1 - 1, h_x2 + 1, y1 + 4, h_z1 - 1, bl.WOOD.id, rnd_wood)
    mc.setBlocks(h_x2 + 1, y1, h_z2 + 1, h_x2 + 1, y1 + 4, h_z2 + 1, bl.WOOD.id, rnd_wood)

    #door & windows
    door_side = random.randint(0, 1)
    if door_side == 1:
        #DOOR FACING NEGATIVE X
        door_placement = random.randint(1, x_len - 2)
        mc.setBlock(h_x1 + door_placement, y1 + 1, h_z1, (bl.DOOR_DARK_OAK.id, 9))
        mc.setBlock(h_x1 + door_placement, y1, h_z1, bl.DOOR_DARK_OAK.id, 1)
        mc.setBlock(h_x1 + door_placement, y1, h_z1 - 1, bl.AIR)

        door_xyz = vec3.Vec3(h_x1 + door_placement, y1 - 1, h_z1 - 1)

        #WINDOW FACING NEGATIVE Z
        window_len = random.randint(0, z_len - 2)
        
        if window_len != 0:
            win_start = random.randint(1, z_len - window_len)
            mc.setBlocks(h_x1, y1 + 1, h_z1 + win_start, h_x1,  y1 + 2, h_z1 + window_len, bl.GLASS.id)

        
    else:
        #DOOR FACING NEGATIVE Z
        door_placement = random.randint(1, z_len - 2)
        mc.setBlock(h_x1, y1 + 1, h_z1 + door_placement, (bl.DOOR_DARK_OAK.id, 10))
        mc.setBlock(h_x1, y1, h_z1 + door_placement, bl.DOOR_DARK_OAK.id, 2)
        mc.setBlock(h_x1 - 1, y1, h_z1 + door_placement, bl.AIR)

        door_xyz = vec3.Vec3(h_x1 - 1, y1 - 1, h_z1 + door_placement)

        #WINDOW FACING NEGATIVE X
        window_len = random.randint(0, x_len - 2)
        
        if window_len != 0:
            win_start = random.randint(1, x_len - window_len)
            mc.setBlocks(h_x1 + win_start, y1 + 1, h_z1, h_x1 + window_len,  y1 + 2, h_z1, bl.GLASS.id)

        
    #TODO: find real-world pobability of Australian houses having a pool, use that statistic as % chance to spawn a pool in the first place.
    if (x_len < 10):
        #POOL IS PLACED ALONG POSITIVE x AXIS
        px_len = 11 - x_len
        pz_len = random.randint(4, 10)
        #mc.postToChat("xlen: {}, pxlen: {}".format(x_len, px_len))
        px1 = x1 + x_len + 4
        pz1 = z1 + random.randint(0, 15 - pz_len)

        mc.setBlocks(px1, y1, pz1, px1 + px_len, y1, pz1 + pz_len, bl.FENCE)
        mc.setBlocks(px1, y1 - 2, pz1, px1 + px_len, y1 - 2, pz1 + pz_len, bl.END_STONE)
        mc.setBlocks(px1, y1 - 1, pz1, px1 + px_len, y1 - 1, pz1 + pz_len, bl.COBBLESTONE)
        
        mc.setBlocks(px1 + 1, y1, pz1 + 1, px1 + px_len - 1, y1 - 1, pz1 + pz_len - 1, bl.AIR)
        mc.setBlocks(px1 + 1, y1 - 1, pz1 + 1, px1 + px_len - 1, y1 - 1, pz1 + pz_len - 1, bl.WATER_STATIONARY)

        #BUG here as mentioned in TODO above
        mc.setBlock(px1 + random.randint(1, px_len - 1), y1, pz1, bl.FENCE_GATE)

        pass
    elif (z_len < 10):
        #POOL IS PLACED ALONG POSITIVE z AXIS

        pz_len = 11 - z_len
        px_len = random.randint(4, 10)
        #mc.postToChat("zlen: {}, pzlen: {}".format(x_len, px_len))
        pz1 = z1 + z_len + 4
        px1 = x1 + random.randint(0, 15 - px_len)

        mc.setBlocks(px1, y1, pz1, px1 + px_len, y1, pz1 + pz_len, bl.FENCE)
        mc.setBlocks(px1, y1 - 2, pz1, px1 + px_len, y1 - 2, pz1 + pz_len, bl.END_STONE)
        mc.setBlocks(px1, y1 - 1, pz1, px1 + px_len, y1 - 1, pz1 + pz_len, bl.COBBLESTONE)
        
        mc.setBlocks(px1 + 1, y1, pz1 + 1, px1 + px_len - 1, y1 - 1, pz1 + pz_len - 1, bl.AIR)
        mc.setBlocks(px1 + 1, y1 - 1, pz1 + 1, px1 + px_len - 1, y1 - 1, pz1 + pz_len - 1, bl.WATER_STATIONARY)

        #BUG also here as mentioned in TODO above
        mc.setBlock(px1, y1, pz1 + random.randint(1, pz_len - 1), bl.FENCE_GATE.id, 1)
        pass



    return door_xyz
        
pos = mc.player.getPos()

while True:
    hx, hy, hz = House(pos.x, pos.y, pos.z)
    #mc.postToChat("{:.0f}, {:.0f}, {:.0f}".format(hx, hy, hz))
    #time.sleep(2)
    break

#time.sleep(10)

#mc.restoreCheckpoint()
