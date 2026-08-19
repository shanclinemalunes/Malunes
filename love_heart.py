import tkinter as tk
import math
import random

WIDTH = 900
HEIGHT = 700

root = tk.Tk()
root.title("I Love You ❤️")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="black")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

texts = []

for i in range(500):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    text = canvas.create_text(
        x, y,
        text="I LOVE YOU",
        fill="pink",
        font=("Arial", 10, "bold")
    )

    texts.append({
        "id": text,
        "x": x,
        "y": y,
        "speed": random.uniform(0.5, 2)
    })


def heart_position(t):
    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    scale = 20

    x = WIDTH / 2 + x * scale
    y = HEIGHT / 2 - y * scale

    return x, y


def animate():
    for i, item in enumerate(texts):

        t = (i / len(texts)) * math.pi * 2

        target_x, target_y = heart_position(t)

        item["x"] += (target_x - item["x"]) * 0.02
        item["y"] += (target_y - item["y"]) * 0.02

        canvas.coords(
            item["id"],
            item["x"],
            item["y"]
        )

    root.after(20, animate)


animate()
root.mainloop()

