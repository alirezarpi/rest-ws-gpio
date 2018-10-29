import time
import RPi.GPIO as GPIO

###### INTIALIZATION ######

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

GPIO.output(40,0)
GPIO.output(38,0)
GPIO.output(36,0)

# Main
def gpio(port, status):
    GPIO.output(port, status)

def change_gpio(status):
    print("Status will be: " + str(status))
    if( status[0] == "1" ):
        gpio(36, 1)
    if( status[0] == "0" ):
        gpio(36, 0)
    if( status[1] == "1" ):
        gpio(38, 1)
    if( status[1] == "0" ):
        gpio(38, 0)
    if( status[2] == "1" ):
        gpio(40, 1)
    if( status[2] == "0" ):
        gpio(40, 0)
    return 0

def validate_data(data):
    if ((len(data)) == 3):
        for l in data:
            if(l == '0'):
                flag = True
            elif(l == '1'):
                flag = True
            else:
                flag = False
                break
    else:
        flag = False

    return flag

