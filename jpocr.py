import wx
import screenshot_app
import keyboard
from multiprocessing import Process
mode = 'Vocab'


class TransparentFrame(wx.Frame):
    ''' Transparent Frame '''
    DEFAULT_ALPHA = 255
    DEFAULT_SIZE = (400, 200)
    TEXTCTRL_SIZE = (200, 100)
    def __init__(self, size=DEFAULT_SIZE, *args, **kwargs):
        wx.Frame.__init__(self, None, size=size, title='yomeru', style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, *args, **kwargs)
        # This is all you need to make the window transparent.
        self.SetTransparent(self.DEFAULT_ALPHA)
        # self.SetWindowStyle(wx.STAY_ON_TOP)

        pnl = wx.Panel(self)
        self.button = wx.Button(pnl, label='Scan')
        self.button.Bind(wx.EVT_BUTTON, self.onClick)
        self.Centre()
        self.Show(True)


        lblList = ['Vocab', 'Google', 'Romaji', 'DeepL']

        self.rbox = wx.RadioBox(pnl, label='Mode', pos=(80, 10), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.onRadioBox)
        self.Centre()
        self.Show(True)

        self.Centre()
        self.Show(True)




    def onClick(self, event):
        screenshot_app.ocr_main(mode)

    def onRadioBox(self, e):
        global mode
        mode = self.rbox.GetStringSelection()
        print(mode)



if __name__ == '__main__':
    app = wx.App(False)
    frame = TransparentFrame()
    frame.Show()
    keyboard.add_hotkey('shift+ctrl+a', lambda: screenshot_app.spawn_ocr_main_process())
    app.MainLoop()
