def check_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    key = 0xA2
    for i in range(2,ord(data[0])+2):
    	if i>=len(data):
            continue;
    	key = key ^ ord(data[i])
    if key==ord(data[1]):
    	return True
    return False


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
