#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while wall_is_on_the_right() is False:
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        elif wall_is_above() == False and wall_is_beneath() == False:
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()
        elif wall_is_above() == True:
            move_down(1)
            fill_cell()
            move_up()
        elif wall_is_above() == False:
            move_up()
            fill_cell()
            move_down()
        move_right()        

    if wall_is_above() and wall_is_beneath():
        fill_cell()
    elif wall_is_above() == False and wall_is_beneath() == False:
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        move_up()
    elif wall_is_above() == True:
        move_down(1)
        fill_cell()
        move_up()
    elif wall_is_above() == False:
        move_up()
        fill_cell()
        move_down()        




if __name__ == '__main__':
    run_tasks()
