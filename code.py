import os
import cv2
import numpy as np
os.chdir('C:\\Users\Arush\Desktop\cdac\Code\mycode\Images')
#image=cv2.imread("in000001.jpg")
#pixel=image[300,200] /height*width

name="in00"
tempname=name

image2 = np.zeros((240,320,1), np.uint8)
tensor= np.zeros((240,320,200), np.uint8)        #Here@@@@@@@@@@
fmedian=np.zeros((240,320,1), np.uint8)


for x in range(1,201):                                         #Here@@@@@@@@@@
	y=str(x)
	if(len(y)==1):
		y='000'+y
	elif(len(y)==2):
		y='00'+y
	elif(len(y)==3):
		y='0'+y
	
	tempname=tempname+y+'.jpg'
	
	print tempname

	image=cv2.imread(tempname)
	avg=0
	for i in range(0,240):
		for j in range(0,320):
			image2[i,j]=(image[i,j][0]*0.299+image[i,j][0]*0.587+image[i,j][0]*0.114)
			tensor[i,j,x-1]=(image[i,j][0]*0.299+image[i,j][0]*0.587+image[i,j][0]*0.114)
			#print tensor[i,j][x-1]
	
	tempname=name
	
a=[]
for i in range(0,240):
	for j in range(0,320):
		for k in range(0,200):               #Here@@@@@@@@@@@@@
			a.append(tensor[i,j,k])	
		fmedian[i,j]=np.median(a)
		a=[]
#print image2

#print fmedian
cv2.imshow('Output',fmedian)
#cv2.imshow('Output',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('background.png',fmedian)	
	
	
	
	