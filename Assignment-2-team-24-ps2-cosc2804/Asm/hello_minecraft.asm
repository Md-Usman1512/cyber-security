        .ORIG x3000
        LEA R3 MCStr
        TRAP 0x30
        HALT
MCStr   .STRINGZ "Hello Minecraft!!"
        .END