import pandas as pd
import random
import wx
import time

application = wx.App()

layout = wx.BoxSizer(wx.HORIZONTAL)

materials = pd.read_excel("materials.xlsx")

for i in range(2):
    kind = random.randint(2,4)
    matelist = materials.sample(n=kind)
    list_r = matelist.reset_index()
    list = list_r['具材']
    print(list_r)
    
    frame = wx.Frame(None, wx.ID_ANY, 'たこ焼きダイス', size=(kind*200,300))
    panel = wx.Panel(frame, wx.ID_ANY)
    button = wx.Button(panel,wx.ID_ANY,'ルーレット')
    
    layout.Add(button,flag=wx.ALIGN_BOTTOM)
    
    if kind == 2:
        text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
        text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
        layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
    elif kind == 3:
        text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
        text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
        text3 = wx.StaticText(panel, wx.ID_ANY, list[2], style=wx.TE_CENTER)
        layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text3,proportion=1,flag=wx.ALIGN_CENTER)
    elif kind == 4:
        text1 = wx.StaticText(panel, wx.ID_ANY, list[0], style=wx.TE_CENTER)
        text2 = wx.StaticText(panel, wx.ID_ANY, list[1], style=wx.TE_CENTER)
        text3 = wx.StaticText(panel, wx.ID_ANY, list[2], style=wx.TE_CENTER)
        text4 = wx.StaticText(panel, wx.ID_ANY, list[3], style=wx.TE_CENTER)
        layout.Add(text1,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text2,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text3,proportion=1,flag=wx.ALIGN_CENTER)
        layout.Add(text4,proportion=1,flag=wx.ALIGN_CENTER)
    
    panel.SetSizer(layout)
    
    frame.Centre()
    frame.Show()
    
    time.sleep(2)
    frame.Destroy()

application.MainLoop()