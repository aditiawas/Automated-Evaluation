from tkinter import *
import studentMongoInteract

def getUSN():
    usn=entry.get()
    m=re.match("1BM[0-9]{2}[A-Z]{2}[0-9]{3}\Z",usn)
    if m:
        studentAdd.destroy()
        studentMongoInteract.sendToDb(usn)
    else:
        lbl['text']="please enter valid USN"
        lbl.place(x=5,y=45)
        #lbl.pack()

    
    
usn=""
studentAdd = Tk()
studentAdd.title("Add Student")
studentAdd.configure(background='#ffffff')
studentAdd.geometry('150x100')

Label(studentAdd,text="Enter the USN :").pack()
entry = Entry(studentAdd,width=40)
entry.place(x=5,y=25)

lbl=Label(studentAdd,width=100,height=1,anchor=CENTER,text="")
Button(studentAdd,text="DONE",anchor=CENTER,width=20,height=2,\
       command=getUSN).pack(side=BOTTOM,anchor=S)




