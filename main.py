from event import Event
from scheduler import Scheduler
from schedulerUI import SchedulerUI
import datetime

date = datetime.date(2024,1,10)
date1 = datetime.date(2024,1,11)




#TESTING
schedule = Scheduler()
schedule.addevent('Dentist Appointment','Get my teeth fixed, root canal surgery, bloody',date)
schedule.addevent('Birthday','Birthday event, bringing balloons',date1)
print(schedule.events)
schedule.delevent('Birthday')
print(schedule.events)

