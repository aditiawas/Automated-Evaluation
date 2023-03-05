from tkinter import *
from tkinter import ttk


class HomeFrame(Frame):
    def __init__(self,master):
        super(HomeFrame,self).__init__(master)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.pack()
        self.createWidgets(master)

    def createWidgets(self,master):

        Label(self,text="Hand-Written Paper Correction",anchor=CENTER,relief=GROOVE\
              ,width=700,height=2,font='Verdana 15 bold').pack(fill=BOTH)

        Button(self,text="UPLOAD SCHEME",padx=10,pady=20,\
               font='Helvetica 15 bold',command=lambda:self.nextWindow(1,master)).pack(padx=50,pady=30,fill=X)
        Button(self,text="VALIDATE SCRIPTS",padx=10,pady=20,\
               font='Helvetica 15 bold',command=lambda:self.nextWindow(2,master)).pack(padx=50,pady=30,fill=X)
        Button(self,text="ADD STUDENT",padx=10,pady=20, font='Helvetica 15 bold',command=lambda:self.nextWindow(3,master)).\
                              pack(padx=50,pady=30,fill=X)

    def nextWindow(self,frameType,master):
        master.destroy()
        if(frameType==1):
            import uploadScheme
        elif(frameType==2):
            import qpaperSelect
        elif (frameType==3):
            import addStudent
            
        else:
            pass
        

root=Tk()
root.title("Answer Script Evaluation Software")
root.geometry('700x500')
root.resizable(width=False,height=False)
root.configure(background='#ffffff')

hf=HomeFrame(root)
root.mainloop()
