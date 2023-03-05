from rake_nltk import Rake
import mongoInteract
from tkinter import *

def recvInfo(ques,ans,marks):
    
    r=Rake()
    r.extract_keywords_from_text(ans)
    scheme=r.get_ranked_phrases_with_scores()
    newid=mongoInteract.findLastId()+1
    dbscheme={}

    for pair in scheme:
        key=""
        for c in pair[1]:
            if not (c.isalnum() or c==' '):
                continue
            key=key+c
        if key!='':
            dbscheme[key]=pair[0]

    
    def changeDict():
        newdbscheme={}
        for i in range(len(dbscheme)):
            if listofKeyEntries[i].get()=="" or listofWeightEntries[i].get()=="":
                continue
            newdbscheme[listofKeyEntries[i].get()]=listofWeightEntries[i].get()
        schemeChecker.destroy()
        newdbscheme["_id"]=newid
        newdbscheme["question"]=ques
        newdbscheme["marks"]=float(marks)
        mongoInteract.sendToDb(newdbscheme)

    schemeChecker = Toplevel()
    schemeChecker.title("Edit Scheme")
    schemeChecker.configure(background='#ffffff')


    #dbscheme={"Zero-Drift":4,"Sensitivity":9,"MinValue":6,"Accuracy":9,"Precision":9,"Zero-Offset":7,"Range":9}
    length='500x'+str(len(dbscheme)*20+70)
    schemeChecker.geometry(length)

    listofKeyEntries=[]
    listofWeightEntries=[]
    xo=20
    yo=20

    for key in dbscheme:
        entry = Entry(schemeChecker,width=400)
        entry.place(x=xo,y=yo)
        entry.insert(0,key)
        listofKeyEntries.append(entry)
        entry = Entry(schemeChecker,width=30)
        entry.place(x=xo+350,y=yo)
        entry.insert(0,dbscheme[key])
        listofWeightEntries.append(entry)
        yo += 20
    newdbscheme={}

    Button(schemeChecker,text="DONE",anchor=CENTER,width=20,height=2,\
           command=changeDict).pack(anchor=S,side=BOTTOM)
    schemeChecker.mainloop()
 #to be removed

if __name__=="__main__":
    recvInfo()
