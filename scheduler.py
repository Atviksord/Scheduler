#This class can serve as a container and manager for Event objects.
from event import Event
import datetime
import plyer
import time
class Scheduler:
    def __init__(self) -> None: 
        self.events = {} #will hold instances/objects of each event.
    
    def addevent(self,event_name,description,time,recurring = False,days = 0): #add event, 3 fields 1 optional. Event name, Event description, Time and 4th recurring (if recurring, what interval)
        #reads textbox in GUI, this is triggered by a button from GUI.
        #reads from time selection as well.
        if not event_name:
            raise Exception('Please write an event name')
        if not description:
            raise Exception('Please write a description for the event')
        if not time:
            raise Exception('Please select a time')
        
        event = Event(event_name,description,time,recurring)
        self.conflicting_event(time)
        
        if recurring:
            if days > 0:
                self.recurring_event(event,days) #if its a recurring event, call this to handle it. TO BE MADE!!!
        self.events.update({event.event_name: event}) 
    
    def delevent(self,event_name): #deletes a selected event, once a non reccuring event is triggered, automatically remove the event.
         #if the key is found, delete the object from hashmap
                if event_name in self.events:
                    del self.events[event_name]
                print(f'Event: {event_name} not found')
                
    
    def reminder(self): #Sends out reminders based on proximity of schedule deadlines. Python datetime, and time libraries.
        current_date = datetime.datetime.now().date()
        for event in self.events.values():
             if event.time.date() - current_date == datetime.timedelta(days=1):
                plyer.notification.notify(title=event.event_name, message= event.description, timeout=10)
                
    
    def conflicting_event(self,time): #checks for conflict in schedules. If you have another schedule on the same hour returns an OVERBOOKED warning.
        for event in self.events:
            if self.events[event].time == time:
                raise Exception (f'OVERBOOKED {event.event_name} is already scheduled for that time')
                
    
    def recurring_event(self,event,days): #method that reapplies the same event on (x) interval(if the reccurring flag is true). if deleted will stop.
         if event in self.events and self.events[event].recurring:
               event.time += datetime.timedelta(days=days)

              
        
             