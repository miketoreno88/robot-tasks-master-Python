#!/usr/bin/python3
import math

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    i = 0
    while not wall_is_beneath():
        move_down()
        i += 1
        k = math.floor(i/2)
    for n in range(k):
        move('go_right', i-n*2)
        move('go_up', i-n*2)
        move('go_left', i-n*2)
        move('go_down', i-n*2)
        if n == k-1:
            while not wall_is_on_the_left():
                move_left()
                move_down()
        else:
            move_up()
            move_right()


def move(direction, i):        
    for k in range(i):
        if k != 0 and k != i:
            fill_cell()
        if direction == 'go_left':
            move_left()
        if direction == 'go_up':
            move_up()
        if direction == 'go_right':
            move_right()
        if direction == 'go_down':
            move_down()    
        


if __name__ == '__main__':
    run_tasks()
