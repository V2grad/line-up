import logging
import datetime
# it record all the activities of event
class Log():

    # initializing the Log cass
    def __init__(self,s):
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("lineup_"+s+".log"),
                              logging.StreamHandler()])
    
    #record a message into Lineup.log
    #argument: string that need to be recorded
    def logContent(self, s):
        logging.info(s)
    
    #view the Log
    def viewLog(self):
        #place holder
        return False