import os
import cv2
import numpy as np
os.chdir('C:\\Users\Arush\Desktop\cdac\Code\mycode\Images\Output')
background=cv2.imread("background.png",-1)
#pixel=image[300,200] /height*width

name="in00"
tempname=name

threshold=20                                # threshold for error
error=0


foreground = np.zeros((240,320,3), np.uint8)

for i in range(1,211):
	os.chdir('C:\\Users\Arush\Desktop\cdac\Code\mycode\Images')
	y=str(i)
	tempname=name
	if(len(y)==1):
		y='000'+y
	elif(len(y)==2):
		y='00'+y
	elif(len(y)==3):
		y='0'+y
	
	tempname=tempname+y+'.jpg'
	
	print tempname
	image=cv2.imread(tempname)
	
	for x in range(0,240):
		for y in range(0,320):
			error=abs((image[x,y][0]*0.299+image[x,y][0]*0.587+image[x,y][0]*0.114) - (background[x,y]))
	
			#if(((float(error/background[x,y]))*100)>=threshold):
			#	foreground[x,y]=250
			#else:
			#	foreground[x,y]=0

			if(((float(error/background[x,y]))*100)<threshold):
				foreground[x,y]=[0,0,0]
			else:
				foreground[x,y]=image[x,y]

	os.chdir('C:\\Users\Arush\Desktop\cdac\Code\mycode\Images\Output')
	cv2.imwrite(tempname,foreground)
	

