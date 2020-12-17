import sys
sys.path.append("../models")
from GQueue import GQueue
from User import User

#test model/PQueue.py
if __name__ =="__main__":
    a=GQueue('check',1)
    a.getQueueName
    a.getQueueId
    alice = User('Alice',1,'alice@rpi.edu')
    bob = User('Bob',2,'bob@rpi.edu')
    a.addUser(alice)
    a.removeUser(alice)
    a.addUser(bob)
    a.removeUserById(2)
    a.Lock()
    a.addUser(alice)
    a.addUser(bob)
    a.Unlock()
    a.addUser(alice)
    a.addUser(bob)