from rrb3 import *
import time

rr = RRB3(6,6)

def forward(distance):
    rr.set_motors(0,0,1,0)
    time.sleep(distance)
    stop()
    
def backward(distance):
    rr.set_motors(0,0,1,1)
    time.sleep(distance)
    stop()
    
def left():
    rr.set_motors(0.5,0,0,0)
    time.sleep(1)
    stop()
    
def right():
    rr.set_motors(0.5,1,0,0)
    time.sleep(1)
    stop()
    
def stop():
    rr.set_motors(0,0,0,0)