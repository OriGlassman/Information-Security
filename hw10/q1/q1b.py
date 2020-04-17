import time
from scapy.all import *


WINDOW       = 60
MAX_ATTEMPTS = 15

LAST_ARRIVAL_INDEX  = 1
NUMBER_OF_SYN_INDEX = 0
SYN                 = 2

# Initialize your data structures here
# TODO: Initialize your data structures


blocked = set()  # We keep blocked IPs in this set

not_blocked_dict = {} # of the form { "ip":[counter, time] }
def on_packet(packet):
    def garbage_collector(time):
        delete_ips = []
        for ip in not_blocked_dict.keys():
            if (time - not_blocked_dict[ip][LAST_ARRIVAL_INDEX] > WINDOW):
                delete_ips.append(ip)
        for ip in delete_ips:
            del not_blocked_dict[ip]


    if TCP in packet and IP in packet:
        src_ip = str(packet[IP].src)
        if packet[TCP].flags == SYN:
            if src_ip in blocked:
                return
            if (src_ip in not_blocked_dict):
                new_amount_of_packet = not_blocked_dict[src_ip][NUMBER_OF_SYN_INDEX] + 1
                current_time = time.time()

                if (new_amount_of_packet > MAX_ATTEMPTS) and (current_time - not_blocked_dict[src_ip][LAST_ARRIVAL_INDEX] <= WINDOW) :
                    block(src_ip)
                    del not_blocked_dict[src_ip] 
                else:
                    if current_time - not_blocked_dict[src_ip][LAST_ARRIVAL_INDEX] > WINDOW: # shouldn't enter here - just in case.
                        not_blocked_dict[src_ip] = [1, current_time]
                    else:
                        not_blocked_dict[src_ip]  = [new_amount_of_packet, current_time]
                    garbage_collector(current_time)
                

            else: # first time
                not_blocked_dict[src_ip] = [1, time.time()]




def generate_block_command(ip):
    """Generate a command that when executed in the shell, blocks this IP.

    The blocking will be based on `iptables` and must drop all incoming traffic
    from the specified IP."""
    # TODO: Implement me
    return "iptables -A INPUT -s " + ip + " -j DROP"


def block(ip):
    os.system(generate_block_command(ip))
    blocked.add(ip)


def is_blocked(ip):
    return ip in blocked


def main():
    sniff(prn=on_packet)


if __name__ == '__main__':
    main()
