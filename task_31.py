#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while not wall_is_on_the_left() or not wall_is_beneath():
        while not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()
            flag_left = True
        while not wall_is_beneath():
            move_down()
            flag_left = False
            flag_right = False
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                move_down()
            flag_right = True
        if flag_right == True and flag_left == True:
            while not wall_is_on_the_left():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
