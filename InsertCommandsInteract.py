class InsertCommandsInteract:
    
    def __init__(self, connection, sourceFile):
        print "criando insert"
        self.connection = connection
        self.sourceFile = sourceFile
        
    def putCommands(self):
        print "executando insert"
        print self.sourceFile
        #time.sleep(self.wait) 
        commands = self.sourceFile
        
        for comm in commands:
            self.connection.write(comm + "\n")
            a = True
            while a == True:
                output2 = self.connection.read_very_eager()            
                print output2
                yesNo = raw_input("YES para continuar leitura, NO para cancelar o comando: ") 
                yesNo = yesNo.upper()
                if (yesNo == 'NO'):
                    a = False
            self.connection.write('\x03' + "\n") 
            self.connection.write('\x03' + "\n") 
            time.sleep(2)
            output2 = self.connection.read_very_eager()            
            print output2
