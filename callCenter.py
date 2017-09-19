class call(object):
    def __init__(self,CallerId, callerName, callerPhoneNumber, CallTime, reasonForCall):
        self.CallerId = CallerId 
        self.callerName = callerName
        self.callerPhoneNumber = callerPhoneNumber
        self.CallTime =CallTime
        self.reasonForCall = reasonForCall
        
    def display(self):
        print "caller id: {}".format(self.CallerId)
        print "caller name: {}".format(self.callerName)
        print "caller phone number: {}".format(self.callerPhoneNumber)
        print "caller time: {}".format(self.CallTime)
        print "reson for call: {}".format(self.reasonForCall)
        
callerOne = call("ty", "coon", 5107619837, "4:14pm", "service") 
callerOne.display()
        
class callCenter(object):
    def __init__(self, listOfCalls, QueueSize):
        self.listOfCallers = listOfCallers
        self.QueueSize = QueueSize
        
    def adds(self, call):
        self.listOfCallers.insert(call)
        self.QueueSize =+ 1
        print "list of callers: {}".format(self.listOfCallers)
        print "Queue Size: {}".format(self.QueueSize)
        
