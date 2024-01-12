
from scheduler import Scheduler
from schedulerUI import SchedulerUI

import datetime


date = datetime.date(2024,1,10)
date2 = datetime.date(2024,1,13)
date3 = datetime.date(2024,1,12)




#TESTING
schedule = Scheduler()


window = SchedulerUI(schedule)
window.run()






