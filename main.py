from brightness import led_power
from yolo import yolo
import cv2



vid = cv2.VideoCapture(0) 

capturing = True  
while(capturing): 
      
    ret, frame = vid.read() 
    capturing = False

vid.release() 
cv2.destroyAllWindows() 



power = led_power(frame)
LABELS, classIDs = yolo(frame)


def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False


objects = []
for i in range(len(classIDs)):
    objects.append(LABELS[classIDs[i]])

classes = ['person', 'bicycle', 'car', 'motorbike', 'bus', 'truck']

print(objects)

if(common_member(objects, classes)):
    ON(power)
else:
    OFF()
