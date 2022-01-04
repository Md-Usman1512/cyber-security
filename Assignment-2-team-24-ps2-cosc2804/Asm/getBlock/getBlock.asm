.ORIG x3000
        LD R0 x_Coord
        LD R1 y_Coord
        LD R2 z_Coord

        TRAP 0x36
        HALT

x_Coord  .FILL        #73
y_Coord  .FILL        #0
z_Coord  .FILL        #19

        .END
