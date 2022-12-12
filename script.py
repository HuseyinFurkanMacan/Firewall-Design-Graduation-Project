import iptc
import os
import sys

def Configure():
   os.system("ifup br0")
   os.system("modprobe br_netfilter")
   os.system("echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables")
   os.system("echo 'net.bridge.bridge-nf-call-iptables=1' >> /etc/sysctl.conf")