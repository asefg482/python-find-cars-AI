import cv2
Cap = cv2.VideoCapture('Video.avi');
Car_Cas_Cade = cv2.CascodeClassifier('Cars.xml')
while True:
    Ret,Frames = Cap.read()
    Gray  = cv2.cvtColor(Frames,cv2.COLOR_BGR2GRAY)
    Cars = Car_Cas_Cade.detectMultiScale(Gray,1.1,1)
    for (x,y,w,h) in Cars:
        cv2.rectangle(Frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('Video',Frames)
        if cv2.waitKey(33) == 27:
            break
cv2.destroyAllWindows()