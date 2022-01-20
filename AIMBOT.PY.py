import pyautogui
import keyboard
import cv2
import numpy as np
import sys


pyautogui.position(280,640)
while True:

    if keyboard.is_pressed('q'):
        i=1
        l=[]
        while True:

            print(pyautogui.position())
            img = pyautogui.screenshot()
            open_cv_image = np.array(img)
# Convert RGB to BGR
            open_cv_image = cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)
            cropped_image = open_cv_image[300:800, 650:1150]
            #imgHSV = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
            #imgGrey=cv2.cvtColor(imgHSV,cv2.COLOR_BGR2GRAY)
            haystack_img = open_cv_image
            imgBlur=cv2.GaussianBlur(haystack_img,(1,1),0)
            imgGrey=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
            circles=cv2.HoughCircles(imgGrey,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=24,maxRadius=30)
            if i==10:
                l =[]
                i=1
            if circles is not None:
                i=i+1
                detected_circles = np.uint16(np.around(circles))
                for (x,y,r) in detected_circles[0,:]:

                    cv2.circle(haystack_img,(x,y),r,(0,255,0),1)
                    l1 = [x,y,r]
                    if(l1 in l)==False:
                        pyautogui.leftClick(x,y)

                        l.append(l1)

            #needle_img=cv2.imread('Resources/player.png')
            #needle_img1=cv2.imread('Resources/player1.png')
            #needle_img2=cv2.imread('Resources/target.png')
            #result = cv2.matchTemplate(haystack_img,needle_img,cv2.TM_CCOEFF_NORMED)
            #res1=cv2.matchTemplate(haystack_img,needle_img1,cv2.TM_CCOEFF_NORMED)
            #res2=cv2.matchTemplate(haystack_img,needle_img2,cv2.TM_CCOEFF_NORMED)
            #min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)
            #min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
            #min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

            #conf=0.8
            #bottom_left=max_loc[0]+needle_img.shape[0]
            #bottom_right=max_loc[1]+needle_img.shape[1]
            #bottom_left1 = max_loc1[0] + needle_img1.shape[0]
            #bottom_right1 = max_loc1[1] + needle_img1.shape[1]
            #bottom_left2 = max_loc2[0] + needle_img2.shape[0]
            #bottom_right2 = max_loc2[1] + needle_img2.shape[1]

            #if max_val>conf:
                #cv2.rectangle(haystack_img,max_loc,(bottom_left,bottom_right),(0,255,0),2)
            #if max_val1>conf:
                #cv2.rectangle(haystack_img, max_loc1, (bottom_left1, bottom_right1), (0, 255, 0), 2)
            #if max_val2>conf:
                #cv2.rectangle(haystack_img, max_loc2, (bottom_left2, bottom_right2), (0, 255, 0), 2)



            #imgBlur=cv2.GaussianBlur(imgGrey,(1,1),1)
            #imgCanny=cv2.Canny(imgBlur,150,300)
            #imgCropped =open_cv_image[400:800][0:500]
#imgResize= cv2.resize(imgCropped,(720,1280))
            #cv2.imshow('image',open_cv_image)
            #cv2.imshow('crp',cropped_image)
            #cv2.imshow('canny',imgCanny)
            #cv2.imshow('blr',imgBlur)
            #cv2.imshow('hsv',imgHSV)
            #cv2.imshow('result',res2)
            cv2.imshow('fin',haystack_img)
#cv2.imshow('imagecrp',imgCropped)q
#cv2.imshow('imagecrp1',imgResize)q
            cv2.waitKey(1)