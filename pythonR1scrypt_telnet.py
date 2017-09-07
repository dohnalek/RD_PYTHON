import getpass
import sys
import telnetlib

HOST = "10.130.123.1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

#tn.write("enable\n")
#tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int lo 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("sh ip int brief\n")
tn.write("exit\n")

print tn.read_all()
