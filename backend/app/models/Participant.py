
#Base class of user, admin and Assistant
class Participant:
    def __init__(self,name,user_id,contact):
        self.name = name
        self.user_id = user_id
        self.contact = contact
        self.key=0
        self.busy = False
    