import RPI.GPIO as GPIO


def init():

    GPIO.setmode(GPIO.BOARD)

    # voltage pin
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    
    # ground pin
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.LOW)

    return [2, 3, 4, 5]


def ON(power, pins):
    for i in range(len(pins)-1):
        GPIO.PWM(pins[i], power)

def OFF(pins):
    for i in range(len(pins)-1):
        GPIO.PWN(pins[i], 0)





