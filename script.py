import iptc
import os
import sys

def Configure():
   os.system("ifup br0")
   os.system("modprobe br_netfilter")
   os.system("echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables")
   os.system("echo 'net.bridge.bridge-nf-call-iptables=1' >> /etc/sysctl.conf")

def View(table='filter'):
   table_result=iptc.easy.dump_table(table=table, ipv6=False)
   print(table_result)

def SocialMedia(table='filter'):
   rule = iptc.Rule()
   target = iptc.Target(rule, "DROP")
   rule.target = target

   #Facebook
   rule.src = "157.240.238.35"
   chain.insert_rule(rule)

   #Instagram
   rule.src = "157.240.238.174"
   chain.insert_rule(rule)