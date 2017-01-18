from django.contrib import admin
from .models import Packet

class PacketAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'title', 'target', 'src','dst','dstport'] 

admin.site.register(Packet, PacketAdmin)
