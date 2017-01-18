# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField()),
                ('src', models.CharField(max_length=64)),
                ('dst', models.CharField(max_length=64)),
                ('srcport', models.IntegerField()),
                ('dstport', models.IntegerField()),
                ('protocol', models.CharField(max_length=5, choices=[(b'UDP', b'UDP Protocol'), (b'TCP', b'TCP Protocol'), (b'ICMP', b'ICMP Protocol'), (b'IP', b'IP / Other')])),
                ('pcap', models.FileField(upload_to=b'')),
                ('target', models.CharField(max_length=128)),
                ('packetdata', models.TextField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
