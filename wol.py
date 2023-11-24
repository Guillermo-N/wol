#!/usr/bin/env python3

import socket
import binascii
import sys

def send_magic_packet(mac_address):
    mac_bytes = binascii.unhexlify(mac_address.replace(":", ""))
    magic_packet = b"\xFF" * 6 + mac_bytes * 16
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <MAC_address>".format(sys.argv[0]))
        sys.exit(1)
    
    mac_address = sys.argv[1]
    print("Waking up: {mac_address}")
    send_magic_packet(mac_address)
