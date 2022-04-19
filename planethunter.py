#Planethunder Game
#Written by Iniyan. Supported by Jayakumar

#imports
import turtle
import winsound
import random
import time
import os
#screen
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
#screen.tracer(0)
Description = ["Mars","Jupiter","Saturn","Uranus","Neptune"]
planets = ["mars.gif","jupiter.gif","saturn.gif","uranus.gif","neptune.gif"]

#starting index for planet
iPlanetCounter = 0


for plim in planets:
    screen.addshape(plim)
    
timer = turtle.Turtle() #instantiates a Turtle object from the Turtle class.
timer.hideturtle() #hides the turtle
timer.penup() #stops the turtle from drawing a line whenever moving
timer.goto(130,180) #moves the turtle to the top right corner of the screen
timer.color("blue")
timer.write("Planet names: ", align ="left", font=("Courier",15,"bold")) #displays the time limit
timer.goto(300,180)
timer.write(Description[iPlanetCounter], align ="left", font=("Courier", 15,"bold"))


screen.addshape("boy.gif")

#global variables
score = 0
isGameOn = 1

#score turtle
sturtle = turtle.Turtle()
sturtle.hideturtle()
sturtle.penup()
sturtle.goto(-300,180)
sturtle.pendown()
sturtle.color("blue")

sturtle.write("score:",align ="left", font=("Courier",15,"bold"))
#sturtle = turtle.Turtle()
sturtle.penup()
sturtle.goto(-190,180)
sturtle.pendown()
sturtle.color("blue")

sturtle.write("0",align ="right", font=("Courier",15,"bold"))
#timer turtle


#player fox turtle
fox = turtle.Turtle() # instantiates a Turtle object from the Turtle class into fox
fox.shape("boy.gif") # sets the shape of the turtle to fox.png
fox.resizemode("auto")
fox.penup() # stops the turtle from drawing a line whenever moving
fox.speed(0) # sets the turtle’s speed to ‘fastest’
fox.goto(-200,-200)
#planet turtle
planet = turtle.Turtle() # instantiates a Turtle object from the Turtle class into fox

planet.shape(planets[iPlanetCounter]) # sets the shape of the turtle to fox.png
planet.resizemode("auto")
planet.penup() # stops the turtle from drawing a line whenever moving
#planet.circle(-1000)
#planet.pendown()

# def functions
def updatescore():
    sturtle.undo()
    sturtle.write(score,align ="right", font=("Courier",15,"bold"))
    timer.undo()
    timer.write(Description[iPlanetCounter], align ="left", font=("Courier", 15,"bold"))
    


def mr():    
    currentHeading =fox.heading()
    fox.setheading(0)
    fox.forward(50)
    fox.setheading(currentHeading)
    areTheyTouching()

    
def ml():
    currentHeading =fox.heading()
    fox.setheading(180)
    fox.forward(50)
    fox.setheading(currentHeading)
    areTheyTouching()
    
def mu():
    currentHeading =fox.heading()
    fox.setheading(90)
    fox.forward(50)
    fox.setheading(currentHeading)
    areTheyTouching()
    
def md():
    currentHeading =fox.heading()
    fox.setheading(270)
    fox.forward(50)
    fox.setheading(currentHeading)
    areTheyTouching()

def changeplanet():
    global iPlanetCounter
    global isGameOn
    iPlanetCounter=iPlanetCounter+1
    print("Planet is ..."+planets[iPlanetCounter] +" -> "+Description[iPlanetCounter])
    planet.shape(planets[iPlanetCounter])
    winsound.PlaySound("hunted.wav",winsound.SND_ASYNC)
    if(iPlanetCounter >= 4) :
        isGameOn = 0;
    
def areTheyTouching():
    #Check of fox coordinate are within +/-25 pixel of planets center point
    global score
    by = fox.ycor()
    bx = fox.xcor()
    py = planet.ycor()
    px = planet.xcor()
   
    if((by > py-50) & (by < py+50) & (bx > px-50) & (bx < px+50)) :
        istouching = True
    else:
         istouching = False
    if(istouching):
        fox.goto(0,0)
        score = score + 50
        print("Touched..."+str(score))
        changeplanet()
        updatescore()
      

        


        
turtle.listen()
#turtle.onkey(tl, "L")#turtle.onkey(tl, "l")
#turtle.onkey(tr, "R")
#turtle.onkey(tr, "r")
turtle.onkey(mr, "Right")
turtle.onkey(ml, "Left")
turtle.onkey(mu, "Up")
turtle.onkey(md, "Down")
#turtle.onkey(j, "J")
#turtle.onkey(j, "j")


while (isGameOn == 1):
    planet.speed(1)
    planet.fillcolor("red")
    planet.penup()
    planet.circle(-300)
    #planet.pendown()
    #check if they are touching, then increase the score. Switch to next planet

planet.hideturtle()
planet.goto(0,0)
fox.hideturtle()
turtle.bgcolor("blue")

planet.write("Game over",align ='center', font=("Courier",90,"bold"))
winsound.PlaySound("gmsw1.wav",winsound.SND_ASYNC)
time.sleep(12)

turtle.mainloop()
