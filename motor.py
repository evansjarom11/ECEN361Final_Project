import time
from rrb3 import *

rr = RRB3()

def left(angle):
    rr.set_motors(0, 0, 1, 1)
    time.sleep(2.3*angle/360)
    stop()

def right(angle):
    rr.set_motors(0, 0, 1, 0)
    time.sleep(2.1*angle/360)
    stop()

def forward(distance):
    rr.set_motors(1, 0, 0, 0)
    time.sleep(distance)
    stop()
    
def backward(distance):
    rr.set_motors(1, 1, 0, 0)
    time.sleep(distance)
    stop()

def stop():
    rr.set_motors(0, 0, 0, 0)
    