from tkinter import *
from tkinter import ttk

class KeywordPane(Frame):
    
    unmatched=[]
    extra=[]
    dict1={} #matched
    dict2={} #unmatched from scheme
    noMatch={} #extra in answer
    marks=0
    
    def __init__(self,master,addedset, removeddict, samedict,marks):
        super(KeywordPane,self).__init__(master)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.pack(fill=BOTH,expand=1)
        self.dict1=samedict
        self.dict2=removeddict
        self.noMatch=addedset
        self.marks=marks
        self.master=master
        #print(self.dict1)
        #print(self.dict2)
        #print(self.noMatch)
        #print(self.marks)
        self.createWidgets(addedset, removeddict, samedict,marks)

    def createWidgets(self,noMatch,dict2,dict1,marks):
        self.MatchedKeywords=LabelFrame(self,text="Matched Keywords")
        self.MatchedKeywords.pack(padx=10,pady=10,fill=X)
        for key in dict1.keys():
            Label(self.MatchedKeywords,text=key,\
                  font="Helvetica 10 bold").pack(side=TOP,anchor=NW)
            
        self.UnMatchedKeywords=LabelFrame(self,text="Un-matched Keywords",width=300)
        self.UnMatchedKeywords.pack(padx=10,pady=10,side=LEFT,fill=BOTH)
        self.givenKey=StringVar()
        self.givenKey.set(None)
        for key in dict2.keys():
            Radiobutton(self.UnMatchedKeywords,text=key,\
              font="Helvetica 10 bold",value=key,variable=self.givenKey).pack(anchor=NW,fill=X)
        self.extraKeywords=LabelFrame(self,text="Extra Keywords",width=300)
        self.extraKeywords.pack(padx=10,pady=10,fill=BOTH,side=RIGHT)
        self.obtainedKey=StringVar()
        self.obtainedKey.set(None)
        for key in noMatch:
            Radiobutton(self.extraKeywords,text=key,\
              font="Helvetica 10 bold",value=key,variable=self.obtainedKey).pack(anchor=NW,fill=X)
        #self.buttonFrame=LabelFrame(self,width=600,height=1).pack(fill=BOTH,anchor=S)
        Button(self,text="MATCH",font="Helvetica 15 bold"\
               ,anchor=CENTER,height=1,command=lambda:self.matchKeys(dict1,dict2,noMatch)).pack(side=TOP,padx=50,pady=30)
        Button(self,text="DONE",font="Helvetica 15 bold",anchor=CENTER,\
               height=1,command=self.doneMapping).pack(side=TOP,padx=50,pady=30)
          
    def matchKeys(self,dict1,dict2,noMatch):
        weight = dict2.pop(self.givenKey.get())
        dict1[self.givenKey.get()]=weight
        noMatch.remove(self.obtainedKey.get())
        print(dict1)
        print(dict2)
        print(noMatch)

    def doneMapping(self): #write coding for grading here. Ref dictionary is dict1
        self.destroy()
        self.master.destroy()


