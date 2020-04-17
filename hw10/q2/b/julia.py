import socket
from Crypto.Cipher import AES

def receive_message(port):
    key = "ScaramouchFandan"
    iv = "\x88\xf3\x11\x77\x79\x02\x25\xc0\x37\xee\x12\x55\xa9\xdd\xf3\x22"
    mode = AES.MODE_CBC
    aes = AES.new(key, mode, iv)

    listener = socket.socket()
    try:
        listener.bind(('', port))
        listener.listen(1)
        connection, address = listener.accept()
        try:
            encrypted_text = connection.recv(1024)
            padded_text = aes.decrypt(encrypted_text)
            return padded_text[:-ord(padded_text[-1])]

        finally:
            connection.close()
    finally:
        listener.close()


def main():
    message = receive_message(1984)
    print('received: %s' % message)


if __name__ == '__main__':
    main()
