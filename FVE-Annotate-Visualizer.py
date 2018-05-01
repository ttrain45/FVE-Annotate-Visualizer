from Tkinter import *
import getFiles
import graphArrows as graph

window = Tk()
 
window.title("Welcome to the FVE-Annotate Visualizer")
 
window.geometry('350x200')
 
directories = [] 
 
lbl = Label(window, text="Enter The Path To FVE-Anntate-Output")
lbl2 = Label(window, text="Where your scaffolding from FVE-Annotate are located")
 
lbl.place(relx = .5, rely = .1, anchor="center")
lbl2.place(relx = .5, rely = .2, anchor="center")
 
txt = Entry(window,width=50)
 
txt.place(relx = .5, rely = .5, anchor="center")
 
 
def clicked():
	directories.extend(getFiles.getFiles(txt.get()))
	directoryWindow = Toplevel(window)
	buttons = []
	variables = []
	j = 0
	def selectAll():
		for button in buttons:
			button.toggle()
	titleLabel = Label(directoryWindow, text="Select the scaffolding you want visualized")
	titleLabel.grid(row=0,column=((len(directories)%12)/2))
	selectAll = Button(directoryWindow, text="Select All", command=selectAll)
	selectAll.grid(row=1, column=((len(directories)%12)/2))
	for i in directories:
		variables.append(IntVar())
		dirNumber = int(i[9:])
		check = Checkbutton(directoryWindow, text=i, variable = variables[j], onvalue = 1, offvalue = 0)
		buttons.append(check)
		buttons[j].grid(row = dirNumber%12 + 2, column = dirNumber / 12)
		j += 1
	def done():
		k = 0
		paths = []
		for button in buttons:
			if variables[k].get():
				if (txt.get())[-1:] == '\\':
					paths.append(txt.get() + button['text'])
				else:
					paths.append(txt.get() + "\\" + button['text'])
			k += 1
		paths.sort(key = lambda x: x[-7:].split('-')[1])
		graph.createVisualization(paths)
	goButton = Button(directoryWindow, text="Go", command=done)
	goButton.grid(row=15,column=((len(directories)%12)/2))
 
btn = Button(window, text="Go", command=clicked)
 
btn.place(relx = .5, rely = .7, anchor="center")

def clear():
	txt.delete(0,END)

clear = Button(window, text="Clear", command=clear)

clear.place(relx = .5, rely = .9, anchor="center")
 
window.mainloop()