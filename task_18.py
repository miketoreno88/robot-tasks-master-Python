#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    direction = -1
    while wall_is_above() == True:
        if wall_is_on_the_left() == True: 
            print('ky')
            direction = 1
        if direction == -1:
            move_left()
        elif direction == 1:
            move_right()
    while wall_is_above() == False:
        move_up()
    while wall_is_on_the_left() ==False:
        move_left()           

if __name__ == '__main__':
    run_tasks()
