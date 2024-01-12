# This class deals with all the aspects of the GUI. Here, you'll create elements like windows, buttons, text fields, and define their behavior.
#drawing the elements on the canvas and connecting to the other classes/modules for data manipulation and logic.
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

class SchedulerUI:
    def __init__(self,schedule) -> None:
        self.window = tk.Tk()
        self.window.title('Scheduler')
        self.window.geometry('1000x800')
        self.schedule = schedule
        
        
        self.textfield()
        self.canvas()
        self.update_listbox()
        self.buttons()
        self.timeselector()
        
        
        
        
    def add_event(self):
        self.selectedDate = self.cal.get_date() # GETS A STRING, NEED TO CONVERT TO DATETIME LATER.
        self.selectedTitle = self.text_entry.get()
        self.selectedDescription = self.descriptionbox.get('1.0','end')
        
        self.schedule.addevent(self.selectedTitle,self.selectedDescription,self.selectedDate)
        self.update_listbox()
        
        
    def del_event(self):
        try:
            current = self.listbox.curselection() #select index of the object in the listview
            current2 = self.listbox.get(current) #get the whole thing from it going to be name : time
            event = current2.split(':')[0] #index 0 is the left side and 1 would be the time.
            self.schedule.delevent(event)
            print(event)
            self.update_listbox()
        except:
            pass

        pass
    def run(self):
        self.window.mainloop()
    
    def canvas(self): # creating a container
        self.frame1 = tk.Frame(self.window, bg="grey", width=200, height=200)
        self.frame1.pack()
    
    def buttons(self): #button management and what they do.
        self.addButton = tk.Button(self.frame1, text="Add", command=self.add_event,activebackground='green')
        self.delButton = tk.Button(self.frame1, text="Delete", command=self.del_event,activebackground='red')
        self.addButton.pack(side='left')
        self.delButton.pack()
        

    def textfield(self): #textfields to write in (writing event name, details etc.)
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(fill=tk.BOTH,expand=1)
        self.text_entry = tk.Entry(self.window)

        self.descriptionbox = tk.Text(self.window)
        self.descriptionbox.pack()
        
        
        self.text_entry.config(width=20)
        self.text_entry.pack()
    
    

    def update_listbox(self):
       self.listbox.delete(0,tk.END)
       for event,value in self.schedule.events.items():
           self.listbox.insert(tk.END,f'{value.event_name}:{value.time}')
          
        

    
    def timeselector(self): #select and manage time in the GUI:
        self.cal = Calendar(self.window,selectmode='day',year=2024,month=1,day=1)
        self.cal.pack(padx=10,pady=10)
