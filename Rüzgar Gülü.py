import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors=["red","yellow","blue","green","purple","orange"]
for i in range(300):
    t.pencolor(colors[i%6])
    t.forward(i*2)
    t.right(61)
turtle.done() 



for i in range (0,5):
    for j in range(i):
        print("*")
print("\n")