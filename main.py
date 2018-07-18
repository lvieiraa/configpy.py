import telnetlib
import time
import getpass
import re
import threading

sw1 = PingPtp (
    "lvieiranet",
    getpass.getpass("Senha: "),
    sw = raw_input("SWITCH 1 (ip ou nome): "),
    #sw = "172.17.34.208",
    vlan = raw_input("Vlan: "),
    #vlan = "471",
    ipAddress = "10.20.34.2",
    ipDest = "10.20.34.1",
    iD = 1
)

sw2 = PingPtp (
    "lvieiranet",
     getpass.getpass("Senha: "),
    sw = raw_input("SWITCH 2 (ip ou nome): "),
    #sw = "172.17.3.7",
    vlan = raw_input("Vlan: "),
    #vlan = "471",
    ipAddress = "10.20.34.1",
    ipDest = "10.20.34.2",
    iD = 2
)


#devices = [sw1, sw2]
#procs = []
#for a_device in devices:
#    my_thread = threading.Thread(target=a_device.connect)
#    my_thread.start()
#    
#main_thread = threading.currentThread()
#for some_thread in threading.enumerate():
#    if some_thread != main_thread:
#        print(some_thread)
#        some_thread.join()

        
sw1.connect() 
sw1.setIp()

sw2.connect() 
sw2.setIp()

sw1.setPing() 
sw2.setPing()

sw1.unsetIp() 
sw2.unsetIp()
