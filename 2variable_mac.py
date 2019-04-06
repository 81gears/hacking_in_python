# using a Variable
# a Variable is a lable for a Value you want to use in your program.

# Variable names in Python follow two main  rules:

# They must contain only letters, underscores, and numbers.
# They must start with a letter or underscore.

# a Variable canhold a small piece of information,or it can hold many gigabytes of data.



import subprocess

interface = " eth0 "
new_mac = " 00:11:11:22:33:44 "
shell=True

# what is a String?
# a string is a value made up of one or more characters,
# surrounded by single or double quotes.

print("[+] Changing MAC address for " + interface + " to new_mac ")

subprocess.call(" ifconfig " + interface + "down", shell=True)
subprocess.call(" ifconfig " + interface + "hw ether " + new_mac, shell=True)
subprocess.call(" ifconfig " + interface + "up", shell=True)
