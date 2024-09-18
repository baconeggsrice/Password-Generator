import password
import wx

class guiFream(wx.Frame):
    def __init__(self, *args, **kwargs):
        panel = wx.Panel(self)
        self.InitUI(panel)
        self.label = wx.StaticText(panel, label = "Choose a password length: ", pos = (15,15))
        self.info = 0

    def InitUI(self, panel):
        self.getLength(panel)
        self.SetSize((250,250))
        self.SetTitle('Password Generator')
        self.Center()

    def getLength(self, panel):
        self.text_ctrl = wx.TextCtrl(panel, pos = (75, 75))
        self.button = wx.Button(panel, label = "Create Password")

    def buttonTriggered(self, panel):
        