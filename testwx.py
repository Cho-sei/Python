# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:35:20 2018

@author: OKAMOTO_LAB
"""

import wx
 
application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
 
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('#AFAFAF')
 
s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'テキスト１')
s_text_2 = wx.StaticText(panel, wx.ID_ANY, 'テキスト２')
s_text_3 = wx.StaticText(panel, wx.ID_ANY, 'テキスト３')
s_text_4 = wx.StaticText(panel, wx.ID_ANY, 'テキスト４')
s_text_5 = wx.StaticText(panel, wx.ID_ANY, 'テキスト５')
 
s_text_3.Hide()
# s_text_3.Show()
 
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(s_text_1)
layout.Add(s_text_2)
layout.Add(s_text_3)
layout.Add(s_text_4)
layout.Add(s_text_5)
 
panel.SetSizer(layout)
 
frame.Show()
application.MainLoop()