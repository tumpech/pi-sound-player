#!/home/pi/project/venv/bin/python
from omxplayer.player import OMXPlayer
import RPi.GPIO as GPIO
from time import sleep
import signal

GPIO.cleanup()

def handler(signum, stack_frame):
    try:
        player1.quit()
    except:
        pass
    try:
        player2.quit()
    except:
        pass
    try:
        player3.quit()
    except:
        pass
    try:
        GPIO.cleanup()
    except:
        pass

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

LED = 18
SWITCH_1 = 17
SWITCH_2 = 27
SWITCH_3 = 22
#SWITCH_3 = 25

if __name__ == "__main__":
    MP3_1_PATH = "/home/pi/project/1.mp3"
    MP3_2_PATH = "/home/pi/project/2.mp3"
    MP3_3_PATH = "/home/pi/project/3.mp3"

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED,GPIO.HIGH)

    GPIO.setup(SWITCH_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_3,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    c1, c2, c3 = True, True, True

    while True:
        try:
            input_state_1 = GPIO.input(SWITCH_1)
            if c1 and not input_state_1:
                player1 = OMXPlayer(MP3_1_PATH,dbus_name='org.mpris.MediaPlayer2.omxplayer1')
                c1 = False
    
            input_state_2 = GPIO.input(SWITCH_2)
            if c2 and not input_state_2:
                player2 = OMXPlayer(MP3_2_PATH,dbus_name='org.mpris.MediaPlayer2.omxplayer2')
                c2 = False
    
            input_state_3 = GPIO.input(SWITCH_3)
            if c3 and not input_state_3:
                player3 = OMXPlayer(MP3_3_PATH,dbus_name='org.mpris.MediaPlayer2.omxplayer3')
                c3 = False
        except Exception as e:
             GPIO.cleanup()
             print(e)
             exit()



    exit()

