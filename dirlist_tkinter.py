#!/C:/Users/lh3795/AppData/Local/Programs/Python/Python37-32
import sys
import os
from time import sleep
from tkinter import *

class DirList(object):
    def __init__(self, initdir=None):
        '''directory lister'''
        #show title
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()
        self.cuwd = StringVar(self.top)
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()
        #show list
        self.dirmf = Frame(self.top)
        self.dirsb = Scrollbar(self.dirmf)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirbox = Listbox(self.dirmf, height=15, width=50,
                              yscrollcommand=self.dirsb.set)
        self.dirbox.bind('<Return>', self.setDirAndGo)
        self.dirsb.config(command=self.dirbox.yview)
        self.dirbox.pack(side=LEFT, fill=BOTH)
        self.dirmf.pack()
        #type in directory address
        self.diren = Entry(self.top, width=50,textvariable=self.cuwd)
        self.diren.bind('<Return>', self.showList)
        self.diren.pack()

        self.secf = Frame(self.top)
        self.clr = Button(self.secf, text='clear', command=self.clrDir,
                          activeforeground='white',
                          activebackground='red')
        self.ls = Button(self.secf, text='show list', command=self.showList,
                          activeforeground='grey',
                          activebackground='red')
        self.quitp = Button(self.secf, text='quit', command=self.top.quit,
                          activeforeground='yellow',
                          activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quitp.pack(side=LEFT)
        self.secf.pack()
        #init frame
        if initdir:
            self.cuwd.set(initdir)
            self.showList()
        else:
            self.cuwd.set(os.curdir)
            self.showList()

    def setDirAndGo(self, ev=None):
        self.dirbox.config(selectbackground='red')
        checkDir = self.dirbox.get(self.dirbox.curselection())
        if not checkDir:
            checkDir = os.curdir
        self.cuwd.set(checkDir)
        self.showList()            
        
    def clrDir(self, ev=None):
        self.cuwd.set('')
        
    def showList(self, ev=None):
        error = ''
        todir = self.cuwd.get()
        if  not todir: todir = os.curdir
        if not os.path.exists(todir):
            error = todir + ': no such file'
        elif not os.path.isdir(todir):
            error = todir + ': not a directory'

        if error:
            self.cuwd.set(error)
            self.top.update()
            sleep(2)
            self.cuwd.set(os.curdir)
            self.dirbox.config(selectbackground='green')
            self.top.update()
            return

        self.cuwd.set('fetching dic con')
        self.top.update()
        dirList = os.listdir(todir)
        dirList.sort()
        os.chdir(todir)
        self.dirl.config(text=os.getcwd())
        self.dirbox.delete(0, END)
        self.dirbox.insert(END, os.curdir)
        self.dirbox.insert(END, os.pardir)
        for fi in dirList:
            self.dirbox.insert(END, fi)
        self.cuwd.set(todir)
        self.dirbox.config(selectbackground='yellow')
        
def mainfun():
    if len(sys.argv) > 1:
        a =sys.argv[1]
        print(a)    
    else:
        a = None
    d = DirList(a)
    mainloop()

if __name__ == '__main__':
    mainfun()

