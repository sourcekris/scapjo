#!/usr/bin/python

import os
import django
import datetime
from scapy.all import *

# setup django environ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scapjo.settings")
django.setup()
from packetstore.models import Packet # Django Packet model
from scapjo.settings import MEDIA_ROOT

targets = {31337 : "echo", 22 : "ssh", 21 : "ftp" }
protos  = {6: "TCP", 17 : "UDP", 1:"ICMP" }

debug = True

def hd(src, length=16):
    FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
    lines = []
    for c in xrange(0, len(src), length):
        chars = src[c:c+length]
        hex = ' '.join(["%02x" % ord(x) for x in chars])
        printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or '.') for x in chars])
        lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
    return ''.join(lines)

#
# Stores the packet data in the Djago DB
def store_packet(pkt):
    if debug: print pkt.getlayer(IP).proto
    wrpcap(MEDIA_ROOT + "temp.pcap",pkt)
    p = Packet(title='Captured Packet', 
               timestamp=datetime.fromtimestamp(pkt.time).strftime("%Y-%m-%d %H:%M:%S.%f"),  
               src=pkt.getlayer(IP).src,
               dst=pkt.getlayer(IP).dst,
               srcport=pkt.sport,
               dstport=pkt.dport,
               packetdata=hd(str(pkt)))

    p.pcap.name = "temp.pcap"
    try:
        p.target=targets[pkt.dport],
    except KeyError:
        p.target="return traffic"

    #try:
    p.protocol = protos[pkt.getlayer(IP).proto]
    #except KeyError:
    #    p.protocol="IP"

    p.save()

# setup django
# wait for a syn packet
sniff(filter="port 31337", prn=store_packet, store=0)
