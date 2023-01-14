import  tkinter as tk # Importing Tkinter module

jadwalKuliah = ["senin", "selasa", "rabu", "kamis", "jumat"] # days

# customizable schedules

senin = {"subject" : "time"}

selasa = {"subject" : "time"}

rabu = {"subject" : "time"}

kamis = {"subject" : "time"}

jumat = {"subject" : "time"}

# connecting days to schedules
tag = {"senin" : senin,
       "selasa" : selasa,
       "rabu" : rabu,
       "kamis" : kamis,
       "jumat" : jumat}

screen = tk.Tk() # window

width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
screen.geometry(f"{width}x{height}+0+0")

screen.attributes("-transparentcolor", screen["bg"]) # to make window transparent
screen.overrideredirect(True)

'''
Function to clear program output on the screen
Parameters :
- labels : list, 
'''
labels = []
def destroyLabels(labels) :
    if len(labels) == 0 :
        pass
    else :
        for i in range(len(labels)) :
            if i % 2 == 1 :
                sub = labels[i]
                sub.destroy()
            elif i % 2 == 0 :
                line = labels[i]
                line.destroy()

# Main Logic

'''
Function to print schedules in a certain day
Parameters :
- day : String, one of the days in the tag dictionary
'''
def printSchedule(day) :
    x1 = 0.5
    y1 = 0.65
    x2 = 0.5
    y2 = 0.7

    if day.lower() == "clear" : # if input is "clear", delete output
        destroyLabels(labels)

    for jadwal in jadwalKuliah : # print schedules
        if day.lower() == jadwal : # destroys current labels and replace them with new labels
            destroyLabels(labels)
            for subjects in tag[jadwal] :
                sub = tk.Label(master=screen, text=f"{subjects} || {tag[jadwal][subjects]}", fg="white", font=("Helvetica", 20))
                labels.append(sub) # to keep track of the current subjects in the label
                sub.pack()
                sub.place(relx=x1, rely=y1, anchor="center")
                line = tk.Label(master=screen, text="--------------------------------------", fg="white", font=("Helvetica", 20))
                labels.append(line) # to keep track of the current lines in the label
                line.pack()
                line.place(relx=x2, rely=y2, anchor="center")
                y1 += 0.1
                y2 += 0.1

'''
Function to clear the input bar
'''
def clearEntry() :
    entry.delete(0, tk.END)

'''
Function to get actions based on keyboard input
Parameters :
- event : String, keys on keyboard
'''
def key_pressed(event):
    day = entry.get()
    clearEntry()
    printSchedule(day)

capt = tk.Label(master=screen, text="College Schedule", foreground="#ffffff", font=("Helvetica", 40))
capt.pack()
capt.place(relx=0.5, rely=0.495, anchor="center")

# program start
entry = tk.Entry(master=screen, fg="#FF10F0", bg="white", font=("Helvetica", 12), borderwidth=0)
entry.pack()
entry.place(relx=0.5, rely=0.55, anchor="center", width=300, height=22)
entry.bind("<Return>", key_pressed)
screen.mainloop()




