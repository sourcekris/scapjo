from django.shortcuts import render
from django.http import Http404

from packetstore.models import Packet

def index(request):
    packets = Packet.objects.all()
    return render(request, 'packetstore/index.html', {'packets':packets})

def packet_details(request, id):
    try:
        packet = Packet.objects.get(id=id)
    except Packet.DoesNotExist:
        raise Http404('Packet not found.')

    return render(request, 'packetstore/packet_details.html', {'packet':packet})

# Create your views here.
