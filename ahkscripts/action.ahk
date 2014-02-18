; These are one button actions, like drinking Estus. I put a short 300 millisecond
; delay in, otherwise the game doesn't seem to register them.

command = %1%

send {%command% down}
sleep 300
send {%command% up}

ExitApp