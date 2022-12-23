#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():

    while wall_is_above() == True or wall_is_beneath() == True:
        fill_cell()
        move_right()
    while wall_is_above() != True:
        move_right()        


if __name__ == '__main__':
    run_tasks()
