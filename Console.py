from tkinter import *
from tkinter.scrolledtext import ScrolledText

mainWindow = Tk()
def getInputs( regexEntry) :
    Label(mainWindow, text="Please enter the pattern").grid(row=0, column=0)
    pattern = Entry(mainWindow, width=95); pattern.grid(row=0, column=1)

    Label(mainWindow, text="Please enter the input string").grid(row=1, column=0)
    inputString = ScrolledText(mainWindow, width=70, height=5); inputString.grid(row=1, column=1)
    Button(mainWindow, text="Process", command=(lambda: regexEntry.SetInputs( pattern.get(),  inputString.get("1.0", "end-1c")))).grid(row=1, column=2, sticky="EW" )

    Button(mainWindow, text="Exit", command=sys.exit).grid(row=2, column=0, columnspan=3, sticky="EW")
    mainWindow.mainloop()    

def displayOutputs(output) : 
    Label(mainWindow, text=output ).grid(row=3, column=0)

    

