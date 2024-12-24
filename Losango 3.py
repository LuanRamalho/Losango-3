import turtle
import random

def draw_rhombus(x, y, size, color):
    """Desenha um losango com o centro em (x, y)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.left(120)

    turtle.end_fill()

def random_color():
    """Gera uma cor aleatória no formato hexadecimal."""
    return "#" + "".join(random.choices("0123456789ABCDEF", k=6))

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Losangos Aleatórios")

    turtle.speed(0)
    turtle.hideturtle()

    # Gera entre 5 e 15 losangos
    num_rhombuses = random.randint(5, 25)

    for _ in range(num_rhombuses):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        size = random.randint(20, 100)
        color = random_color()
        draw_rhombus(x, y, size, color)

    # Mantém a janela aberta até o usuário clicar
    screen.mainloop()

if __name__ == "__main__":
    main()
