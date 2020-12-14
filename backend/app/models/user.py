from Participant import Participant

#User base on Participant
class User(Participant):
    # tell users all the assistants who can help
    # argument: list of all assistants
    def setAssistant(self,assistant):
        self.assistant = assistant
        self.assistantname = []
        for i in self.assistant:
            self.assistantname.append(i.name)
        self.assistantid=[]
        for i in self.assistant:
            self.assistantid.append(i.user_id)
    
    #return all the names of assistants who can help me
    def getAssistantName(self):
        return self.assistantname
    
    #return all the names of assistants who can help me
    def getAssistantId(self):
        return self.assistantid
    
    #return the contact information
    def getContact(self):
        return self.contact