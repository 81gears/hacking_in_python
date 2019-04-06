# parser
# python3 6function.py -i eth0 -m 00:11:11:22:33:44

# Function is a block of code you give a Name to , so you can use it again.
# Calling a functions Name runs the entire block of code.


import subprocess
import optparse

def change_mac(interface, new_mac):
    print(" Changing MAC address for " + interface + " to " + new_mac )
    
    subprocess.call(["ifconfig", interface , "down"])
    subprocess.call(["ifconfig", interface , "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help=" Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help=" New MAC address")

# can use any name , use a useful name
(options, arguments)= parser.parse_args()

change_mac(options.interface, options.new_mac)


#________________________________________

# old code below 

# interface = input(" interface >") 

# interface = " eth0 "
# interface = options.interface
# new_mac = options.new_mac

# new_mac = input("new MAC > ")
# shell = True 


# print(" Changing MAC address for " + interface + " to " + new_mac )



# subprocess.call(["ifconfig", interface , "down"])
# subprocess.call(["ifconfig", interface , "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])





