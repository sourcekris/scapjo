from django.db import models

# Fields we care about should be:
#   - IPv4 source, destionation and ports
#   - Transport protocol
#   - Data (hexencoded)
#   - Description
#   - Target service name
#   - Some title
class Packet(models.Model):
    PROTOCOL_CHOICES = (
        ('UDP', 'UDP Protocol'),
        ('TCP', 'TCP Protocol'),
        ('ICMP', 'ICMP Protocol'),
        ('IP', 'IP / Other'),
    )
    title = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    src = models.CharField(max_length=64)
    dst = models.CharField(max_length=64)
    srcport = models.IntegerField()
    dstport = models.IntegerField()
    protocol = models.CharField(max_length=5, choices=PROTOCOL_CHOICES)
    pcap = models.FileField()
    target = models.CharField(max_length=128)
    packetdata = models.TextField()
    description = models.TextField(blank=True)
    
