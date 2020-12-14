import Participant
import Log

class Queue:
    def __init__(self,name,queue_id):
        self.name = name
        self.queue_id = queue_id
        self.queue = []
        self.VIPqueue=[]
        self.isLock = False
        self.Log = Log()
    
    def getQueueName(self):
        self.Log.logcontent(self.queue_id+": Queue.getQueueName() complete")
        return self.name
    
    def getQueueid(self):
        self.Log.logcontent(self.queue_id+": Queue.getQueueid() complete")
        return self.queue_id
    
    def addUser(self,user):
        self.Log.logcontent(self.queue_id+": Queue.addUser({0})".format(user))
        if(not self.isLock):
            self.queue.append(user)
            self.Log.logcontent(self.queue_id+": Queue.addUser({0}) complete".format(user))
            return True
        else:
            self.Log.logcontent(self.queue_id+": Queue.addUser({0}) error".format(user))
            return False
    
    def removeUser(self,user):
        self.Log.logcontent(self.queue_id+": Queue.removeUser({0})".format(user))
        if(not self.isLock):
            self.queue.remove(user)
            self.Log.logcontent(self.queue_id+": Queue.removeUser({0}) complete".format(user))
            return True
        else:
            self.Log.logcontent(self.queue_id+": Queue.removeUser({0}) error".format(user))
            return False
    
    def popFirstUser(self):
        self.Log.logcontent(self.queue_id+": Queue.popFirstUser()")
        if (not self.isLock):
            self.Log.logcontent(self.queue_id+": Queue.popFirstUser() complete")
            return self.queue.pop()
        else:
            self.Log.logcontent(self.queue_id+": Queue.popFirstUser() error")
            return None
    
    def Lock(self):
        self.Log.logcontent(self.queue_id+": Queue.Lock() complete")
        if (not self.isLock):
            self.isLock=True
            return True
        return True
    
    def Unlock(self):
        self.Log.logcontent(self.queue_id+": Queue.Unlock() complete")
        if (self.isLock):
            self.isLock=False
            return True
        return True