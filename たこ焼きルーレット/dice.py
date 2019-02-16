import pandas as pd
import numpy as np
import random
import wx
import msvcrt
import csv
import os

def click(event):
	main()

def textenter(event):
	print(textbox.GetValue())

def main():
	

	vSizer = wx.BoxSizer(wx.VERTICAL)
	layout = wx.BoxSizer(wx.HORIZONTAL)
	button_layout = wx.BoxSizer(wx.HORIZONTAL)
	frame = wx.Frame(None, wx.ID_ANY, 'たこ焼きダイス', size=(800,300))
	panel = wx.Panel(frame, wx.ID_ANY)
	textbox = wx.TextCtrl(panel,wx.ID_ANY)
	

	kind = random.randint(2,4)
	matelist = materials.sample(n=kind)
	list_r = matelist.reset_index()
	list = list_r['具材']

	counter_list = [0] * len(materials.index)
	array = matelist.index.values
	output = array.tolist()

	for i in output:
		counter_list[i] = 1

	counter_list.append(textbox.GetValue())
	

	with open('test.csv','a') as file:
	    writer = csv.writer(file, lineterminator='\n')
	    writer.writerow(counter_list)
	            

	button = wx.Button(panel,wx.ID_ANY,'ルーレット')
	end_button = wx.Button(panel,wx.ID_ANY,'終了')

	button.Bind(wx.EVT_BUTTON, click)
	end_button.Bind(wx.EVT_BUTTON, exit)
	textbox.Bind(wx.EVT_TEXT_ENTER, textenter)

	font = wx.Font(20,wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

	if kind == 2:
	    text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
	    text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
	    text1.SetFont(font)
	    text2.SetFont(font)
	    layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
	elif kind == 3:
	    text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
	    text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
	    text3 = wx.StaticText(panel, wx.ID_ANY, list[2], style=wx.TE_CENTER)
	    text1.SetFont(font)
	    text2.SetFont(font)
	    text3.SetFont(font)
	    layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text3,proportion=1,flag=wx.ALIGN_CENTER)
	elif kind == 4:
	    text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
	    text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
	    text3 = wx.StaticText(panel, wx.ID_ANY, list[2], style=wx.TE_CENTER)
	    text4 = wx.StaticText(panel, wx.ID_ANY, list[3], style=wx.TE_CENTER)
	    text1.SetFont(font)
	    text2.SetFont(font)
	    text3.SetFont(font)
	    text4.SetFont(font)
	    layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text3,proportion=1,flag=wx.ALIGN_CENTER)
	    layout.Add(text4,proportion=1,flag=wx.ALIGN_CENTER)

	button_layout.Add(button,flag=wx.ALIGN_BOTTOM)
	button_layout.Add(end_button,flag=wx.ALIGN_BOTTOM)

	vSizer.Add(layout, proportion=4, flag=wx.ALIGN_CENTER)
	vSizer.Add(textbox,proportion=1,flag=wx.ALIGN_CENTER)
	vSizer.Add(button_layout, proportion=1, flag=wx.ALIGN_CENTER)
	            
	panel.SetSizer(vSizer)
	            
	frame.Centre()
	frame.Show()

	

application = wx.App()
materials = pd.read_excel("materials.xlsx")
input = materials.T
array = input.values
list = array.tolist()
output = [flatten for inner in list for flatten in inner]
output.append('評価')
with open('test.csv','w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(output)
main()
application.MainLoop()