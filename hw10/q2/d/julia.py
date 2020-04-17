from scapy.all import *
import socket


msg_bits = ""
index_seen = []

def receive_message(port):
    global msg_bits
    BYTE_SIZE = 8

    def stop_sniffing_cond(packet):
        global msg_bits
        global index_seen

        if (packet[TCP].seq not in index_seen) and (packet[TCP].dport == 65000):  
            index_seen.append(packet[TCP].seq)
            msg_bits += "{0:03b}".format(packet[TCP].reserved)

        return True if (packet[TCP].ack == packet[TCP].seq)  else False

        

    sniff(filter='tcp', stop_filter=stop_sniffing_cond)
    msg_bits = msg_bits[:-1]
    msg = ""
    for i in range(0, len(msg_bits), BYTE_SIZE):
        msg += chr(int(msg_bits[i:i+BYTE_SIZE], 2))

    return msg

def main():
    message = receive_message(65000)
    print('received: %s' % message)


if __name__ == '__main__':
    main()
