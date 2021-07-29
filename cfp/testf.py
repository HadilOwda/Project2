import turtle
import random
#set up the screen
wn = turtle.Screen()
wn.bgcolor('white')
wn.title('break out')
wn.setup(width=600,height = 600)
wn.tracer(0)
boundry = turtle.Turtle()
boundry.speed(0)
boundry.penup()
boundry.goto(-200,200)
boundry.pendown()
for i in range(4):
 boundry.forward(400)
 boundry.right(90)

paddle = turtle.Turtle()
paddle.color('pink')
#to the paddle turtle to to position
paddle.penup()
paddle.goto(0,-180)
paddle.shape('square')
paddle.shapesize(0.5,3)
paddle.penup()

def move_right():
 	if paddle.xcor()+30 < 190:
  	  paddle.forward(20)

def move_left():
	if paddle.xcor()-30 >-190:
	  paddle.backward(20)


wn.onkey(move_right,"Right")
wn.onkey(move_left,"Left")
wn.listen()

gap_size = 10
brick_width = 50
brick_length = 25

color_list = ['red','blue','green', 'purple']
bricks_list = []
def draw_bricks(x):
	x = -170
	y = 180
	for b in range(4):
		
		for i in range(7):
			bricks = turtle.Turtle()
			bricks.speed(0)
			bricks.penup()
			bricks.goto(x,y)
			bricks.pendown()
			bricks.color(color_list[b])
			bricks.shape('square')
			bricks.shapesize(1,2)
			bricks_list.append(bricks)
			x = x + gap_size +45
		x = -170
		y = y - gap_size-brick_length

draw_bricks(bricks_list)



Circle = turtle.Turtle()
Circle.shape("circle")
Circle.color('yellow')
Circle.penup()
Circle.setheading(random.randint(0 , 360))
gravity=0.1
def cor (a,b):
	return a.distance(b)<20


v=0


while v==0:
	wn.update()
	wn.delay(0)
	Circle.fd(3)
	Circle.speed(0)
	for x in bricks_list:
		if cor(Circle,x):
			bricks_list.remove(x)
			x.hideturtle()
			a=360-Circle.heading()
			Circle.setheading(a)
	if Circle.ycor()<=-200:
		Circle.hideturtle()
		Circle.penup()
		Circle.goto(-170,-30)
		Circle.write('Game over !', font=("Arial", 50 , "normal"))
		v=1
	if Circle.xcor()+10>=200:
		a=180-Circle.heading()
		Circle.setheading(a)
	if Circle.xcor()-10<=-200:
		a=180-Circle.heading()
		Circle.setheading(a)
	if Circle.ycor()+10>=200:
		a=360-Circle.heading()
		Circle.setheading(a)
	if Circle.ycor()-10<=paddle.ycor()+5 and Circle.xcor()+10<=paddle.xcor()+30 and Circle.xcor()+10>=paddle.xcor()-30:
		a=360-Circle.heading()
		Circle.setheading(a)
	if bricks_list==[]:
		Circle.goto(-130,0)
		Circle.write('You win !', font=("Arial", 50 , "normal"))
		Circle.hideturtle()
		v=1

	 

turtle.exitonclick()


