import turtle as ttl
import random

screen = ttl.Screen()
screen.setup(1000,700)
ttl.speed("fastest")
background = "background.gif"
screen.register_shape(background)
screen.bgpic(background)

enemy_missile = 'enemy_missile.gif'
screen.register_shape(enemy_missile)

random_colors = ["gray", "black", "blue4", "DarkSlateGray"]
enemy_missiles = []
lives = 5

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

# Placing the Q-launcher
screen.register_shape("q_launcher.gif")
ttl.penup()
ttl.goto(-400, -250)
ttl.shape("q_launcher.gif")
ttl.stamp()
ttl.hideturtle()

# Placing the R-launcher
screen.register_shape("r_launcher.gif")
ttl.penup()
ttl.goto(-150, -250)
ttl.shape("r_launcher.gif")
ttl.stamp()
ttl.hideturtle()

# Placing the U-launcher
screen.register_shape("u_launcher.gif")
ttl.penup()
ttl.goto(150, -250)
ttl.shape("u_launcher.gif")
ttl.stamp()
ttl.hideturtle()

# Placing the p-launcher
screen.register_shape("p_launcher.gif")
ttl.penup()
ttl.goto(400, -250)
ttl.shape("p_launcher.gif")
ttl.stamp()
ttl.hideturtle()

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
ttl.write("Lives Remaining: " + str(lives), font=("Minecraft", 16, "bold"), align='right')

# Generate Enemy Missiles
xpos = -400
for enemy in range(0, 20):
  missile = ttl.Turtle(shape=enemy_missile)
  enemy_missiles.append(missile)
  missile.teleport(xpos, 400)
  missile.setheading(random.randint(-180, 0))
  xpos += 50

#Enemy Missile Movement
for step in range(100):
  for x in enemy_missiles:
    x.penup()
    x.forward(10)

    #Missile Exploding on City
    if x.ycor() <= -100:
      x.shape("circle")
      x.fillcolor("orange")
      x.pensize(100)
      x.hideturtle()
      enemy_missiles.remove(x)
      lives -= 1
      ttl.fillcolor('white')
      ttl.begin_fill()
      ttl.teleport(450, 250)
      ttl.goto(450, 276)
      ttl.goto(250, 276)
      ttl.goto(250, 250)
      ttl.goto(450, 250)
      ttl.end_fill()
      ttl.pencolor("red")
      ttl.write("Lives Remaining: " + str(lives), font=("Minecraft", 16, "bold"), align='right')

      if lives == 0:
        ttl.done()






screen.mainloop()