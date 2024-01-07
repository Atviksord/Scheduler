## This class represents an individual event with properties such as title, start time, end time, and participants, along with methods to manipulate these.
import datetime
class Event:
    def __init__(self,event_name,description,time,recurring = False) -> None:
        self.event_name = event_name
        self.description = description
        self.time = time
        self.recurring = recurring
        
    
