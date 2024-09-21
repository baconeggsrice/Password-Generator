import password
import wx

class guiFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(guiFrame, self).__init__(*args,**kwargs)
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
        num = self.text_ctrl.GetValue()
        self.clicked = True
        if (num.isnumeric() == True):
            num = int(num)
            password.generate(num)
        else:
            wx.CallLater(1000, self.showError)
        
    def showError(self):
        wx.MessageBox("Error, Not a number. Please Enter a whole number.", 'Error', wx.OK | wx.ICON_INFORMATION)
    