        .ORIG x3001
        LEA R4 message

        TRAP 0x31
        HALT
message .STRINGZ "Player position"
        .END




;         .ORIG x3000
;         LEA R3 MCStr
;         TRAP 0x30
;         HALT
; MCStr   .STRINGZ "Hello Minecraft!!"
;         .END