from scapy.all import *



def send_message(ip, port):
    try:
        bits_msg = "".join("{0:08b}".format(ord(x), 'b') for x in "I love you")
        index_l = 0
        index_r = 3
        seq = 0
        while index_r <= 81:
        	if index_r == 81:
        		reserved_bits = int(bits_msg[-2:] + "0", 2)
        	else:
				reserved_bits = int(bits_msg[index_l:index_r],2)

        	scapy_packet = IP(dst=ip) / TCP(dport=port, reserved=reserved_bits, seq=seq, ack=26, flags="SA")
        	send(scapy_packet)
        	index_r += 3
        	index_l += 3
        	seq += 1
        
    finally:
        return


def main():
    send_message('127.0.0.1', 65000)


if __name__ == '__main__':
    main()
