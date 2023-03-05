from tkinter import *
from tkinter import ttk
import mongoInteract
import _pickle as pickle
import pprint

class QuestionsListFrame(Frame):

    listOfQuestions=[]
    listOfCheckBoxesVars=[]
    listOfSelectedQuestions=[]
    
    def __init__(self,master):
        super(QuestionsListFrame,self).__init__(master)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.pack(fill=BOTH)
        self.createWidgets(master)
        

    def createWidgets(self,master):
        self.sidebar = Frame(root, width=250, bg='white', height=500,\
                             relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=True, fill='both', side='left', anchor='nw')
        self.getQuestions()

        self.buttonbar = Frame(root, width=200, bg='white', height=500, borderwidth=2)
        self.buttonbar.pack(expand=True, fill='both', side='left', anchor='nw')

        Button(self.buttonbar,text='Select',width=10,font="Helvetica 15 bold",\
               height=1,anchor=CENTER,command=lambda:self.selectQuestions(master)).pack(pady=80,side=TOP)  

    def getQuestions(self):
        self.listOfQuestions = mongoInteract.recvAllFromDb()
        for q in self.listOfQuestions:
            self.listOfCheckBoxesVars.append(BooleanVar())
            Checkbutton(self.sidebar,text=q["question"],\
                        variable=self.listOfCheckBoxesVars[-1]).pack(side=TOP)

    def selectQuestions(self,master):
        for i in range(len(self.listOfCheckBoxesVars)):
            if self.listOfCheckBoxesVars[i].get():
                self.listOfSelectedQuestions.append(self.listOfQuestions[i])
        qpickle=pickle.dumps(self.listOfSelectedQuestions)
        qpaper=open("quespaper.txt","wb")
        qpaper.write(qpickle)
        qpaper.close()
        master.destroy()
        import studentSelect
            
        
root=Tk()
root.title('Select question paper')
root.geometry('700x500')
root.resizable(width=False,height=False)
root.configure(background='#ffffff')
root.style=ttk.Style()
root.style.theme_use('alt')
frame=QuestionsListFrame(root)
root.mainloop()
