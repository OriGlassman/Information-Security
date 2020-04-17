import assemble

def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    data_list = list(data)
    replacement_list = list(assemble.assemble_file("patch1.asm")) 
    for i in range(len(replacement_list)):
    	data_list[0x633+i] = replacement_list[i]
    replacement_list = list(assemble.assemble_file("patch2.asm"))
    for i in range(len(replacement_list)):
        data_list[0x5cd+i] = replacement_list[i]
    data = "".join(data_list)
    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
