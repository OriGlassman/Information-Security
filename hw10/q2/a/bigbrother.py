from scapy.all import *


LOVE = 'love'
unpersons = set()


def spy(packet):
    """Check for love packets.

    For each packet containing the word 'love', add the sender's IP to the
    `unpersons` set.
    """
    # TODO: Implement me (question 2a)
    if Raw in packet:
    	if "love" in repr(packet[Raw].load):
    		unpersons.add(str(packet[IP].src))


def main():
    sniff(prn=spy)


if __name__ == '__main__':
    main()
