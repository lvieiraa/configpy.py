class DiscoverVendor:
   
    def __init__(self, connection):
        self.connection = connection
        
        
    def vendor(self):
        wait = 4
        
        time.sleep(wait)  
        
        self.connection.write("show version" + "\n")
        time.sleep(wait)
        self.connection.write("show system" + "\n")
        time.sleep(wait)
        self.connection.write("display version" + "\n")
        time.sleep(wait)
        
        output = self.connection.expect(['DmSwitc|DM','RAX711|ISCOM','EXOS|extreme'])
       
        device_vendor = False
        if (output[0] == 0):
            device_vendor = "DATACOM"  
            print "DATACOM"
        elif (output[0] == 1):
            device_vendor = "RAISECOMM"
            print "RAISECOMM"
        elif (output[0] == 2):
            device_vendor = "EXTREME"
            print "EXTREME"
        else:
            device_vendor = "NotDefined"
        return device_vendor    
