#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_5_10():
    while not wall_is_beneath() is True:
        fill_cell()
        while not wall_is_on_the_right() is True:
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        while not wall_is_on_the_left() is True:
            fill_cell()
            move_left()
        fill_cell()
        if not wall_is_beneath() is True:
            move_down()
    while wall_is_beneath() and not wall_is_on_the_right() is True:
        fill_cell()
        move_right()
    fill_cell()
    while not wall_is_on_the_left() is True:
        move_left()


if __name__ == '__main__':
    run_tasks()
