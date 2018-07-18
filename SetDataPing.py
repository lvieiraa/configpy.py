class SetData():
    def __init__(self, connection, vendor, iD, vlan ):
        self.connection = connection
        self.vendor = vendor
        self.iD = iD
        self.vlan = vlan
    
    def setIp(self):
        
        ipAddress = "10.21.33.1"
        if (self.iD == 2):
            ipAddress = "10.21.33.2"
              
        if (self.vendor == "DATACOM"):
            #rotina DM
            sourceFile = ["configure", "interface vlan " + self.vlan, "ip address " + ipAddress + "/30", "end"]
            insert = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insert.putCommands()
            
        elif(self.vendor == "RAISECOMM"):          
            #rotina RS
            sourceFile = ["config", "interface ip 5 ", "ip address " + ipAddress +  " 255.255.255.252 " + self.vlan, "end"]
            insert = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insert.putCommands()
            
        elif(self.vendor == "EXTREME"):          
            #rotina RS
            sourceFile = ["configure vlan " + self.vlan + " ipaddres " + ipAddress + " 255.255.255.252"]
            insert = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insert.putCommands()
            
    def ping(self):
        
        nCount =  raw_input("Repeticoes do ping: ")
        ipDest = "10.21.33.2"
        if (self.iD == 2):
            ipDest = "10.21.33.1"
            
        sourceFile = ["ping " + ipDest + " count " + nCount]
        insertPing = InsertCommandsInteract(
                connection = self.connection,
                sourceFile = sourceFile,

            )
        insertPing.putCommands()
    
    def unsetIp(self):
        ipAddress = "10.21.33.1"
        if (self.iD == 2):
            ipAddress = "10.21.33.2"
   
        if (self.vendor == "DATACOM"):
            #rotina DM
            sourceFile = ["configure", "interface vlan " + self.vlan, "no ip address "]
            insertUnset = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insertUnset.putCommands()
         
        elif(self.vendor == "RAISECOMM"):
            #rotina RS
            sourceFile = ["config", "interface ip 5 ", "no ip address " + ipAddress]
            insertUnset = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insertUnset.putCommands()
            
        elif(self.vendor == "EXTREME"):
            #rotina RS
            sourceFile = ["unconfigure vlan " + self.vlan + " ipaddress"]
            insertUnset = InsertCommands(
                connection = self.connection,
                sourceFile = sourceFile,
                wait = 4
            )
            insertUnset.putCommands()
        
