import array
from netaddr import *
import ipaddress

net_addr=[]

def main():
     global nw_input,a,c, subnet_address,host_input,z	
     print(" CLASS B NETWORK ADDRESS RANGE: 128.1.0.0 - 191.255.0.0 ")
     print("---------------------------------------------------------")
     #print("Start of Multiple Subnet Calculator")
main()

while True:
	M = input("Enter Class B NETWORK ADDRESS: ")
	T = M.split('.')	
	if int(T[0]) < 192 and int(T[0]) > 128 and int(T[1]) < 256  and int(T[2]) < 256 and int(T[3]) < 256:
		 nw_input=M
		 #print("IP in range")
		 break
	else:
		 print('IP not in CLASS B Range')
 

def subnetmask_calculator():
	global c,b,a, subnet_address,nw_input,host_input,z  
	host_array = array.array('f',[])
	host_input = int(input("Enter number of hosts per subnet:" ))

	if host_input > 2**16:
		print ('Host address out of range, host count should be less than 65536')
		host_input = int(input("Enter number of hosts per subnet:" ))

	else: 
		pass

	for power_2 in range (16):
		total_hosts = 2**power_2
		host_array.append(total_hosts)

		
		if (host_input) < total_hosts:
			hostbits=power_2
			subnet_mask = int(32-hostbits)
			subnet_address = ("%s/%s")%(nw_input,subnet_mask)
			
			if len(net_addr)==0:

			    a= IPNetwork(subnet_address)
				#a=nw_input
				print(a)
				
				b=a.network
			#print(b)

				c= a.broadcast
				c=str(ipaddress.IPv4Address(c)).split("/")[0]
			#print(c)
				print("Subnet address as per requiremnt: %s"%subnet_address)
				print ("Network Address:%s"%b)
				print("Broadcast Address:%s"%c)
				net_addr.append(a+1) 
				break
			else:




		

subnetmask_calculator()



def yes_or_no(question): 
    global c, subnet_address,nw_input,host_input,z
    answer = input( question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False


while yes_or_no("Do you want to continue using the same network?"):
	z = ipaddress.IPv4Address(c) + 1
	nw_input=z
	subnetmask_calculator()


