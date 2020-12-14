import logging
import datetime
class Log():
    def __init__(self):
        logging.basicConfig(filename='Lineup.log', encoding='utf-8', level=logging.DEBUG)
    def logcontent(self, s):
        logging.info(str(datetime.datetime.now())+": "+s)