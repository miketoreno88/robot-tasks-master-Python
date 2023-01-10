#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_8_29():
    while not wall_is_on_the_left() and wall_is_above() is True: 
        move_left() 
    
    if wall_is_above() is True: 
        while wall_is_above() and not wall_is_on_the_right() is True: 
            move_right()
    
    while not wall_is_above() is True: 
        move_up() 
    
    if not wall_is_on_the_left() and not wall_is_beneath() is True: 
        while not wall_is_on_the_left() is True: 
            move_left()

if __name__ == '__main__':
    run_tasks()