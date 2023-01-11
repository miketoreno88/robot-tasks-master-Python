#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 1
    move_right()
    fill_cell()
    while not wall_is_on_the_right() is True:
        for j in range(i):
            if not wall_is_on_the_right() is True:
                move_right()
        if not wall_is_on_the_right() is True:
            fill_cell()
        i = i + 1


if __name__ == '__main__':
    run_tasks()
