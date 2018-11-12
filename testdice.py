# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:51:08 2018

@author: OKAMOTO_LAB
"""
import wx

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, size=(300,300))
panel1 = wx.Panel(frame, wx.ID_ANY, size=(300,200))
#panel2 = wx.Panel(frame, wx.ID_ANY, size=(300,100), pos=(0,200))

panel1.SetBackgroundColour('#FFFFFF')
#panel2.SetBackgroundColour('#00FF00')

button1 = wx.Button(panel1, wx.ID_ANY, 'button1')
button2 = wx.Button(panel1, wx.ID_ANY, 'button2')
button3 = wx.Button(panel1, wx.ID_ANY, 'button3')
button4 = wx.Button(panel1, wx.ID_ANY, 'button4')

vSizer = wx.BoxSizer(wx.VERTICAL)
layout1 = wx.BoxSizer(wx.HORIZONTAL)
layout2 = wx.BoxSizer(wx.HORIZONTAL)

layout1.Add(button1)
layout1.Add(button2)
layout2.Add(button3)
layout2.Add(button4)

vSizer.Add(layout1)
vSizer.Add(layout2)

panel1.SetSizer(vSizer)

frame.Centre()
frame.Show()
application.MainLoop()