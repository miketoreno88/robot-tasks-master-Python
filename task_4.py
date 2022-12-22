#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    toreno()

    if wall_is_above() == True and wall_is_beneath() == True:
            if wall_is_on_the_left() == True:
                move_right(1)  
            if wall_is_on_the_right() == True:
                move_left(1) 

    if wall_is_on_the_left() == True and wall_is_on_the_right() == True:
            if wall_is_above() == True:
                move_down(1)  
            if wall_is_beneath() == True:
                move_up(1) 

def toreno():
    print("toreno")                



if __name__ == '__main__':
    run_tasks()
