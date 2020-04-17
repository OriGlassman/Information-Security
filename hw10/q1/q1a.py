from scapy.all import *


OPEN = 'open'
CLOSED = 'closed'
FILTERED = 'filtered'


def generate_syn_packets(ip, ports):
    """Returns a list of TCP SYN packets, to perform a SYN scan on the given
       TCP ports."""
    # TODO: Implement me
    packets_list = []
    for port in ports:
    	syn_packet_for_specific_port = IP(dst=ip) / TCP(dport=port, flags='S')
    	packets_list.append(syn_packet_for_specific_port)

    return packets_list


def analyze_scan(ip, ports, answered, unanswered):
    """Analyze the results from `sr` of SYN packets.
    
    This function returns a dictionary from port number, to
    'open' / 'closed' / 'filtered', based on the answered and unanswered packets
    return from `sr`.
    """
    results = {}
    filtered = {}
    opened = {}
    closed = {}
    SYN_ACK = 18
    SYN_RESET = 20
    for packet in answered:
    	if packet[1][TCP].flags == SYN_ACK:
    		opened[packet[0][TCP].dport] = 'open'
    	elif packet[1][TCP].flags == SYN_RESET:
    		closed[packet[0][TCP].dport] = 'closed'
    for packet in unanswered:
    	filtered[packet[TCP].dport] = 'filtered'
    results.update(opened)
    results.update(filtered)
    results.update(closed)
    return results
    

def stealth_syn_scan(ip, ports, timeout):
    # WARNING: DO NOT MODIFY THIS FUNCTION
    packets = generate_syn_packets(ip, ports)
    answered, unanswered = sr(packets, timeout=timeout)
    return analyze_scan(ip, ports, answered, unanswered)


def main(argv):
    # WARNING: DO NOT MODIFY THIS FUNCTION
    if not 3 <= len(argv) <= 4:
        print('USAGE: %s <ip> <ports> [timeout]' % argv[0])
        return 1
    ip    = argv[1]
    ports = [int(port) for port in argv[2].split(',')]
    if len(argv) == 4:
        timeout = int(argv[3])
    else:
        timeout = 5
    results = stealth_syn_scan(ip, ports, timeout)
    for port, result in results.items():
        print('port %d is %s' % (port, result))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
