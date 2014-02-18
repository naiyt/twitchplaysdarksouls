import wx
from queue import MyQ

class GameFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))

class GameWindow(wx.Panel):
    def __init__(self, parent, queue, update):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.queue = queue

        grid = wx.GridBagSizer(hgap=7, vgap=7)
        self.votes_label = wx.StaticText(self, label="Votes")
        self.actions_label = wx.StaticText(self, label="Actions in Queue")

        font = wx.Font(15, wx.FONTFAMILY_ROMAN, wx.NORMAL, wx.NORMAL)
        self.votes_label.SetFont(font)
        self.actions_label.SetFont(font)

        grid.Add(self.votes_label, pos=(0,0))
        grid.Add(self.actions_label, pos=(0,7))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(grid, 0, wx.ALL, 8)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        if update:
            self.timer = wx.Timer(self)
            self.Bind(wx.EVT_TIMER, self.update, self.timer)
            self.timer.Start(2000)

        self.Show(True)

    def update(self, event):
        votes = self.queue.get_votes()
        in_queue = self.queue.get_queue()
        votes_str = 'Votes:\n'
        for vote in votes:
            new_section = '{} - {}\n'.format(votes[vote], vote)
            votes_str += new_section
        self.votes_label.SetLabel(votes_str)
        
        queue_section = 'Actions in Queue\n'
        for queued in in_queue:
            queue_section += '{}\n'.format(queued)
        self.actions_label.SetLabel(queue_section)



class Gui:
    def __init__(self, queue, update=True):

        app = wx.App(False)
        frame = GameFrame(None, 'Twitch Plays Dark Souls')
        GameWindow(frame, queue, update)
        frame.Show()
        app.MainLoop()

if __name__ == '__main__':
    gui = Gui([1,2,3], update=False)