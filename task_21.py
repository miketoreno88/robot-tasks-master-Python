#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range(6):
        for j in range(13-i*2):
            move_down()
            move_right()
            fill_cell()
        for j in range(12-i*2):
            move_left()
            fill_cell() 
            move_up()
        move_down()
        move_left()  
    move_down()
    move_right()
    fill_cell()
    move_down()
    



    # move_right()
    # move_down()
    # for i in range(12):
    #     move_right()

    #     for j in range(13-i):
    #         fill_cell()
    #         move_down()
    #     move_right()
    #     for j in range(12-i):
    #         move_up()
    #         fill_cell()

            
        



    # for i in range(13):
    #     move_right()
    #     move_down()
    #     fill_cell()
    # for i in range(12):    
    #     move_left()    
    #     fill_cell()
    #     move_up()


if __name__ == '__main__':
    run_tasks()
