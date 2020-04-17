import socket
from Crypto.Cipher import AES

def send_message(ip, port):
    key = "ScaramouchFandan"
    iv = "\x88\xf3\x11\x77\x79\x02\x25\xc0\x37\xee\x12\x55\xa9\xdd\xf3\x22"
    mode = AES.MODE_CBC
    text = "I love you"


    length = 16 - (len(text) % 16)
    padded_text = text + chr(length)*length 
    aes = AES.new(key, mode, iv)
    encrypted_text = aes.encrypt(padded_text)

    connection = socket.socket()
    try:
        connection.connect((ip, port))
        connection.send(encrypted_text)
    finally:
        connection.close()


def main():
    send_message('127.0.0.1', 1984)


if __name__ == '__main__':
    main()
