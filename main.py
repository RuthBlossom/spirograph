# Import the turtle module as 't'
import turtle as t
import random

# Create a turtle object named 'tim'
tim = t.Turtle()

# Set color mode to 255 (RGB)
t.colormode(255)


# Function to generate a random RGB color
def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color


# Function to draw a spirograph pattern
def draw_spirograph(size_of_gap):
	tim.speed("fastest")  # Set the turtle speed to "fast"
	tim.pensize(2)  # Set the pen size to 2 (you can adjust this value)
	# Loop to create the spirograph
	for _ in range(int(360 / size_of_gap)):
		# Set the turtle's color to a random color
		tim.color(random_color())



		# Draw a circle with a radius of 100 units
		tim.circle(100)

		# Rotate the turtle's heading by the specified gap size
		tim.setheading(tim.heading() + size_of_gap)


# Call the draw_spirograph function with a gap size of 5
draw_spirograph(5)

# Keep the window open until closed by the user
t.mainloop()

