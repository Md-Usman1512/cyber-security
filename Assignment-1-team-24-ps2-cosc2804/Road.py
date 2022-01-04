#   Python script for developing the road/pathing function/s
#       Author: Alex

from mcpi.minecraft import Minecraft
from mcpi import block as bl, vec3

import sys
import os
import time
import math
import random

#Adding this for readability of the code
mc = Minecraft.create()
# - Liam

sys.path.append(".")
from furniture_2storey import House


class Road:
    mc = Minecraft.create()

    def get_equation_line(self, coords_start, coords_end):
        try:
            m = float((coords_end[1] - (coords_start[1]))) / float((coords_end[0] - (coords_start[0])))
            c = (coords_end[1] - (m * coords_end[0]))
            variable_ar = [m, c]
        except ZeroDivisionError:
            m = 0
            c = (coords_end[1])
            variable_ar = [0, c]

        return variable_ar

    def get_door_direction(self, door_coords, orig_z):
        door_vec_coords = list(door_coords) #Convert Vector Object to list
        #Case for if door_z != orig_z  (door facing -x)
        if math.floor(door_vec_coords[2]) != (int(math.floor(orig_z)) + 1):
            return True
        else: #Case for if door_x != orig_x (door facing -z)
            return False    

    def door_plane(self, prev_x, prev_y, prev_z, testing_x, testing_z):
        #Check positive x direction for bl.AIR whilst being withing the wood & slab bounds
        while mc.getBlock(testing_x, prev_y, prev_z) == bl.STONE_SLAB.id:
            if mc.getBlock(testing_x, prev_y, prev_z) != bl.AIR.id and mc.getBlock(testing_x, prev_y, prev_z) != bl.STONE_SLAB.id: #i.e. if its wood
                break
            elif mc.getBlock(testing_x, prev_y, prev_z) == bl.STONE_SLAB.id:
                testing_x += 1

            if mc.getBlock(testing_x, prev_y, prev_z) == bl.AIR.id:
                #mc.setBlock(testing_x, prev_y, prev_z, bl.DIAMOND_BLOCK)
                return False
                break

        while mc.getBlock(prev_x, prev_y, testing_z) == bl.STONE_SLAB.id:
            if mc.getBlock(prev_x, prev_y, testing_z) != bl.AIR.id and mc.getBlock(prev_x, prev_y, testing_z) != bl.STONE_SLAB.id:
                break
            elif mc.getBlock(prev_x, prev_y, testing_z) == bl.STONE_SLAB.id:
                testing_z += 1
            if mc.getBlock(prev_x, prev_y, testing_z) == bl.AIR.id:
                #mc.setBlock(prev_x, prev_y, testing_z, bl.IRON_BLOCK)
                return True
                break

    def get_door_plane_x(self, orig_x, orig_z, orig_y, plot_gap, plot_gap_opposite, plot_width, road_width):
        #Checks either side to check if it contains a bl.AIR block, if so then thats the side with the door
        prev_x = orig_x - plot_gap + 1
        prev_z = orig_z - plot_gap_opposite + 1
        prev_y = mc.getHeight(orig_x, orig_z) + 1 

        testing_x = prev_x + 1
        testing_z = prev_z + 1

        if self.door_plane(prev_x, prev_y, prev_z, testing_x, testing_z) == True: #Door is facing -z axis
            nx = prev_x - 1 + (plot_width / 2)
            nz = prev_z - 1 + plot_width
            ny = mc.getHeight(nx, nz)
            
            mc.setBlocks(nx, ny, nz, nx + (plot_width / 2), ny, nz + road_width, bl.MOSS_STONE)
            mc.setBlocks(nx + (plot_width / 2), ny, nz - (plot_width / 2), nx + (plot_width / 2) + road_width, ny, nz + road_width, bl.MOSS_STONE)

    def get_door_plane_z(self, orig_x, orig_z, orig_y, plot_gap, plot_gap_opposite, plot_width, road_width):
        prev_x = orig_x - plot_gap_opposite + 1
        prev_z = orig_z - plot_gap + 1
        prev_y = mc.getHeight(orig_x, orig_z) + 1

        testing_x = prev_x + 1
        testing_z = prev_z + 1

        if self.door_plane(prev_x, prev_y, prev_z, testing_x, testing_z) == True: #Door is facing -z axis
            #mc.postToChat('Z House: Door facing -z')
            nx = prev_x - 1 + (plot_width / 2)
            nz = prev_z - 1 + plot_width
            ny = mc.getHeight(nx, nz)
            mc.setBlocks(nx, ny, nz, nx + road_width, ny, nz + road_width, bl.MOSS_STONE)
            mc.setBlocks(nx, ny, nz + road_width, nx + road_width, ny, nz + (2*road_width), bl.MOSS_STONE)
        else: #Door is facing -x axis
            nx = prev_x + plot_width
            nz = prev_z + (plot_width / 2) - road_width + 1
            time.sleep(0.01)

            ny = mc.getHeight(nx, nz)
            mc.setBlocks(prev_x + plot_width, ny, nz, prev_x + road_width + plot_width, ny, prev_z - 1 + plot_width + road_width, bl.MOSS_STONE)
            
            nx2 = prev_x + (plot_width / 2) - 1
            nz2 = prev_z - 1 + plot_width
            ny2 = mc.getHeight(nx2, nz2)
            mc.setBlocks(prev_x  + (plot_width / 2) - 1, ny2, prev_z - 1 + plot_width, prev_x + road_width + plot_width, ny2, prev_z - 1 + plot_width + road_width, bl.MOSS_STONE)

    def gen_house_path_pos_z(self, door_coords, road_width, orig_x, orig_z):
        time.sleep(0.05)
        #mc.postToChat('door facing -x')
        door_vec_coords = list(door_coords)
        #mc.postToChat('Neg X')
        #Front Door Path
        mc.setBlock(door_vec_coords[0] - 1, door_vec_coords[1], door_vec_coords[2], bl.MOSS_STONE)
        mc.setBlock(door_vec_coords[0], door_vec_coords[1], door_vec_coords[2], bl.MOSS_STONE)
        for i in range(0, (road_width + 1), 1):
            mc.setBlock(door_vec_coords[0] - i - 1, door_vec_coords[1], door_vec_coords[2], bl.MOSS_STONE)

        road_length_limit = int(math.floor(orig_z) + 16 + road_width + 1)
        for i in range(int(math.floor(door_vec_coords[2])), road_length_limit, 1): #Z Axis
            nx = int(math.floor(door_vec_coords[0])) - 1
            nz = i + 1
            ny = mc.getHeight(nx - 1, nz - 1)
            mc.setBlocks(int(math.floor(door_vec_coords[0])) - road_width - 2, ny, int(math.floor(door_vec_coords[2])), nx - 1, ny, nz - 1, bl.MOSS_STONE)

        path_limit_x = int(int(math.floor(orig_x)) + (16 / 2))
        for i in range(int(math.floor(orig_x)) - 1, path_limit_x, 1): #X Axis
            nx = i + 1
            nz = int(math.floor(orig_z)) + road_width + 16
            ny = int(mc.getHeight(nx, nz))
            mc.setBlocks(int(math.floor(orig_x)) - road_width + 2, ny, (int(math.floor(orig_z)) + 16), nx, ny, nz, bl.MOSS_STONE)

    def gen_house_path_pos_x(self, door_coords, road_width, orig_x, orig_z):
        time.sleep(0.05)
        #mc.postToChat('door facing -z')
        door_vec_coords = list(door_coords)
        #mc.postToChat('Neg Z')
        #Front Door Path
        #16 is the plot width
        mc.setBlock(door_vec_coords[0], door_vec_coords[1], door_vec_coords[2] - 1, bl.MOSS_STONE)
        mc.setBlock(door_vec_coords[0], door_vec_coords[1], door_vec_coords[2], bl.MOSS_STONE)
        for i in range(0, (road_width + 1), 1):
            mc.setBlock(door_vec_coords[0], door_vec_coords[1], door_vec_coords[2] - i - 1, bl.MOSS_STONE)

        road_length_limit = int(math.floor(orig_x) + 16 + road_width + 1)
        for i in range(int(math.floor(door_vec_coords[0])), road_length_limit, 1): #X Axis
            new_path_block_x = i + 1
            new_path_block_z = int(math.floor(door_vec_coords[2])) - road_width - 2
            new_path_block_y = mc.getHeight(new_path_block_x, new_path_block_z)
            mc.setBlocks(int(math.floor(door_vec_coords[0])), new_path_block_y, new_path_block_z, new_path_block_x, new_path_block_y, int(math.floor(orig_z)) - 1, bl.MOSS_STONE)
            #mc.setBlock(new_path_block_x, new_path_block_y, new_path_block_z, bl.OBSIDIAN)

        path_limit_z = int(int(math.floor(orig_z)) + (16 / 2))
        for i in range(int(math.floor(orig_z)), path_limit_z, 1):
            nx = int(math.floor(orig_x)) + road_width + 16
            nz = i
            test_z = i + 1
            ny = int(mc.getHeight(nx, nz))
            mc.setBlocks(int(math.floor(orig_x)) + 17, ny, int(math.floor(orig_z)) - road_width, nx + 1, ny, test_z, bl.MOSS_STONE)
            #mc.setBlock(nx, ny, test_z, bl.OBSIDIAN)

    ## FIXED: Passed 'self' in through gen_road()
    def gen_road(self):
        pos = mc.player.getPos()

        orig_x, orig_y, orig_z = pos.x, pos.y, pos.z

        upper_limit = 7 #Maximum can whatever limit we want
        lower_limit = 4 #Minimum should be set to at least 4
        number_of_houses = random.randint(lower_limit, upper_limit)
        road_width = random.randint(2, 4) #Road Width

        #Get a coordinate list of where the houses will be placed using randint
        #   - since the house is 16 * 16 blocks & MAX road width is 5 a house cannot be within a 26 block radius of each coord 
        #       i.e. the difference in 1 of the coords must be > 26 blocks
        for i in range(0, number_of_houses, 1):
            #mc.postToChat('House: {}, @ X: {}, Y: {}, Z: {}'.format(i, orig_x, orig_y, orig_z))
            #gets a coord from original player pos, i.e. select either x or z plain from random
            plain = random.randint(0, 1)
            plot_width = 16
            plot_gap = random.randint(27, 32)
            plot_gap_opposite = random.randint(math.sqrt(plot_width), plot_width) #originally (0,8)
            a = (plot_width) / 2

            if plain == 0: #Positive x direction 
                if i != 0: 
                    time.sleep(0.05)
                    orig_x += plot_gap
                    orig_z += plot_gap_opposite   

                    variable_y = mc.getHeight(orig_x, orig_z)
                    #mc.postToChat('House {}, built in +X'.format(i))
                    time.sleep(0.05)
                    door_xyz_coords = House(orig_x, variable_y + 1, orig_z)
                    door_vec_coords = list(door_xyz_coords)
                    #Determines which side the door is on
                    if self.get_door_direction(door_xyz_coords, orig_z) == True:
                        #mc.postToChat('House: {}, door facing -x'.format(i))
                        self.gen_house_path_pos_z(door_xyz_coords, road_width, orig_x, orig_z) #Pass original coordinates, pass door coordinates
                        
                    else:
                        #mc.postToChat('House: {}, door facing -z'.format(i))
                        self.gen_house_path_pos_x(door_xyz_coords, road_width, orig_x, orig_z)
                        #door is facing -z
                        nx = orig_x - 1 - road_width
                        nz = orig_z - 1 - road_width
                        ny = mc.getHeight(nx, nz)
                        mc.setBlocks(nx, ny, nz, door_vec_coords[0], ny, nz + road_width, bl.MOSS_STONE)
                        mc.setBlocks(nx, ny, nz, nx + road_width, ny, orig_z + (plot_width / 2), bl.MOSS_STONE)

                    #Next generate a road in the negative x direction 
                    c = orig_z + a #Starting z position
                    d = orig_x - road_width - 1 #Starting x position

                    diff_x = plot_gap - ((road_width + 1) * 2) - plot_width
                    limit_x = d - diff_x
                    diff_z = plot_gap_opposite
                    limit_z = c - diff_z
                    #mc.setBlock(limit_x, orig_y, limit_z, bl.DIAMOND_BLOCK) #Testing lower limit


                    # y = mx + c given (x1, y1) & (x2, y2). Where y = x (in mc) & x = z (in mc)
                    for j in range(0, (road_width - 1), 1):
                        equ_line_vars = self.get_equation_line([c + j, d], [limit_z + j, limit_x])
                        gradient = equ_line_vars[0]
                        rise = equ_line_vars[1]

                        for h in range(int(limit_z + j - 1), int(c), 1): #increasing z axis coord (x)
                            curved_x = gradient * h + rise
                            mc.setBlock(int(math.ceil(curved_x)), variable_y, h, bl.MOSS_STONE)
                            mc.setBlock(int(math.ceil(curved_x)), variable_y, h - 1, bl.MOSS_STONE)
                            mc.setBlock(int(math.floor(curved_x)), variable_y, h, bl.MOSS_STONE)
                            mc.setBlock(int(math.floor(curved_x)), variable_y, h + 1, bl.MOSS_STONE)
                            time.sleep(0.05)
                            mc.setBlock(int(math.floor(curved_x)) - 1, variable_y, h, bl.MOSS_STONE)
                            mc.setBlock(int(math.floor(curved_x)) + 1, variable_y, h, bl.MOSS_STONE)

                    self.get_door_plane_x(orig_x, orig_z, orig_y, plot_gap, plot_gap_opposite, plot_width, road_width)

                    
                else:
                    time.sleep(0.05)
                    variable_y = mc.getHeight(orig_x, orig_z)
                    door_xyz_coords = House(orig_x, variable_y + 1, orig_z)
                    #Determine which side the door is on
                    if self.get_door_direction(door_xyz_coords, orig_z) == True:
                        #self.gen_house_path_pos_z(door_xyz_coords, road_width, orig_x, orig_z) #Pass original coordinates, pass door coordinates
                        #mc.postToChat('DONE')
                        self.gen_house_path_pos_z(door_xyz_coords, road_width, orig_x, orig_z)

                    else:
                        #self.gen_house_path_pos_x(door_xyz_coords, road_width, orig_x, orig_z)
                        self.gen_house_path_pos_x(door_xyz_coords, road_width, orig_x, orig_z)

            else: #Positive z direction
                if i != 0: 
                    time.sleep(0.05)
                    #mc.postToChat('House {}, built in +Z'.format(i))
                    orig_z += plot_gap
                    orig_x += plot_gap_opposite
                    variable_y = mc.getHeight(orig_x, orig_z)
                    door_xyz_coords = House(orig_x, variable_y + 1, orig_z)

                    door_vec_coords = list(door_xyz_coords)
                    #Determine which side the door is on
                    if self.get_door_direction(door_xyz_coords, orig_z) == True:
                        #mc.postToChat('House: {}, door facing -x'.format(i))
                        self.gen_house_path_pos_z(door_xyz_coords, road_width, orig_x, orig_z) #Pass original coordinates, pass door coordinates
                        nx = orig_x - 1 - road_width
                        nz = orig_z - 1 - road_width
                        ny = mc.getHeight(nx, nz)
                        mc.setBlocks(nx, ny, nz, nx + (plot_width / 2) + road_width, ny, nz + road_width, bl.MOSS_STONE)
                        mc.setBlocks(nx, ny, nz, nx + road_width, ny, orig_z + (plot_width / 2), bl.MOSS_STONE)

                        mc.setBlock(door_vec_coords[0], door_vec_coords[1] - 1, door_vec_coords[2], bl.MOSS_STONE)
                    else:
                        #mc.postToChat('House: {}, door facing -z'.format(i))
                        self.gen_house_path_pos_x(door_xyz_coords, road_width, orig_x, orig_z)



                    #Next generate a road in the negative z direction 
                    c = orig_x + a #Starting X position
                    d = orig_z - road_width - 1 #Starting Z position

                    diff_z = plot_gap - ((road_width + 1) * 2) - plot_width
                    limit_z = d - diff_z #Lower Z limit

                    diff_x = plot_gap_opposite
                    limit_x = c - diff_x #Lower X limit

                    for j in range(0, (road_width - 1), 1):
                        #increase coords by +j
                        equ_line_vars = self.get_equation_line([d, c + j], [limit_z, limit_x + j])
                        gradient = equ_line_vars[0]
                        rise = equ_line_vars[1]

                        for h in range(int(limit_x + j), int(c), 1):
                            # y = mx + c (Rearrange to get in terms of x)
                            # i.e. x = (y - c) / m
                            curved_z = (h - rise) / gradient
                            mc.setBlock(h, variable_y, int(math.ceil(curved_z)), bl.MOSS_STONE)
                            mc.setBlock(h, variable_y, int(math.floor(curved_z)), bl.MOSS_STONE)
                            mc.setBlock(h - 1, variable_y, int(math.ceil(curved_z)), bl.MOSS_STONE)
                            mc.setBlock(h + 1, variable_y, int(math.ceil(curved_z)), bl.MOSS_STONE)
                            time.sleep(0.05)
                            mc.setBlock(h - 1, variable_y, int(math.floor(curved_z)) - 1, bl.MOSS_STONE)
                            mc.setBlock(h + 1, variable_y, int(math.floor(curved_z)) + 1, bl.MOSS_STONE)

                    
                    self.get_door_plane_z(orig_x, orig_z, orig_y, plot_gap, plot_gap_opposite, plot_width, road_width)
                else:
                    time.sleep(0.05)
                    variable_y = mc.getHeight(orig_x, orig_z)
                    door_xyz_coords = House(orig_x, variable_y + 1, orig_z)

                    #Determine which side the door is on
                    if self.get_door_direction(door_xyz_coords, orig_z) == True:
                        self.gen_house_path_pos_z(door_xyz_coords, road_width, orig_x, orig_z) #Pass original coordinates, pass door coordinates
                    else:
                        self.gen_house_path_pos_x(door_xyz_coords, road_width, orig_x, orig_z)

            time.sleep(0.1)
