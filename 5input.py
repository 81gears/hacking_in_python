# parser
# python3 5input.py -i eth0 -m 00:11:11:22:33:44

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help=" Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help=" New MAC address")

# can use any name , use a useful name
(options, arguments)= parser.parse_args()


# interface = input(" interface >") 

# interface = " eth0 "
interface = options.interface
new_mac = options.new_mac
# new_mac = input("new MAC > ")
# shell = True 


print(" Changing MAC address for " + interface + " to " + new_mac )

# subprocess.call("ifconfig" + interface + "down", shell=True)
# subprocess.call("ifconfig" + interface + "hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig" + interface + "up", shell=True)

subprocess.call(["ifconfig", interface , "down"])
subprocess.call(["ifconfig", interface , "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])



# print("[+] Changing MAC address for " + interface + " to new_mac ")

# subprocess.call(" ifconfig " + interface + "down", shell=True)
# subprocess.call(" ifconfig " + interface + "hw ether " + new_mac, shell=True)
# subprocess.call(" ifconfig " + interface + "up", shell=True)


