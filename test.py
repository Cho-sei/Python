import wx

class ChildFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"child frame",pos=(100,100))

class MyWindow(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"main frame")
        panel = wx.Panel(self)
        self.showChildBtn = wx.Button(panel,label="show child",pos=(10,10))
        self.exitBtn = wx.Button(panel,label="exit",pos=(100,10))
        self.Bind(wx.EVT_BUTTON,self.showChild,self.showChildBtn)
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)
    def showChild(self,event):
        childFrame = ChildFrame(self)
        childID = childFrame.Show()
    def exit(self,event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frame = MyWindow(parent=None,id=-1)
    frame.Show()
    app.MainLoop()