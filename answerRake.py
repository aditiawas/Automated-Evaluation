from rake_nltk import Rake
import mongoInteract
import marksCalculator
from tkinter import *


def dict_compare(li, d2):
    d1_keys = set(li)
    d2_keys = set(d2.keys())
    sameset = d1_keys.intersection(d2_keys)
    addedset = d1_keys - d2_keys
    removedset = d2_keys - d1_keys
    samedict={}
    removeddict={}
    for key in sameset:
        samedict[key]=d2[key]
    for key in removedset:
        removeddict[key]=d2[key]
    return addedset, removeddict, samedict

def recvInfo(ques,answer):   
    r=Rake()
    ans2=open(answer,"r")
    ans=ans2.read()
    r.extract_keywords_from_text(ans)
    ansScript=[i[1] for i in r.get_ranked_phrases_with_scores()]
    scheme=mongoInteract.recvFromDb(ques["_id"])
    addedset, removeddict, samedict=dict_compare(ansScript,scheme)  #extra, missing, present (in this order)
    import keywordMatcher
    root=Toplevel()
    root.title("Keyword Matcher")
    root.geometry('700x500')
    root.resizable(width=False,height=False)
    root.configure(background='#ffffff')
    frame=keywordMatcher.KeywordPane(root,addedset, removeddict, samedict,float(ques["marks"]))
    root.mainloop()
    return(marksCalculator.calc(removeddict, samedict, float(ques["marks"])))
    
    
if __name__=="__main__":
    print(recvInfo(1,"averageAnswer.txt"))
    #print(dict_compare(['a','b','c'],{'a':12,'b':13,'d':14}))
