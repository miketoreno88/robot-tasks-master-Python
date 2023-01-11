#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_4():
    for i in range(5):
        move_right(2)
        while not wall_is_on_the_right() is True:
            plus()
            move_right(4)
        plus()
        while not wall_is_on_the_left() is True:
            move_left()
        move_down(2)
        if not wall_is_beneath() is True:
            move_down(2)
        else:
            move_up(2)


def plus():
    move_left()
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
