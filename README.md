# ScapJo

##### Author: Kris Hunt
##### Version: 0.0

Combine Scapy and Django for capturing and replaying exploits in attack defense CTF scenarios. 

Current status, work in progress, nothing functional yet.

The idea is that a Python Scapy system will be collecting data regarding packets seen targeting the services you're defending on your server in an attack defense CTF. 

The Web UI will provide an overview of the metadata, hexdump of the exploit payload, extraction of strings, disassembly of shellcode and so on.

You should be able to modify and replay exploits at the click of a button, scroll back to see historical incoming exploits, diff exploits to find how incoming exploits change over time and so on.

Additionally, generation of bogus outgoing exploit payloads for replay by Scapy is also a target feature. To provide air cover for any actual exploit attempts your team might be making.

