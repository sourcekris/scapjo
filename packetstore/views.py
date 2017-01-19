from django.shortcuts import render
from django.http import Http404

from packetstore.models import Packet

def index(request):
    if Packet.objects.count() > 20:
        packets = Packet.objects.all()[Packet.objects.count()-21:Packet.objects.count()-1]
    else:
        packets = Packet.objects.all()

    return render(request, 'packetstore/index.html', {'packets':packets})

def packet_details(request, id):
    try:
        packet = Packet.objects.get(id=id)
    except Packet.DoesNotExist:
        raise Http404('Packet not found.')

    return render(request, 'packetstore/packet_details.html', {'packet':packet})

def no_return_traffic(request):
    packets = Packet.objects.exclude(target='return traffic')
    return render(request, 'packetstore/index.html', {'packets':packets})
