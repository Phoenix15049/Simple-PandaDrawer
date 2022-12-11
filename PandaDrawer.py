import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining method to draw a colored circle
def ring(col, rad):

	pen.fillcolor(col)

	pen.begin_fill()

	pen.circle(rad)

	pen.end_fill()

#Face Drawer

pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

pen.up()
pen.setpos(-18, 75)
pen.down
ring('black', 8)

pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

#Eyes Drawer

pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 5)

#Mouth and nose drawer

pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)
pen.hideturtle()

#Last Text 

turtle.write("Phoenix15049", font=("Verdana",15, "normal"))

turtle.delay(3000)

turtle.clearscreen()

turtle.Screen().bgcolor('black')
turtle.pensize(2)
turtle.speed(10.005)

for i in range(6):

	for color in ('red', 'magenta', 'blue','cyan', 'green', 'white','yellow'):
        
		turtle.color(color)

		# Draw a circle of chosen size, 100 here
		turtle.circle(100*((i+1)/2))

		# Move 10 pixels left to draw another circle
		turtle.left(10)

	# Hide the cursor(or turtle) which drew the circle

	turtle.hideturtle()




turtle.done()