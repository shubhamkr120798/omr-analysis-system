#Part 1

import cv2   #importing opencv
import numpy as np
from matplotlib import pyplot as plt
d = []

Error =[["ME3081","nope","ME3081","ME2081"],  #Hardcoded Error codes
        ["ME3081","ME3081","ME306","nope"],
        ["ME3081","nope","ME306","ME3081"],
        ["nope","ME3081","ME3081","ME2081"],
        ["ME3081","nope","ME3081","ME306"],
        
        ["ME3081","ME3081","ME306","ME306"],
        ["ME3062","nope","ME3081","ME306"],
        ["ME3062","nope","ME3081","ME306"],
        ["ME3081","ME3081","ME3062","nope"],
        
        ["ME3081","ME306","ME3062","nope"],
        ["ME3081","nope","ME3062","ME2081"],
        ["nope","ME3081","ME3081","ME3062"],
        ["ME3115","nope","nope","ME3110"],
        ["ME3115","nope","ME3110","ME3116"],
        
        ["ME3115","ME3116","nope","ME3110"],
        ["ME3115","nope","ME3116","ME3110"],
        ["nope","ME3110","ME3110","ME311"],
        ["ME3116","ME3115","ME311","nope"],
        ["nope","ME3116","ME3115","ME311"],
        
        ["ME3116","ME3115","ME3115","ME311"],
        ["nope","ME3116","ME3115","ME3111"],
        ["ME3110","ME2063","nope","ME3111"],
        ["nope","ME3110","ME311","ME311"]]


def getd():  
    Error1=Error[:]          
    img_rgb = cv2.imread('rss.jpg')  #Reading Main image
    
    img_rgb1 = cv2.imread('rss.jpg',0)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  #Converting to Gray Scale
            
    template1 = cv2.imread('Tick.JPG',0)  #Reading Template image
    #template2 = cv2.imread('Star.jpg',0)
    #template3 = cv2.imread('Cross.jpg',0)
            
    
    w, h = template1.shape[::-1]
    W, H = img_rgb1.shape[::-1]

    res = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)  #The opencv function used for templae matching
    
    threshold = 0.6   #The threshold we wnat to match these two images so higher the threshold, higher will be the similarity.
    
    #res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
    #res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)
                
    loc = np.where(res >= threshold)                                    #Making a boolean array of the sub images of the main image which
                                                                        #crosses the threshold similarity 
    #loc+=np.where(res2 >= threshold)+np.where(res3 >= threshold)       #threshold needs to be checked carefully as sometimes similar images may overshoot 
    #loc=np.argsort(loc, order=('y', 'x'))                              #and sometimes the just opposite. One can also write a function to gain the
                                                                        #threshold for each user.
    c=0        
    f=set()        
    for pt in zip(*loc[::-1]):
        if(len(d)>22):
            break
        
        if(pt[0]>=0 and pt[0]<=W/4):                                    #Main image is imagined to be divided in fours parts based on x-coordinate
            if(Error1[c][0]!=-1):
                d.append(Error1[c][0])
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)    #In First Part
                Error1[c][0]=-1
        elif(pt[0]>W/4 and pt[0]<=W/2):
             if(Error1[c][1]!=-1):
                d.append(Error1[c][1])
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)    #In Second Part
                Error1[c][1]=-1
        elif(pt[0]>W/2 and pt[0]<=(3*W)/4):
             if(Error1[c][2]!=-1):
                d.append(Error1[c][2])
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)    #In Third Part
                Error1[c][2]=-1
        elif(pt[0]>(3*W)/4 and pt[0]<=W):
             if(Error1[c][3]!=-1):
                d.append(Error1[c][3])
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)    #In Fourth Part
                Error1[c][3]=-1
        c+=1   
                   
    #So the errors have been stored in the d array
        
    dp={}     #Dictionary to find count of each error code, nope represents correct answer. 
    
    print(len(d))   #Number of different types of error codes
    
    for i in range(len(d)):
        #dp[d[i]]+=1
        dp[d[i]] = dp.get(d[i], 0) + 1   #Incrementing count of each error code by iterating d and keeping in dp
    
    for key, value in dp.items():        
        print(key," ",value)        #Printing the dictionary to print the corresponding error codes and their counts.
        
    cv2.imwrite('rss5.jpg',img_rgb)   #Writing the image with drawing a rectangle in the tick areas 
    return

#End of Part 1

getd()    #Utility Function for starting the whole process
