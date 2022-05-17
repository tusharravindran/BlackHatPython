#!/usr/bin/python3

import sys

from scapy.all import *

source = “192.168.21.1”

destination = “192.168.1.23”

packet = IP(src=source, dst=destination) / ICMP()

resp = send(packet)

if resp:

    resp.show()
