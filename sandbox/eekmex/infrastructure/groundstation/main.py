#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

class EmLoadingPanel(wx.Panel):

    def __init__(self, *args, **kwargs):

        super(EmLoadingPanel, self).__init__(*args, **kwargs)

        image = wx.Image("black.jpg")
        width, height = wx.GetDisplaySize()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        self.bitmap = wx.BitmapFromImage(image)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        cid = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onCtrlC, id=cid)
        self.accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL, ord('C'), cid),])
        self.SetAcceleratorTable(self.accel_tbl)
        self.c = None
        self.sensors = []
        self.port = None

    def onCtrlC(self, event):
        self.GetParent().Close()

    def OnPaint(self, event):
        self.Paint(wx.PaintDC(self))

    def Paint(self, dc):
        dc.DrawBitmap(self.bitmap, 0, 0) 

class EmGroundStation(wx.Frame):

    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title)

        image = wx.Image("black.jpg")
        width, height = wx.GetDisplaySize()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        self.bitmap = wx.BitmapFromImage(image)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.panelLoading = EmLoadingPanel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelLoading, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def OnPaint(self, event):
        self.Paint(wx.PaintDC(self)) 

    def Paint(self, dc):
        dc.DrawBitmap(self.bitmap, 0, 0) 

if __name__ == "__main__":

    app = wx.App()
    frame = EmGroundStation(None,-1,'EekMex Ground Station')
    frame.ShowFullScreen(True)
    frame.Show(True)
    app.MainLoop()
