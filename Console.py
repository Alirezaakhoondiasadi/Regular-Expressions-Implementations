from tkinter import *
from tkinter.scrolledtext import ScrolledText

mainWindow = Tk()
mainWindow.title('PicoVoice')
def getInputs( regexEntry) :
    Label(mainWindow, font = 25 ,   text="Please enter the pattern").grid(row=0, column=0)
    pattern = Entry(mainWindow, width=145); pattern.grid(row=0, column=1)

    Label(mainWindow , font = 25, text="Please enter the input string").grid(row=1, column=0)
    inputString = ScrolledText(mainWindow, width=120, height=25); inputString.grid(row=1, column=1)
    Button(mainWindow, font = 25, text="Process", command=(lambda: regexEntry.SetInputs( pattern.get(),  inputString.get("1.0", "end-1c")))).grid(row=1, column=2, sticky="EW" )

    Button(mainWindow, font = 25, text="Exit", command=sys.exit).grid(row=2, column=0, columnspan=3, sticky="EW")
    mainWindow.mainloop()    
def displayOutputs(output, resultNum) : 
    Label(mainWindow, text=output ).grid(row = resultNum+2, column=0)

    

