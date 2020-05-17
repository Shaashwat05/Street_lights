import cv2
import numpy as np
#import RPI.GPIO as GPIO


def led_power(img_rgb):
    #img_rgb = cv2.imread("gallery/bright.jpg")

    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

    #img_hsv[:, :, 2] = 40
    #print(img_hsv)

    #l = img_hsv.tolist()
    #x = pd.Series(l)
    #x.to_excel('bright.xlsx')


    avg_saturation = np.mean(img_hsv[:, :,1])

    avg_value = np.mean(img_hsv[:, :, 2])

    print(avg_saturation, avg_value)

    #led_val = (((avg_value/(6*255)) + (avg_saturation/(2*255)))/(263.75/255))*255

    #led_val = 255 - led_val

    led_val = (255-(avg_value/1.2)-(avg_saturation/4))

    if(led_val <130):
        power = 0
    else:
        print(led_val)
        power = ((led_val-100)/125) *255

    print(power)


    #img_rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    #cv2.imshow("img", img_rgb)

    #cv2.waitKey(0)

    return power