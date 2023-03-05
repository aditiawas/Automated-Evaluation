from tkinter import *
import easygui
import os
import shutil
import studentMongoInteract
import picSegment
import answerRake
import _pickle as pickle

allpaths=[]
filePathList = []
students = studentMongoInteract.recvAllFromDb()
class Tapp(Frame):
        def __init__(self,master):
                super(Tapp,self).__init__(master)
                self.pack()
                self.wid()
                
        def wid(self):
                self.id=StringVar()
                self.id.set(None)

                self.sidebar = Frame(self, bg='white', width=400,height=500,\
                             relief='sunken', borderwidth=2)
                self.sidebar.pack(expand=True, fill='both', side='left', anchor='nw')
                
                for student in students:
                        Radiobutton(self.sidebar,text=student["USN"],variable=self.id,\
                                    value=student["_id"]).pack(padx=40,fill=X)
                Button(self,text="Browse", command= self.gui).pack(padx=30,pady=30,side=TOP)

                Button(self,text="Evaluate", command= self.evaluate).pack(padx=30,pady=30,side=TOP)
                
        def gui(self):
                x=easygui.fileopenbox()
                n=x.rfind('\\')
                pathstring = x[:n+1]
                iden = self.id.get()

                dirs = os.listdir(pathstring)           
                for file in dirs:
                        newFileName = "st"+iden+"_"+str(file)
                        filepath = os.path.join(pathstring,file)
                        newfilepath = os.path.join(pathstring,newFileName)
                        os.rename(filepath,newfilepath)
                        filePathList.append(newfilepath)
                self.segmentAll(filePathList)
                
        def segmentAll(self,pathList):
                for path in pathList:
                        #picSegment.segmentByPath(path)
                        txt=picSegment.segmentByPath(path)
                        allpaths.extend(txt)
                print(allpaths)

        def evaluate(self):
                quespaper=open("quespaper.txt","rb")
                ques = pickle.loads(quespaper.read())
                marks=0
                maxmarks=0
                for i in range(len(allpaths)):
                        marks=marks+answerRake.recvInfo(ques[i],allpaths[i])        #get ques[i] from somewhere
                        maxmarks=maxmarks+float(ques[i]["marks"])
                        print(marks,maxmarks)
                top = Toplevel()
                top.title("Total Marks")
                msg = Message(top, text="You got "+str(marks)+" out of "+str(maxmarks))
                msg.pack()
                button = Button(top, text="Dismiss", command=top.destroy)
                button.pack()

r2=Tk()
r2.title("Upload Student Answer Script")
a=Tapp(r2)
r2.mainloop()
