#Packet sniffer in python
#Developed for Socket IPC debugging specifically on the Raspberry Pi 
#Modified from examples found @ https://www.binarytides.com/python-packet-sniffer-code-linux
#Tim Rossiter
#May 13 2019
#rosstimo@isu.edu
#https://www.isu.edu/robotics/

import socket, sys
from struct import *

def getPacket () :
	packet = s.recvfrom(65565)
	return packet[0]

def ethernetHeader (packet) :
	eth_length = 14
	return packet[:eth_length]
	
def ethernetProtocol (eth_header) :
	eth = unpack('!6s6sH' , eth_header)
	return socket.ntohs(eth[2])

def destinationMAC (eth_header) :
	return str(mac_addr(packet[0:6])) 
	
def sourceMAC (eth_header) :
	return str(mac_addr(packet[6:12])) 
		
#make MAC address readable
def mac_addr (a) :
  sObject = slice(2, 4)
  MAC = ''
  for i in range(6):
	  hexDigits = str(hex(ord(a[i])))
	  MAC += hexDigits[sObject]
	  if i < 5:
		  MAC += ':'
  return MAC
  
#create an AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()



while True:
	
	packet = getPacket()
	packetHeader = ethernetHeader(packet)
	eth_protocol = ethernetProtocol(packetHeader)
	
	print 'Destination MAC: ' + destinationMAC(packetHeader)
	print 'Source MAC: ' + sourceMAC(packetHeader)
	print 'Protocol : ' + str(ethernetProtocol(packetHeader))
	print
	#break
	
	
	#Parse IP packets, IP Protocol number = 8
	if eth_protocol == 8 :
		#Parse IP header
		#take first 20 characters for the ip header
		ip_header = packet[eth_length:20+eth_length]
		#print 'Tim says length of icmp_header is:' + str(len(ip_header))
		#now unpack them :)
		
		iph = unpack('!BBHHHBBH4s4s' , ip_header)

		version_ihl = iph[0]
		version = version_ihl
		ihl = version_ihl + 0xf #'&' # 0xF
		iph_length = ihl * 4
		ttl = iph[5]
		protocol = iph[6]
		s_addr = socket.inet_ntoa(iph[8]);
		d_addr = socket.inet_ntoa(iph[9]);
		#print s_addr, d_addr
		#if d_addr == '127.0.0.1':
		print 'Version: ' + str(version)
		print 'IP Header Length: ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol)
		print 'Source Address : ' + str(s_addr) 
		print 'Destination Address : ' + str(d_addr)
		print 
	
		#TCP protocol
		if protocol == 6 :
			t = iph_length + eth_length
			tcp_header = packet[t:t+20]
			#now unpack them :)
			if len(tcp_header) > 20 :
				tcph = unpack('!HHLLBBHHH' , tcp_header)

				source_port = tcph[0]
				dest_port = tcph[1]
				sequence = tcph[2]
				acknowledgement = tcph[3]
				doff_reserved = tcph[4]
				tcph_length = doff_reserved #'>> 4'

				print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)

				h_size = eth_length + iph_length + tcph_length * 4
				data_size = len(packet) - h_size

				#get data from the packet
				data = packet[h_size:]

				print 'Data : ' + data			


		

				
		'''
				#ICMP Packets
				elif protocol == 1 :
					break
					u = iph_length + eth_length
					icmph_length = 4
					icmp_header = packet[u:u+4]
					print 'Tim says length of icmp_header is:' + str(len(icmp_header))
					#now unpack them :)
					icmph = unpack('!BBH' , icmp_header)

					icmp_type = icmph[0]
					code = icmph[1]
					checksum = icmph[2]

					print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)

					h_size = eth_length + iph_length + icmph_length
					data_size = len(packet) - h_size

					#get data from the packet
					data = packet[h_size:]

					print 'Data : ' + data

				#UDP packets
				elif protocol == 17 :
					break
					u = iph_length + eth_length
					udph_length = 8
					udp_header = packet[u:u+8]
					print 'Tim says length of udp_header is:' + str(len(udp_header))
					#now unpack them :)
					udph = unpack('!HHHH' , udp_header)

					source_port = udph[0]
					dest_port = udph[1]
					length = udph[2]
					checksum = udph[3]

					print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)

					h_size = eth_length + iph_length + udph_length
					data_size = len(packet) - h_size

					#get data from the packet
					data = packet[h_size:]

					print 'Data : ' + data

				#some other IP packet like IGMP
				else :
					print 'Protocol other than TCP/UDP/ICMP'
				
				print
		'''

	
