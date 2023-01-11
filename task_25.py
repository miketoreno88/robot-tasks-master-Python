#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right(2)
    while not wall_is_on_the_right() is True:
        plus()
        move_right(4)
    plus()
    move_left(2)
    move_down()



def plus():
    move_left()
    move_down()
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
    move_up(2)


if __name__ == '__main__':
    run_tasks()
