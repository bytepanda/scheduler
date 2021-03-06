import Tkinter as tki,tkMessageBox as tbox, tkFileDialog as tdog
import schFunc

from ScrolledText import ScrolledText

class App(object):

    def __init__(self):
        self.root = tki.Tk()
        self.root.title("Loadshedding Schedule Parser")
        tki.Label(text='Copy Schedules from a table and paste it here:').pack()
        self.txt = ScrolledText(self.root, width="50" ,undo=True)
        self.txt['font'] = ('consolas', '12')
        self.txt.pack(expand=True, fill='both')


	def onok():

          dirname = tdog.askdirectory(parent=self.root,initialdir="/",title='Please select a directory')
          print dirname
          schFunc.parse(self.txt.get("1.0","end"),dirname)
          tbox.showinfo("Done","Schedules have been parsed and converted to INI files")


	tki.Button(self.root, text='Parse Schedules', command=onok).pack()

app = App()
app.root.mainloop()
