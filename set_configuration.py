import getpass
import paramiko
import time

#Ask for username and password 
ip_address = open("myswitchip")
username = raw_input("Enter your username: ")
command = open("command")
password = getpass.getpass()

#Open a file called myswitchip 
#router = open("route01")

#Telnet to switches and get the running 
#for line in f:
#	print " Getting running config from Switch " + (line)
#	HOST = line.strip()
#	tn = telnetlib.Telnet(HOST) 
#
#	tn.read_until("Username: ")
#	tn.write(user + "\n")
#	if password:
#		tn.read_until("Password: ")
#		tn.write(password + "\n")
#
#
#	tn.write("terminal lenght 0 \n")
#	tn.write("show runn\n")
#	tn.write("exit\n")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for line in ip_address:
        print " Getting running config from Switch " + (line)
        HOST = line.strip()
	ssh_client.connect(hostname=HOST,username=username,password=password)

	print "Successful connection" , ip_address 

	remote_connection = ssh_client.invoke_shell()

for line in command:
        print " Set command via CLI " + (line)
        COMMAND = line.strip()
	remote_connection.send("terminal length 0\n")
	remote_connection.send("COMMAND\n")
	remote_connection.send("exit\n")

	time.sleep(2)
	output = remote_connection.recv(65535)
	saveoutput = open("config_" + HOST, "w")
	saveoutput.write(output)
	saveoutput.close

	output = output.split('\n')
	for line in output:
		if 'hostname' in line:
			print(line,'\n')
		if 'tacacs' in line:
			print(line,'\n')


#	print output 

#	readoutput = tn.read_all()
#	saveoutput = open("switch" + HOST, "w")
#	saveoutput.write(readoutput)
#	saveoutput.close 




