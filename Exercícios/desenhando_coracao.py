import turtle

pen = turtle.Turtle() 
def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 
def heart(): 
    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112) 
    pen.end_fill() 
def txt(): 
    pen.up() 
    pen.setpos(-68, 95) 
    pen.down() 
    pen.color('white') 
    pen.write("T", (-68, 95), font=( 
        "Stencil std", 18, "italic")) 
    pen.write("e", (-55, 95), font=( 
        "Stencil std", 18, "italic"))
    pen.write(" ", (-42, 95), font=( 
    "Stencil std", 18, "italic"))
    pen.write("A", (-30, 95), font=( 
    "Stencil std", 18, "italic"))
    pen.write("m", (-14, 95), font=( 
    "Stencil std", 18, "italic"))
    pen.write("o", (10, 95), font=( 
    "Stencil std", 18, "italic"))
    pen.write("!", (26, 95), font=( 
    "Stencil std", 18, "italic"))


heart() 
txt() 
pen.ht() 