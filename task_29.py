#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_7():
    i = 0
    while not wall_is_on_the_right() is True:
        move_right()
        if cell_is_filled() is True:
            i += 1
        else:
            i = 0
        if i == 3:
            break


if __name__ == '__main__':
    run_tasks()