import getpass
import paramiko
import time

#Ask for username and password 
ip_address = open("myswitchip")
username = raw_input("Enter your username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for line in ip_address:
        print " Getting show ip interface brief " + (line)
        HOST = line.strip()
	ssh_client.connect(hostname=HOST,username=username,password=password)

	print "Successful connection" , ip_address 

	remote_connection = ssh_client.invoke_shell()

	remote_connection.send("sh ip int brief\n")
	remote_connection.send("exit\n")

	time.sleep(2)
	output = remote_connection.recv(65535)
	saveoutput = open("show_int_" + HOST, "w")
	saveoutput.write(output)
	saveoutput.close

	output = output.split('\n')
	for line in output:
		if 'interface' in line:
			print(line,'\n')
#		if 'PID' in line:
#			print(line,'\n')

