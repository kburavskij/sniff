import pyshark
import ipinfo
import ipaddress
from datetime import datetime
import json
import os

# file = 'server/captures/' + 'output' + str(datetime.now().strftime("%H:%M:%S")) + '.cap'
def sniffPack():
    access_token = '8f2a068b0e4e27'
    file = os.path.dirname(os.path.abspath(__file__)) + '/captures/output.pcap'
    output = open(file, "w")

    handler = ipinfo.getHandler(access_token)
    cap = pyshark.LiveCapture(interface='en0', output_file=file, display_filter='ip && !(ip.dst==10.0.0.0/8) && !(ip.dst==192.168.0.0/16) && ip.version == 4')
    print(datetime.now().strftime("%H:%M:%S"))

    cap.sniff(timeout=30)

    print(cap)

    thisdict =	{}
    print(thisdict)
    print('Just arrived:', len(cap))

    for packet in cap.sniff_continuously(packet_count=len(cap)):
        try:
            if(packet.ip.src and not ipaddress.ip_address(packet.ip.src).is_private):
                # print('Just arrived:', packet)
                # print('IP src:', packet.ip.src)
                details = handler.getDetails(packet.ip.src)
                # print('IP src city:', details.city)
                # print('IP src latitude:', details.latitude)
                # print('IP src longitude:', details.longitude)
                thisdict[packet.ip.src] = [details.latitude, details.longitude]
        except AttributeError as e:
            pass

        try:
            if(packet.ip.dst and not ipaddress.ip_address(packet.ip.dst).is_private):
                # print('IP dst:', packet.ip.dst)
                details = handler.getDetails(packet.ip.dst)
                # print('IP dst city:', details.city)
                # print('IP dst latitude:', details.latitude)
                # print('IP dst longitude:', details.longitude)
                thisdict[packet.ip.dst] = [details.latitude, details.longitude]
        except AttributeError as e:
            pass

    print(thisdict)
    json_object = json.dumps(thisdict, indent = 4)  
    output.close()

    return json_object
