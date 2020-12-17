
from Participant import Participant
from GQueue import Queue

# Priority Queue base on Queue in GQueue


class CRUDPQueue(Queue):
    # sort the queue base on Participant.key
    def sortQueue(self):
        self.Log.logcontent(self.queue_id+": sortQueue()")
        self.queue.sort(key=Participant.key)
        self.Log.logcontent(self.queue_id+": sortQueue() complete")
        return True
