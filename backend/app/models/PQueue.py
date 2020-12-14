from Participant import Participant
import GQueue
class PQueue(GQueue):
    def sortQueue(self):
        self.Log.logcontent(self.queue_id+": sortQueue()")
        self.queue.sort(key = Participant.key)
        self.Log.logcontent(self.queue_id+": sortQueue() complete")
        return True
