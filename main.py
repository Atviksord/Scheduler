from event import Event
from scheduler import Scheduler
from schedulerUI import SchedulerUI
import datetime
from plyer import notification

date = datetime.date(2024,1,10)
date2 = datetime.date(2024,1,13)
date3 = datetime.date(2024,1,12)

date = date.strftime("%Y-%m-%d %H-%M")
date2 = date2.strftime("%Y-%m-%d %H-%M")
date3 = date3.strftime("%Y-%m-%d %H-%M")



#TESTING
schedule = Scheduler()
schedule.addevent('Dentist Appointment','Get my teeth fixed, root canal surgery, bloody',date)
schedule.addevent('Birthday','Birthday event, bringing balloons',date2)


window = SchedulerUI(schedule)
window.run()


#print(list(schedule.events.keys()))
#print(list(schedule.events['Birthday'].time))

#print(list(schedule.events.keys()))


