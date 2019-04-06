# run this code in Python3
# input - getting input from the user
# the input() function prompts the user to enter a value.

# Example
# age = input(" What is your age ")
# Result
# What is your age?
# the Variable age will hold the value of the user input

# old code
# interface = " eth0 "
# new_mac = " 00:11:11:22:33:44 "
# shell=True


import subprocess

interface = input(" interface > ")

# interface = " eth0 "
new_mac = input("new MAC > ")
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


