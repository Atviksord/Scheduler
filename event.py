## This class represents an individual event with properties such as title, start time, end time, and participants, along with methods to manipulate these.
import datetime
class Event:
    def __init__(self,event_name,description,time,recurring = False,days = 0) -> None:
        self.event_name = event_name #string
        self.description = description #string
        self.time = time #datetimeobject
        self.recurring = recurring #boolean flag
        self.days = days #int
        
    
