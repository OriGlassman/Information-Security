import math
from scapy.all import *


LOVE = 'love'
unpersons = set()


def spy(packet):
    """Check for love packets and encrypted packets.

    For each packet containing the word 'love' (or a packet which is encrypted),
    add the sender's IP to the `unpersons` set.
    """
    # TODO: Implement me (question 2c)
    if Raw in packet:
        if ("love" in repr(packet[Raw].load)) or (entropy(str(repr(packet[Raw].load))) > 3):
            unpersons.add(str(packet[IP].src))



def entropy(string):
    distribution = [float(string.count(c)) / len(string)
                    for c in set(string)]
    return -sum(p * math.log(p) / math.log(2.0) for p in distribution)


def main():
    sniff(prn=spy)


if __name__ == '__main__':
    main()
