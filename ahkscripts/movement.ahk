; Takes in the keys to be entered (as command) and the length
; that key should be pressed down. "RUN" and "ROLL" are special
; movements that require a bit more work, thus the statements for them.

command = %1%
length = %2%

if(command = "RUN") {
	send {w down}
	send {SPACE down}
	sleep 1500
	send {SPACE up}
	send {w up}
	ExitApp
}

if(command = "ROLL") {
	send {w down}
	send {SPACE down}
	sleep 100
	send {SPACE up}
	send {w up}
	ExitApp
}

send {%command% down}
sleep %length%
send {%command% up}

ExitApp