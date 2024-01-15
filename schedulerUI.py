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
        self.recurring = False
        self.days = 0
        
        
        self.textfield()
        self.canvas()
        self.update_listbox()
        self.buttons()
        self.timeselector()
        self.setuprecurring()
        

        
    def add_event(self):
        self.selectedDate = self.cal.get_date() # GETS A STRING, NEED TO CONVERT TO DATETIME LATER.
        self.selectedTitle = self.text_entry.get()
        self.selectedDescription = self.descriptionbox.get('1.0','end')
        if self.recurring:
            self.days = int(self.recurringentry.get())

        if self.selectedDate and self.selectedTitle and self.selectedDescription:
            self.schedule.addevent(self.selectedTitle,self.selectedDescription,self.selectedDate,self.recurring,self.days)
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
        self.frame1 = tk.Frame(self.window, bg="grey", width=300, height=200)
        self.frame1.pack()
    
    def setuprecurring(self):
        self.check_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.window,text='Recurring',variable=self.check_var,command=self.togglestate)
        self.checkbox.place(x='80',y='600')
        self.recurringentry = tk.Entry(self.window,state='readonly')
        self.recurringentry.place(x='175',y='600')
    def togglestate(self):
        if self.check_var.get() == 1:
            self.recurringentry.configure(state='normal')
            self.recurring = True   
        else:
            self.recurringentry.delete(0,'end')
            self.recurringentry.configure(state='readonly')
            self.recurring = False
            
    def buttons(self): #button management and what they do.
        self.addButton = tk.Button(self.frame1, text="Add", command=self.add_event,activebackground='green')
        self.delButton = tk.Button(self.frame1, text="Delete", command=self.del_event,activebackground='red')
        self.addButton.pack(side='left')
        self.delButton.pack()
    
    def displayEvent(self,event):
        selected_event = self.listbox.get(self.listbox.curselection())
        popup = tk.Toplevel(self.window)
        popup.geometry('500x500')
        eventName = selected_event.split(':')[0]
        popup.title(eventName)
        listbox2 = tk.Listbox(popup)
        listbox2.pack(fill=tk.BOTH,expand=1)
        
        for event,value in self.schedule.events.items():
            if event == eventName:
                listbox2.insert(tk.END,f'{value.event_name}:{value.time}')
                listbox2.insert(tk.END,'------------------------------------------')
                listbox2.insert(tk.END,'')
                listbox2.insert(tk.END,'')
                listbox2.insert(tk.END,value.description)


    def textfield(self): #textfields to write in (writing event name, details etc.)
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(fill=tk.BOTH,expand=1)
        self.listbox.bind("<Double-Button-1>",self.displayEvent)
        self.text_entry = tk.Entry(self.window)

        self.descriptionbox = tk.Text(self.window)
        self.descriptionbox.pack()
        
        self.text_entry.config(width=20)
        self.text_entry.pack()
    
    def update_listbox(self):
       self.listbox.delete(0,tk.END)
       for event,value in self.schedule.events.items():
           self.listbox.insert(tk.END,f'{value.event_name}:{value.time}: Recurring: {value.recurring} This event will happen again every: {value.days} days')
          
    def timeselector(self): #select and manage time in the GUI:
        self.cal = Calendar(self.window,selectmode='day',year=2024,month=1,day=1)
        self.cal.pack(padx=10,pady=10)
    
