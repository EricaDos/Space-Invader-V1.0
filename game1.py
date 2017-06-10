import turtle
import sys
import random
import math
import os

#Turtle Screen
scr = turtle.Screen()
scr.bgcolor("Black")
scr.tracer(3)
#Border
bord = turtle.Turtle()
bord.color("RED")
bord.penup()
bord.setposition(-270,-270)
bord.pendown()
bord.pensize(3)
for i in range(4):
    bord.forward(540)
    bord.left(90)
bord.hideturtle()
##sp = turtle.Turtle()
##sp.color("RED")
##sp.penup()
##sp.setposition(260,250)
##sp.pendown()
##sp.hideturtle()

                     

#Create Player
player = turtle.Turtle()
player.color("Yellow")
player.shape("triangle")
player.penup()
player.speed(0) #Fastest to prevent it from stopping
#Random location of enemy position to set
randomx = random.randint(-260,260)
randomy = random.randint(-260,260)
#Create enemy

maxEnemies = 10
ene = []

for count in range(maxEnemies):
    ene.append(turtle.Turtle())
    ene[count].color("blue")
    ene[count].pensize(5)
    ene[count].shape("circle")
    ene[count].penup()
    ene[count].speed(0)
    ene[count].setposition(random.randint(-270,270),random.randint(-270,270))

#Set speed variable
speed = 1
points = 0

#Keyboard Functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increaseSpeed():
    global speed
    speed += 1
def decreaseSpeed():
    global speed
    speed -= 1
    if speed <= 0:
        speed += 1
def isCollision(t1,t2):
    #Testing distance between enemy and player
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

def randcord(r):
        nrandomx = random.randint(-260,260)
        nrandomy = random.randint(-260,260)
        r.setposition(nrandomx,nrandomy)
        r.right(random.randint(0,260))
        
#Set keyboard assignment
turtle.listen()
turtle.onkey(turnleft,"Left") 
turtle.onkey(turnright,"Right")
turtle.onkey(increaseSpeed,"Up")
turtle.onkey(decreaseSpeed,"Down")

#Always keeps turtle moving at speed
while True:
    player.forward(speed)
    
    #Boundary checking
    if player.xcor() > 270 or player.xcor() < -270:
        player.right(180)
    
    if player.ycor() > 270 or player.ycor()< -270:
        player.right(180)
   
        
        
    for count in range(maxEnemies):
        ene[count].forward(3)
        #Boundary checking
        if ene[count].xcor() > 270 or ene[count].xcor() < -270:
            ene[count].right(180)
            
        if ene[count].ycor() > 250 or ene[count].ycor()< -250:
            ene[count].right(180)
            
            
        if isCollision(player,ene[count]):
            randcord(ene[count])
            if speed >= 4:
                points += 2
            else:
                points += 1
            bord.undo()
            bord.penup()
            bord.hideturtle()
            bord.setposition(-260,280)
            pointstr = ("Score: %s" %points)
            bord.write(pointstr, False, align="left", font=("Arial",15,"normal"))

##            sp.undo()
##            sp.penup()
##            sp.hideturtle()
##            sp.setposition(200,270)
##            speedstr = ("Speed: %s" %speed)
##            sp.write(speedstr, False, align="right", font=("Arial",15,"normal"))

    
#Delay
delay = raw_input("Press Enter to finish")
