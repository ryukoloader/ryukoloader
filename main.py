import wx
import requests

r = requests.get('https://raw.githubusercontent.com/ryukoloader/dll_storage/main/hacklist')
cheatlist = r.text.split("\n")

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(190,280))
        self.statusbar = self.CreateStatusBar()
        self.Show(True)
        panel = wx.Panel(self)
        self.statusbar.SetStatusText('ryuko loader alpha (v0.1)')

        inject   = self.btn = wx.Button(panel, -1, "Inject", (10, 155), (155, 25))
        settings = self.btn = wx.Button(panel, -1, "Settings", (10, 185), (75, 25))
        bypass   = self.btn = wx.Button(panel, -1, "VAC Bypass", (90, 185), (75, 25))

        inject.Bind(wx.EVT_BUTTON, self.OnInject) 
        settings.Bind(wx.EVT_BUTTON, self.OnSettings) 
        bypass.Bind(wx.EVT_BUTTON, self.OnBypass) 

        lst = wx.ListBox(panel, pos = (10, 10), size = (155, 140), choices = cheatlist, style = wx.LB_SINGLE)

    def OnInject(self, e):
        event.GetEventObject().GetStringSelection()
        

    def OnSettings(self, e):
        dlg = wx.MessageDialog( self, "qweeqwwqewqe", "settings trigger", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnBypass(self, e):
        dlg = wx.MessageDialog( self, "qweeqwwqewqe", "bypass trigger", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, " свинья ебля Украина срать инкогнито дрочка")
app.MainLoop()