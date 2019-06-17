#see https://en.scratch-wiki.info/wiki/Communicating_to_Scratch_via_Python
import socket 
import sys

class ScratchSensorUpdate():
        
        def __init__(self, host_ip, port, sensorName, sensorValue):
                self.host_ip = host_ip
                self.port = port
                self.sensorName = sensorName
                self.sensorValue = sensorValue
                
        def sendUpdate(self):
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        print('Socket successfully created')
                except socket.error as err:
                        print('socket creation failed with error %s" %(err)')

                try:
                        if True: #TODO test if ip and port should be set to defaults
                                host_ip = socket.gethostbyname(socket.gethostname())
                                port = 42001
                        print('the host name is: ' + self.host_ip)
                        print('the port is: ' + str(self.port))
                        # connecting to the server
                        s.connect((self.host_ip, self.port))
                        s.send(self.sensorMessage())
                        print "the socket has successfully connected to scratch on port == %s" %(host_ip)
                        s.close()
                        
                except socket.gaierror:
                        # this means could not resolve the host
                        print "there was an error resolving the host"
                        sys.exit()      

                except socket.error as err:
                        print('it looks like the server doesn\'t want to talk')
                        print(err)
                        #break
         
        def sensorMessage(self):               
                concat_message = 'sensor-update "' + self.sensorName + '" ' + str(self.sensorValue)
                #the next two line pad the begining of dummy with 3 byte of 0x00h
                n = len(concat_message)
                pad = (chr((n >> 24) & 0xFF)) + (chr((n >> 16) & 0xFF)) + (chr((n >> 8) & 0xFF)) + (chr(n & 0xFF))
                print('sending: ' + str(pad) + concat_message)      
                return(pad + concat_message)
     
if __name__ == '__main__' :
        sensorName = "mySensor"
        sensorValue = 42
        host_ip = '127.0.0.1'
        port = 42001
        testUpdate = ScratchSensorUpdate(host_ip, port, sensorName, sensorValue)
        print(testUpdate.port)
        testUpdate.sendUpdate()

