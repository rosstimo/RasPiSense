#Packet sniffer in python
#For Linux - Sniffs all incoming and outgoing packets :)
#Silver Moon (m00n.silv3r@gmail.com)
#https://www.binarytides.com/python-packet-sniffer-code-linux/
import socket, sys
from struct import *

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
	sObject = slice(2, 4)
	MAC = ''
	for i in range(6):
	  hexDigits = str(hex(ord(a[i])))
	  MAC += hexDigits[sObject]
	  if i < 5:
		  MAC += ':'
	#print MAC
	return MAC
  
def hData (d) :
	dataLength = len(d)
	hexData = '\n'
	sObject = slice(2, 4)
	columnNum = 0
	for i in range(dataLength):
		hexByte = hex(ord(d[i]))
		hexDigits = str(hexByte)
		byteString = hexDigits[sObject]
		if len(byteString) == 1:
			byteString = '0' + byteString
		hexData += byteString + ' '
		columnNum += 1
		if columnNum == 32 :
			hexData +=  '\n'
			columnNum = 0
	#print hexData + '\n'
	return hexData
	
def rawData (d):
	dataLength = len(d)
	rawData = '\n'
	columnNum = 0
	for i in range(dataLength):
		rawByte = str(d[i])
		rawData += rawByte
		columnNum += 1
		if columnNum == 32 :
			rawData +=  '\n'
			columnNum = 0
	#print rawData + '\n'
	return rawData

	
#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet
while True:
	packet = s.recvfrom(65565)

	#packet string from tuple
	packet = packet[0]

	#parse ethernet header
	eth_length = 14
	eth_header = packet[:eth_length]
	eth = unpack('!6s6sH' , eth_header)
	eth_protocol = socket.ntohs(eth[2])
	#print 'Destination MAC : ' + str(eth_addr(packet[0:6])) + ' Source MAC : ' + str(eth_addr(packet[6:12])) + ' Protocol : ' + str(eth_protocol)

	#Parse IP packets, IP Protocol number = 8
	if eth_protocol == 8 :
		#Parse IP header
		#take first 20 characters for the ip header
		ip_header = packet[eth_length:20+eth_length]
		#now unpack them :)
		iph = unpack('!BBHHHBBH4s4s' , ip_header)
		version_ihl = iph[0]
		version = version_ihl >> 4
		ihl = version_ihl & 0xf 
		iph_length = ihl * 4
		#print str(iph_length)
		ttl = iph[5]
		protocol = iph[6]
		s_addr = socket.inet_ntoa(iph[8]);
		d_addr = socket.inet_ntoa(iph[9]);
		#print s_addr, d_addr
		if d_addr == '127.0.0.1':
			#print 'Destination MAC : ' + str(eth_addr(packet[0:6])) + ' Source MAC : ' + str(eth_addr(packet[6:12])) + ' Protocol : ' + str(eth_protocol)
			#print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) 
			#print ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
			
			#TCP protocol
			if protocol == 6 :
				t = iph_length + eth_length
				tcp_header = packet[t:t+20]
				#now unpack them :)
				if len(tcp_header) == 20 :
					tcph = unpack('!HHLLBBHHH' , tcp_header)

					source_port = tcph[0]
					dest_port = tcph[1]
					sequence = tcph[2]
					acknowledgement = tcph[3]
					doff_reserved = tcph[4]
					tcph_length = doff_reserved >> 4
					#print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port)
					#print ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
					h_size = eth_length + iph_length + tcph_length * 4
					data_size = len(packet) - h_size

					#get data from the packet
					data = packet[h_size:]
					#TODO if len(data) != 0 print stuff
					if len(data) > 0:
						print '*******************************'
						print 'Destination MAC : ' + str(eth_addr(packet[0:6])) + ' Source MAC : ' + str(eth_addr(packet[6:12])) + ' Protocol : ' + str(eth_protocol)
						print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) 
						print 'Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
						print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port)
						print 'Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
						print 'Data : '  + hData(data) + rawData(data)	
						print len(data)
						print '*******************************'
					#break

			#ICMP Packets
			elif protocol == 1 :
				u = iph_length + eth_length
				icmph_length = 4
				icmp_header = packet[u:u+4]
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

				print 'Data : ' + hData(data) + rawData(data)	

			#UDP packets
			elif protocol == 17 :
				u = iph_length + eth_length
				udph_length = 8
				udp_header = packet[u:u+8]
				#now unpack them :)
				if len(udp_header) == 8 :
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

					print 'Data : ' + hData(data) + rawData(data)	

			#some other IP packet like IGMP
			else :
				print str(protocol) + ' Protocol other than TCP/UDP/ICMP'
				
			print
			
