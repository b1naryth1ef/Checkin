
import  wx

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a TextEntryDialog", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        dlg = wx.TextEntryDialog(
                self, 'What is your favorite programming language?',
                'Eh??', 'Python')

        dlg.SetValue("Python is the best!")

        if dlg.ShowModal() == wx.ID_OK:
            self.log.WriteText('You entered: %s\n' % dlg.GetValue())

        dlg.Destroy()




#---------------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#---------------------------------------------------------------------------


if __name__ == '__main__':
    import sys,os
    runTest("1","1","1")