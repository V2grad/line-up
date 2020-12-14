
from Participant import Participant
from GQueue import Queue
class PQueue(Queue):
    def sortQueue(self):
        self.Log.logcontent(self.queue_id+": sortQueue()")
        self.queue.sort(key = Participant.key)
        self.Log.logcontent(self.queue_id+": sortQueue() complete")
        return True
