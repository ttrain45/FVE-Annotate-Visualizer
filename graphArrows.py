import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patch
import parseScaffoldProteinFAA as parser
import pandas as pd
import os
from random import randint
from matplotlib.widgets import Slider
from Tkinter import *
import tkMessageBox

def createVisualization(path):
	
	numScaffolding = len(path)
	scaffoldNumbers = []
	for i in range(0,numScaffolding):
		path[i] = path[i] + '\\scaffold-' + path[i][-7:].split('-')[1] + '-proteins.faa'
		scaffoldNumbers.append(path[i][-24:].split('-')[1])

	dfs = []
	figWidth = 0
	figStart = 10000000
	arrowHeight = 1.62
	figHeight = arrowHeight * numScaffolding if arrowHeight * numScaffolding > 10 else 10
	for x in range(0,numScaffolding):
		dfs.append(parser.parseFile(path[x]))
		figWidth = int(dfs[x].tail(1)["FINISH"]) if int(dfs[x].tail(1)["FINISH"]) > figWidth else figWidth
		figStart = int(dfs[x].head(1)["START"]) if int(dfs[x].head(1)["START"]) < figStart else figStart 
	figWidth = figWidth + 10
	figStart = figStart - 100 

	fig, ax = plt.subplots(figsize=(10,10))
	plt.subplots_adjust(bottom=0.25)

	scaffoldPositionY = 1.5
	
	for x in range(0, numScaffolding):
		df = dfs[x]
		randColor = [randint(60, 220),randint(60, 220),randint(60, 220)]
		shades = [[randColor[0]-60,randColor[1]-60,randColor[2]-60],[randColor[0]-30,randColor[1]-30,randColor[2]-30], randColor]
		useThis = [i / 255.0 for i in randColor]
		for index, row in df.iterrows():
			useThis = [i / 255.0 for i in shades[index % 3]]
			dif = int(row[3]) - int(row[2])
			if row[4] == '-1':
				ax.add_patch(patch.Arrow(int(row[3]), scaffoldPositionY, -dif, 0, width = 2, color = useThis, picker = 2, label = str(index) + '-' + str(x)))
			else:
				ax.add_patch(patch.Arrow(int(row[3]), scaffoldPositionY, dif, 0, width = 2, color = useThis, picker = 2, label = str(index) + '-' + str(x)))  
		scaffoldPositionY = scaffoldPositionY + 1.5
				
	plt.axis([figStart, figStart + 5000, 0, 10])

	axpos = plt.axes([0.2, 0.15, 0.65, 0.03])
	
	aypos = plt.axes([0.2, 0.1, 0.65, 0.03])
	
	spos = Slider(axpos, 'X Pos', figStart, figWidth - 5000, valinit = figStart)
	
	sposY = Slider(aypos, 'Y Pos', 0, figHeight - 10, valinit = 0)

	def update(val):
		posY = sposY.val
		pos = spos.val
		ax.axis([pos,pos+5000,posY, posY+10])
		fig.canvas.draw_idle()
	
	def onpick(event):
		
		arrowChosen = event.artist
		labelData = arrowChosen.get_label()
		index = int(labelData.split('-')[0])
		scaffold = int(labelData.split('-')[1])
		data = dfs[scaffold].loc[index]
		if data[4] == '-1':
			direction = 'Reverse'
		else:
			direction = 'Forward'
		root = Tk()
		text = Text(root)
		text.insert(INSERT, 'Data for ' + data[1][1:] + '\nScaffolding: Scaffold-' + scaffoldNumbers[scaffold] + '\nStart: ' + data[2] + '\nFinish: ' + data[3] + '\nDirection: ' + direction + '\nProtein: ' + data[5])
		text.pack()
		root.mainloop()
		
		return True
		
		

	fig.canvas.mpl_connect('pick_event', onpick)

	spos.on_changed(update)
	sposY.on_changed(update)

	plt.show()

