#final project : space invaders by Hadil and Deema
#0-import the libraries which we need
import turtle
import os
import random
#1-set up the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.setup(width=700 ,height=700)
wn.bgpic('space_invaders_background.gif')

#Register the shapes
turtle.register_shape('player.gif')
turtle.register_shape('invader.gif')
#a pen to write Game Over and YOU WON!
pen = turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0,0)


#Draw the border
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.goto(-300,-300)
border.pensize(3)
border.pendown()
for side in range(4):
	border.forward(600)
	border.left(90)
border.hideturtle()

#Set the score
score = 0
#draw the score on the screen
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.goto(-290,280)
score_pen.write('score:'+ str(score))


#2-creat the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setheading(90)
player.goto(0,-250)
#
#choose number of enemies
number_of_enemies = 5
#creat an empty list for the enemies
enemies = []
#add enemies to the list
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	#4-creat the enemy
	enemy.color('red')
	enemy.shape('invader.gif')
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.goto(x,y)
enemyspeed = 2







#3-mover the player turtle
#make a  virable to change the position of the player
playersteps = 20
#5- creat the palyers bullet turtle
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 25
#define the bullet state (ready or fire)
#ready-ready to fire
#fire_bullet is firing
bulletstate = 'ready'




#functions to the key event listeners
#the player movment
def move_right():
	x = player.xcor()
	x += playersteps
	if x > 280:
		x = 280 #we chose 280 cuz it's before the border by 20 pixels
	player.setx(x)
def move_left():
	x = player.xcor()
	x -= playersteps
	if x <-280:
		x = -280 #we chose 280 cuz it's before the border by 20 pixels
	player.setx(x)

#fire the bullet
def fire_bullet():
	global bulletstate
	if bulletstate == 'ready':
		bulletstate = 'fire'
	#move the bullet above the player
	x = player.xcor()
	y = player.ycor() + 10
	bullet.goto(x,y)
	bullet.showturtle()
#check is the bullet is tuouching the enemy
def isCollsion(t1,t2):
	distance = t1.distance(t2)
	if distance<15:
		return True
	else:
		return False





#call our player functions
wn.listen()
wn.onkey(move_right,'Right')
wn.onkey(move_left,'Left')
wn.onkey(fire_bullet,'space')

#Main game loop
while True:
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		if enemy.xcor()>280:
			for e in enemies:
				y = e.ycor()
				y -= 20
				e.sety(y)
			enemyspeed *= -1

		if enemy.xcor()< -280:
			for e in enemies:
				y = e.ycor()
				y -= 20
				e.sety(y)
			enemyspeed *= -1
		if isCollsion(bullet,enemy):
			#reset the bullet
			bullet.hideturtle()
			bulletstate = 'ready'
			bullet.goto(0,-400)
			x = random.randint(-200,200)
			y = random.randint(100,250)
			enemy.goto(x,y)
			#update score
			score += 10
			score_pen.clear()
			score_pen.write('score:' + str(score))

		if isCollsion(player,enemy):
			player.hideturtle()
			enemy.hideturtle()
			pen.write('GAME OVER!')
			continue
	#fire the bullet
	y = bullet.ycor()
	y += bulletspeed
	bullet.sety(y)
	#check if the bullet have gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = 'ready'







turtle.mainloop()