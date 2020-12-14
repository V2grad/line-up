# Event class
# it manages all the queue
import GQueue
import Log
class Event:
    # initialize the class
    # argument: name of the Event, id of the event
    def __init__(self,name,id):
        self.name = name
        self.all_queues = dict()
        self.event_id = id
        self.isLocked = False
        self.Log = Log()
        self.Log.logcontent(self.event_id + ": initializing complete")
    
    # return the event name
    def getEventName(self):
        self.Log.logcontent(self.event_id + ": Event.getEventName")
        self.Log.logcontent(self.event_id + ": Event.getEventName complete")
        return self.name
    
    # return the event id
    def getEventId(self):
        self.Log.logcontent(self.event_id + ": Event.getEventId")
        self.Log.logcontent(self.event_id + ": Event.getEventId complete")
        return self.event_id
    
    # add a queue into the event
    # argument: name of the queue, id of the queue
    def addQueue(self,name,queue_id):
        self.Log.logcontent(self.event_id + ": Event.addQueue({0},{1})".format(name,queue_id))
        if(self.isLock == False):
            self.all_queues[queue_id]=GQueue(name,queue_id)
            self.Log.logcontent(self.event_id + ": Event.addQueue({0},{1}) complete".format(name,queue_id))
            return True
        else:
            self.Log.logcontent(self.event_id + ": Event.addQueue({0},{1}) error".format(name,queue_id))
            return False
    
    # delete a specific queue in the event
    # arguments: id of that queue
    def deleteQueue(self,queue_id):
        self.Log.logcontent(self.event_id + ": Event.deleteQueue({0})".format(queue_id))
        if(self.isLock == False):
            self.all_queues.pop(queue_id)
            self.Log.logcontent(self.event_id + ": Event.deleteQueue({0}) complete".format(queue_id))
            return True
        else:
            self.Log.logcontent(self.event_id + ": Event.deleteQueue({0}) error".format(queue_id))
            return False
    # view the Logs of the event
    def viewLogs(self):
        #place holder
        return True
