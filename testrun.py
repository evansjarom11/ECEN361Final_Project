from library import *
import os


forward(2)
time.sleep(4)
backward(2)
os.system('fswebcam -r 640x480 -S 10 --jpeg 95 --save /home/pi/im.jpg')
