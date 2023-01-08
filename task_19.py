#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():



    direction = -1
    if direction == -1:
        while wall_is_on_the_left() == False:
            move_left()
            if wall_is_on_the_left() == True and wall_is_above() == False:
                go_home()
            elif wall_is_on_the_left() == True and wall_is_above() == True:
                direction = 1    


    if direction == 1:
        while wall_is_on_the_right() == False:        
            move_right()
            if wall_is_on_the_right() == True and wall_is_above() == False:
                direction = 0
                go_home()
            
def go_home():
    while wall_is_above() == False:
        move_up()
    while wall_is_on_the_left() == False:
        move_left()                
            

    
    # while wall_is_above() == True:
    #     if wall_is_on_the_left() == True: 
    #         direction = 1
    #     if wall_is_on_the_right() == True:
    #         direction = 0
    #     if direction == -1:
    #         move_left()
    #     elif direction == 1:
    #         move_right()
    #     elif direction == 0:    
    #         move_left(0)
    # while wall_is_above() == False:
    #     move_up()
    # while wall_is_on_the_left() ==False:
    #     move_left()     
        


if __name__ == '__main__':
    run_tasks()







