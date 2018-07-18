class InsertCommands:
    
    def __init__(self, connection, sourceFile, wait):
        print "criando insert"
        self.connection = connection
        self.sourceFile = sourceFile
        self.wait = wait
      
    def putCommands(self):
        print "executando insert"
        print self.sourceFile
        time.sleep(self.wait)  
        commands = self.sourceFile
             
        for comm in commands:
            self.connection.write(comm + "\n")
            time.sleep(self.wait)
        output = self.connection.read_very_eager()
        print output
        
        time.sleep(self.wait)        
