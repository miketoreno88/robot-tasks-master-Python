#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_6_6():
    while not wall_is_on_the_right() is True:
        move_right()
        while not  wall_is_above() is True:
            move_up()
            fill_cell()
        while not wall_is_beneath() is True:
            move_down()
    while wall_is_beneath() is True:
        move_left()


if __name__ == '__main__':
    run_tasks()
