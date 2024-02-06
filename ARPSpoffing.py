import scapy.all as scapy
import optparse

# arp request
# broadcast
# response
def user_datas():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipadress",dest="ipadress",help="please insert your want to find out ip adress !")
    parse_object.add_option("-m","--macadress",dest="macadress",help="please insert your want to find out mac adress")
    parse_object.add_option("-t","--timeout",dest="timeout",help="please insert timeout")
    return parse_object.parse_args()

def scan_network(pdst,dst,timeout=1):
    arp_request_pack=scapy.ARP(pdst=pdst)
    #scapy.ls(scapy.ARP())
    broadcast_pack=scapy.Ether(dst=dst)
    #scapy.ls(scapy.Ether())
    combine_pack=broadcast_pack/arp_request_pack
    (answered_list, unanswered_list)=(scapy.srp(combine_pack,timeout=timeout))
    #print(list((answered_list)))
    answered_list.summary()

print("Starting ARP Broadcasting !!!")
(user_data,arguments)=user_datas()
if user_data.timeout==None:
    timeout=1
else:
    timeout=int(user_data.timeout)

#print(type(user_data.timeout))
#print(timeout)

scan_network(user_data.ipadress,user_data.macadress,timeout)

print("ARP Snoff is Succesfully !!!")
