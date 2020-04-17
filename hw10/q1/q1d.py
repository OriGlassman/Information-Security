from scapy.all import *

SYN_ACK = 18
SYN 	= 2
def on_packet(packet):
    """Implement this to send a SYN ACK packet for every SYN."""
    # TODO: Implement me
    # WARNING: Use only the `send` function from scapy to send the packet. Do
    #          not use any other function to send/receive packets.
    if (IP in packet) and (TCP in packet) and (packet[TCP].flags == SYN):
    	spoof_open_port_packet = IP(dst=packet[IP].src) / TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags=SYN_ACK, ack=packet[TCP].seq + 1)
    	send(spoof_open_port_packet)


def main(argv):
    sniff(prn=on_packet)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

