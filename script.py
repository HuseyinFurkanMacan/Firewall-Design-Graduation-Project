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

def Add(table='filter'):
   giris = input("Enter the ip that you want to block:")
   rule = iptc.Rule()
   rule.src = giris
   target = iptc.Target(rule, "DROP")
   rule.target = target
   chain.insert_rule(rule)

def Delete(table='filter'):
   table_result=iptc.easy.flush_table(table=table,ipv6=False)
   print(table_result)

table=iptc.Table(iptc.Table.FILTER)
chain=iptc.Chain(table,"FORWARD")
iptc.Chain.set_policy(chain,policy="ACCEPT")

ans=True
while ans:
   print ("""
   0.Configurate.
   1.Block Social Media.
   2.Add a rule.
   3.Clean the Table.
   4.Print the Table.
   """)
   ans=input("What would you want to do? ")
   if ans == "0":
       Configure()
   elif ans=="1":
     print("\n Social Media Completely Blocked.")
     SocialMedia()
   elif ans=="2":
     Add()
     print("\n Rule Added.")
   elif ans=="3":
     Delete()
     print("\n Table Cleaned.")

   elif ans=="4":
     View()
   elif ans !="":
     print("\n Not Valid Choice Try again")