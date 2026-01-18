import random
import math
import matplotlib.pyplot as plt

def lerp(a, b, t):
    return a+ t* (b- a)

def fade(t):
    return t* t* t* (t* (t* 6- 15)+ 10)

def random_gradient():
    angle = random.uniform(0, 2* math.pi)
    return (math.cos(angle), math.sin(angle))

def dot_grid_gradient(ix, iy, x, y, gradients):
    dx = x- ix
    dy = y- iy

    gradient = gradients[(ix,iy)]
    return dx* gradient[0] + dy* gradient[1]

def perlin(x, y, gradients):
    x0 = math.floor(x)
    x1 = x0+ 1
    y0 = math.floor(y)
    y1 = y0+ 1

    sx = fade(x - x0)
    sy = fade(y - y0)

    n0 = dot_grid_gradient(x0, y0, x, y, gradients)
    n1 = dot_grid_gradient(x1, y0, x, y, gradients)
    ix0 = lerp(n0, n1, sx)

    n0 = dot_grid_gradient(x0, y1, x, y, gradients)
    n1 = dot_grid_gradient(x1, y1, x, y, gradients)
    ix1 = lerp(n0, n1, sx)
    
    return lerp(ix0, ix1, sy)

def generate_gradients(width, height):
    
    gradients = {}
    for x in range(width+ 1):
        for y in range(height+ 1):
            gradients[(x, y)] = random_gradient()
    return gradients

Width = 500
Height = 500
Scale = 40

gradients = generate_gradients(Width// Scale+ 1, Height// Scale+ 1)

image = []

for y in range(Height):
    row = []
    for x in range(Width):
        value = perlin(x/ Scale, y/ Scale, gradients)
        value = (value + 1) / 2
        row.append(value)
    image.append(row)

plt.imshow(image, cmap="plasma")
plt.colorbar()
plt.title("Perlin Noise")

plt.show()

