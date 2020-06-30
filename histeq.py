import cv2
import numpy as np
import matplotlib.pyplot as plt


I=cv2.imread("leena.jpg",0)
a=np.shape((I))

hist=np.zeros(256)
for i in range (a[0]):
    for j in range (a[1]):
        hist[I[i,j]]+=1
plt.plot(hist)

chist=np.zeros(256)
for i in range(len(hist)):
    if i==0:
        chist[i]=hist[i]
    else:
        chist[i]=hist[i]+chist[i-1]
plt.plot(chist)

for i in range(len(chist)):
    if chist[i]!=0:
        m=i
        break
LT=np.zeros(256)
for k in range (m,256):
    LT[k]=((chist[k]-chist[m])/(chist[255]-chist[m]))
LT=LT*255

I1=np.zeros((a[0],a[1]),dtype='uint8')
for i in range (a[0]):
    for j in range (a[1]):
        I1[i][j]=np.ceil(LT[I[i][j]])

cv2.imwrite('equized.jpeg',I1)


nhist=np.zeros(256)
for i in range (a[0]):
    for j in range (a[1]):
        nhist[I1[i,j]]+=1
plt.plot(hist)