# This class deals with all the aspects of the GUI. Here, you'll create elements like windows, buttons, text fields, and define their behavior.
#drawing the elements on the canvas and connecting to the other classes/modules for data manipulation and logic.
import tkinter as tk
from scheduler import Scheduler

class SchedulerUI:
    def __init__(self, schedule) -> None:
        self.window = tk.Tk()
        self.window.title = 'Scheduler'
        self.window.geometry('1000x800')
        self.scheduler = schedule
        self.textfield()
        self.listbox()
        
        
    def run(self):
        self.window.mainloop()
    
    def canvas(self): #using tkinter to create side windows
        pass
    
    def buttons(self): #button management and what they do.
        pass

    def textfield(self): #textfields to write in (writing event name, details etc.)
        text_entry = tk.Entry(self.window)
        text_entry.config(width=20)
        text_entry.place(x=500,y=400)
    def listbox(self):
        listbox = tk.Listbox(self.window)
        
        for event in self.scheduler.events:
            listbox.insert(tk.END,str(event))
        listbox.pack()
        
    
    def timeselector(self): #select and manage time in the GUI:
        pass