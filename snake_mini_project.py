# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle 
import random
turtle.tracer(1,0) 
SIZE_X=900
SIZE_Y=900
turtle.setup(SIZE_X, SIZE_Y)
turtle.bgcolor("light green")

SQUARE_SIZE = 20
START_LENGTH = 10
score = 0

score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.goto(-250,200)
score_turtle.hideturtle()
square = turtle.Turtle()
square.shape("blank")
square.speed(5)
square.penup()
square.goto(-350,-350)
square.pendown()
square.pensize(5)
for i in range(4):
    square.forward(700)
    square.left(90)
turtle.penup()
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.goto(0,0)
snake.shape("square")
turtle.hideturtle()
for i  in range(START_LENGTH):
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

  
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos) 
   
   
    pos_list.append(my_pos) 

       
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)
    

UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100 
SPACEBAR = "space" 

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


direction = UP
UP_EDGE = 340
DOWN_EDGE = -340
RIGHT_EDGE = 340
LEFT_EDGE = -340


def up():
    global direction 
    direction=UP 
    print("You pressed the up key!")


def down():
    global direction 
    direction=DOWN
    print("You pressed the down key!")

def left():
    global direction 
    direction=LEFT
    print("You pressed the left key!")

def right():
    global direction 
    direction=RIGHT
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
def make_score():
    score_turtle.clear()
    score_turtle.write(score, move=False, align = 'left' , font=("fantasy", 24, "normal"))
    score_turtle.color("purple")
def make_food():
    min_x=-int(650/2/SQUARE_SIZE)+1
    max_x=int(650/2/SQUARE_SIZE)-1
    min_y=-int(650/2/SQUARE_SIZE)-1
    max_y=int(650/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    stamp=food.stamp()
    food_stamps.append(stamp)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
def move_snake():
    color_list = ['red','blue','green', 'yellow' , 'purple' ,'orange','pink','light blue','violet','lime','navy','crimson']
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit the bottom! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("you hit the top! Game over!")
        quit()
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        snake.color(color_list[random.randint(0,len(color_list)-1)])
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
        snake.color(color_list[random.randint(0,len(color_list)-1)])
        
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        snake.color(color_list[random.randint(0,len(color_list)-1)])
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        snake.color(color_list[random.randint(0,len(color_list)-1)])
        print("You moved down!")
    #for i in range(len(pos_list)):
    if snake.pos() in pos_list[:-1]:
        quit()

    
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    
    
    
    global score
    
    turtle.ontimer(move_snake,TIME_STEP)
    if len(food_stamps) <= 6:
        make_food()
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eatan the food")
        score +=1
        make_food()
        make_score()
    else:
        pos_list.pop(0)
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for i in food_pos:
    food.goto(i[0], i[1])
    stamp=food.stamp()
    food_stamps.append(stamp)
    '''
def enemy():
    SQUARE_SIZE = 20
    START_LENGTH = 1

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
    direction= UP
    UP_EDGE = 340
    DOWN_EDGE = -340
    RIGHT_EDGE = 340
    LEFT_EDGE = -340
    TIME_STEP = 100
    TIME_STEP1 = 1000

    def move_enemy():
        global direction
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
        
        enemy.towards(snake.pos())
        turtle.ontimer(move_enemy, TIME_STEP)
    move_enemy()
enemy()
'''
move_snake()
