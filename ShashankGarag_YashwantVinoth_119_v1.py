import turtle as ttl
import random

screen = ttl.Screen()
screen.setup(1000,700)
ttl.speed("fastest")
background = "background.gif"
screen.addshape(background)

random_colors = ["gray", "black", "blue4", "DarkSlateGray"]

#Drawing Buildings
ttl.pencolor("black")
ttl.pensize(3)

height = 200
ttl.teleport(-500, -100)

for building in range(0, 20):
  ttl.fillcolor(random.choice(random_colors))
  ttl.begin_fill()
  ttl.forward(50)
  ttl.right(90)
  ttl.forward(height)
  ttl.right(90)
  ttl.forward(50)
  ttl.right(90)
  ttl.forward(height)
  ttl.end_fill()

  ttl.right(90)
  ttl.forward(50)
  ttl.right(90)
  ttl.forward(height)
  
  height = random.randint(50,200)
  ttl.right(180)
  ttl.forward(height)
  ttl.right(90)


#Generate Ground
ttl.right(90)
ttl.forward(height)
ttl.right(90)
ttl.fillcolor("black")
ttl.begin_fill()
ttl.forward(1000)
ttl.left(90)
ttl.forward(50)
ttl.left(90)
ttl.forward(1000)
ttl.left(90)
ttl.forward(50)
ttl.end_fill()


#Drawing stats display
# Border
ttl.color('red')
ttl.teleport(-475, 325)
ttl.setheading(0)
ttl.begin_fill()
ttl.forward(950)
ttl.right(90)
ttl.forward(100)
ttl.right(90)
ttl.forward(950)
ttl.right(90)
ttl.forward(100)
ttl.end_fill()

# Background
ttl.color('white')
ttl.teleport(-460, 310)
ttl.right(90)
ttl.begin_fill()
ttl.forward(920)
ttl.right(90)
ttl.forward(70)
ttl.right(90)
ttl.forward(920)
ttl.right(90)
ttl.forward(70)
ttl.end_fill()

# Text
ttl.teleport(-450, 250)
ttl.color('red')
ttl.write("Missile Command", font=("Minecraft", 32, "bold"))
ttl.teleport(450, 275)
ttl.write("Score: 0", font=("Minecraft", 16, "bold"), align='right')
ttl.teleport(450, 250)
ttl.write("Lives Remaining: 0", font=("Minecraft", 16, "bold"), align='right')


screen.mainloop()