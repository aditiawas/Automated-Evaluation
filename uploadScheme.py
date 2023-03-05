from tkinter import *
from tkinter import ttk
import schemeRake

class UploadFrame(Frame):

    question=""
    answer=""
    marks=0
    def __init__(self,master):
        super(UploadFrame,self).__init__(master)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.quesToAns={}
        Label(self,text="Enter question :",font="Helvetica 15 bold",anchor=NW)\
                        .pack(padx=40,fill=X)
        self.question=Text(self,width=450,height=2,wrap=WORD,font='Verdana 15')
        self.question.pack(padx=40,pady=15,fill=X)
        Label(self,text="Enter the Answer:",font="Helvetica 15 bold",anchor=NW)\
                        .pack(padx=40,fill=X)
        self.answer=Text(self,width=450,height=5,wrap=WORD,font='Verdana 15')
        self.answer.pack(padx=40,pady=20,fill=X)
        
        Label(self,text="Enter the Marks:",font="Helvetica 15 bold",anchor=NW)\
                        .pack(padx=40,fill=X)
        self.marks=Entry(self,width=450,font='Verdana 15')
        self.marks.pack(padx=40,pady=20,fill=X)
        
        Button(self,text='Add Question',width=15,font="Helvetica 15 bold",\
               height=1,anchor=CENTER,command=self.addQuestion).pack(padx=80,side=LEFT)
        Button(self,text='Done Uploading',width=15,font="Helvetica 15 bold",\
               height=1,anchor=CENTER,command=self.done).pack(padx=80,side=RIGHT)

    def addQuestion(self):
        schemeRake.recvInfo(self.question.get("1.0",'end-1c'),self.answer.get("1.0",'end-1c'),self.marks.get())
        print("hi")
        self.question.delete(0.0,END)
        self.answer.delete(0.0,END)
        self.marks.delete(0,END)

            
    def done(self):
        self.destroy()
        import home as h
        
root=Tk()
root.title('Upload Scheme')
root.geometry('700x500')
root.resizable(width=False,height=False)
root.configure(background='#ffffff')
root.style=ttk.Style()
root.style.theme_use('alt')
frame=UploadFrame(root)
root.mainloop()

        
        
        
