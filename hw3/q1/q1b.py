def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    key  = 0xA2
    data_list = list(data)
    for i in range(2, ord(data[0]) + 2):
        if i>=len(data):
            continue;
        key = key ^ ord(data[i])
    data_list[1] = chr(key)
    data = "".join(data_list)
    with open(path + '.fixed', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
