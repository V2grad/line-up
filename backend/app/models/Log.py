import logging
import datetime
# it record all the activities of event
class Log():

    # initializing the Log cass
    def __init__(self):
        logging.basicConfig(filename='Lineup.log', encoding='utf-8', level=logging.DEBUG)
    
    #record a message into Lineup.log
    #argument: string that need to be recorded
    def logContent(self, s):
        logging.info(str(datetime.datetime.now())+": "+s)
    
    #view the Log
    def viewLog(self):
        #place holder
        return False