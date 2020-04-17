mov edx, 0x8048662 			# go to normal execution
jmp edx

mov ax, [ebp-0x40C]	# jumping to here
mov bx, 0x2123 # equals to #!
cmp bx, ax
jne not_shell_cmd


lea eax, [ebp-0x40C+2] # push the line (without #!) for system()
push eax
mov ebx, 0x8048460 
call ebx 				# call system
add esp, 4
mov edx, 0x8048662 		
jmp edx						# go to after print


not_shell_cmd:
mov edx, 0x804863A
jmp edx