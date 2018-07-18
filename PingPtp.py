class PingPtp:
    
    
    def __init__(self, user, senha, sw,vlan, ipAddress, ipDest, iD):
        self.user = user
        self.senha = senha
        self.sw = sw    
        self.vlan = vlan
        self.ipAddress = ipAddress
        self.ipDest = ipDest
        self.iD = iD
        self.vendor = 'undefined'
        self.connection = False
        
    def connect (self):
        
        wait = 4
   
        try:
            self.connection = telnetlib.Telnet(self.sw, 23, 5)
        except Exception:
            print "host: "+ self.sw +" sem acesso\n"
            return
        
        self.connection.read_until("Login:", 5)
        self.connection.write(self.user + "\n")

        time.sleep(wait)

        self.connection.read_until("Password:", 5)
        self.connection.write(self.senha + "\n")
        
        time.sleep(wait)  
        
        disc = DiscoverVendor(self.connection)
        self.vendor = disc.vendor()      
        
    def setIp (self):
        setdata = SetData(connection = self.connection,
                          vendor = self.vendor,
                          iD = self.iD,
                          vlan = self.vlan
                         )
        setdata.setIp()
        
    def setPing (self):
        setPing = SetData(connection = self.connection,
                      vendor = self.vendor,
                      iD = self.iD,
                      vlan = self.vlan
                     )
        setPing.ping()
    
    def unsetIp (self):
        unsetData = SetData(connection = self.connection,
                          vendor = self.vendor,
                          iD = self.iD,
                          vlan = self.vlan
                         )
        unsetData.unsetIp()        
        self.connection.close()
