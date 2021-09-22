"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author Brian Ramirez

********* HEY, READ THIS FIRST **********

This code creates random circles across the panel and are colored randomly with the colors in my palette. 
These circles increase in size after every circle and there are 100 circles. It also creates 50 random lines with a
different color palette.


"""
import turtle
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
bro = turtle.Turtle() #set my turtle variable to bro
bro.speed(0) #makes it draw

bro.up() #pick pen up
radius = 25 #set how big the circle is going to be
palette = ("blue", "pink", "white", "#FF6978", "#EEEBDE", "#403233", "#8896AB", "#1F2421", "#B4DC7F") #color palette for circles
palette2 = ("black", "#AA6DA3", "#7DAA92", "#00A7E3") # color palette for lines
for i in range(100): # for loop to create colored circles increasing in size
    bro.goto(random.randint(-300,300),random.randint(-300,300)) #goes to random locations
    bro.down() # pen down
    bro.begin_fill() # start filling my circles
    bro.color(random.choice(palette)) # the colors of my circles at random
    #random.choice(palette)
    #bro.color(palette[i])
    bro.width(i+1)#increases how big the circles are
    bro.circle(radius) #circles
    bro.up() # pick pen up
    bro.end_fill() #end fill for my circles
    
line = turtle.Turtle() # set my turtle variable to line
line.speed(0) #set the speed to fast
for i2 in range(50): # for loop to create 50 lines
    line.goto(random.randint(-300,300),random.randint(-300,300)) #draws lines at different locations
    line.down() #pen down
    line.pencolor(random.choice(palette2)) #makes my lines different colors
    line.width(1) # makes the lines have a smaller width
    line.forward(50) # makes line go forward
    
    

    
    

    

# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
