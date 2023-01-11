#!/usr/bin/python3
import math

from pyrob.api import *


@task(delay=0.10)
def task_9_3():
    i = 0
    while not wall_is_beneath():
        i += 1
        move_down()
    j = math.floor(i/2)
    print(j)
    for k in range(j):
        turnover(i)
        turnover(i-2)
    while not wall_is_on_the_left() and  not wall_is_beneath():
        move_left()
        move_down()

def turnover(i):
    for j in range(i):
        if j != 0 and j != i:
            fill_cell()
        move_right()
    for j in range(i):
        if j != 0 and j != i:
            fill_cell()
        move_up()
    for j in range(i):
        if j != 0 and j != i:
            fill_cell()
        move_left()
    for j in range(i):
        if j != 0 and j != i:
            fill_cell()
        move_down()
    move_up()
    move_right()


if __name__ == '__main__':
    run_tasks()
