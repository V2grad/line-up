import sys
sys.path.append("../models")
from Event import Event

#test model/Event.py
if __name__ =="__main__":
    a=Event('lab1',1)
    print(a.getEventName())
    print(a.getEventId())
    a.addQueue('check',1)
    a.deleteQueue(1)
    a.addQueue('check',1)
    a.addQueue('help',2)
    a.Lock()
    a.deleteQueue(1)
    a.addQueue('extra',3)
    a.Unlock()
