#!/usr/bin/python

import wx

class EekMexGui(wx.App):

    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):

        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)
	pass

    def main(self, parent):

        wx.Frame.__init__(self, None, wx.ID_ANY, "EekMex")
        

        pass

app = EekMexGui()
app.main('Temp')

# End of File
