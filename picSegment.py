import cv2
import numpy as np
from PIL import Image
import apiConvert

def segmentByPath(path):
    uploaded=path

    imgx = Image.open(uploaded)
    height,width=imgx.size
    coord=[(0,0)]

    img = cv2.imread(uploaded)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength=width
    maxLineGap=10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,width,minLineLength,maxLineGap)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
            coord.extend([(int(height),y2),(0,y1)])      #keep adding end coordinates of each line to the list

    coord.append((int(height),int(width)))
    coord.reverse()
    #start popping to obtain pairs of coordinates to crop
    x=1
    txtpaths=[]
    while coord!=[]:
        x2,y2=coord.pop()
        x1,y1=coord.pop()
        tup=(x2, y2, x1, y1)
        if y1-y2>10:                #to ensure that same line is not segmented
            img2 = imgx.crop(tup)
            name=uploaded[:-4]+"."+str(x)+uploaded[-4:]
            img2.save(name)
            txtpaths.append(apiConvert.recvimg(name))          #needs to be run on vm
            x=x+1

    return txtpaths

