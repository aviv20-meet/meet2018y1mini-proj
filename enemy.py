import turtle
import random
def enemy_start():
    SQUARE_SIZE = 20
    START_LENGTH = 10

    enemy = turtle.clone()
    enemy.goto(-200,-200)
    snake.shape("square")
    turtle.hideturtle()
    stamp_list = []
    for i  in range(START_LENGTH):
        x_pos=snake.pos()[0] 
        y_pos=snake.pos()[1]

      
        x_pos+=SQUARE_SIZE

        my_pos=(x_pos,y_pos) 
        snake.goto(x_pos,y_pos) 
       
       
        pos_list.append(my_pos) 

           
        stamp_ID = snake.stamp()
        stamp_list.append(stamp_ID)
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    direction = UP
    UP_EDGE = 340
    DOWN_EDGE = -340
    RIGHT_EDGE = 340
    LEFT_EDGE = -340
    TIME_STEP = 100
    TIME_STEP1 = 1000
    def move_enemy():
        my_pos = enemy.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        new_pos = enemy.pos()
        new_x_pos = new_pos[0]
        new_y_pos = new_pos[1]
        if new_x_pos >= RIGHT_EDGE:
            direction = LEFT
        elif new_x_pos <= LEFT_EDGE:
            direction = RIGHT
        elif new_y_pos <= DOWN_EDGE:
            direction = UP
        elif new_y_pos >= UP_EDGE:
            direction = DOWN
        
        if direction==RIGHT:
            enemy.goto(x_pos + SQUARE_SIZE, y_pos)
            print("The enemy moved right!")
        elif direction==LEFT:
            snake.goto(x_pos - SQUARE_SIZE, y_pos)
            print("The enemy moved left!")
        elif direction==UP:
            enemy.goto(x_pos, y_pos + SQUARE_SIZE)
            print("The enemy moved up!")
        elif direction==DOWN:
            enemy.goto(x_pos, y_pos - SQUARE_SIZE)
            print("The enemy moved down!")

        
        my_pos=enemy.pos() 
        pos_list.append(my_pos)
        new_stamp = enemy.stamp()
        stamp_list.append(new_stamp)
        
        enemy.towards(snake.pos)
        turtle.ontimer(move_enemy, TIME_STEP)
