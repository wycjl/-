
import cv2

#vc = cv2.VideoCapture(r'E:\嘉善治水视频\罗星街道\4柳洲桥港.MOV') #读入视频文件
vc = cv2.VideoCapture(r'E:\处理完视频\18.5.18 嘉善塘 H200 S10 变焦X2 去段.mp4') #读入视频文件
print(vc)
c=0

rval=vc.isOpened()

timeF = 20  #视频帧计数间隔频率

while rval:   #循环读取视频帧
	
    c = c + 1
    rval, frame = vc.read()
    print(c)
    if(c%timeF == 0): #每隔timeF帧进行存储操作

        cv2.imwrite('c/c'+str(c) + '.jpg', frame) #存储为图像
#    if rval:

	    #img为当前目录下新建的文件夹
 #       cv2.imwrite('img/'+str(c) + '.jpg', frame) #存储为图像
  #      cv2.waitKey(1)
   # else:
    #    break
vc.release()
