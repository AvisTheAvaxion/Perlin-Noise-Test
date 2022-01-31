from perlin_noise import PerlinNoise
import random
import discord_bot

noise = PerlinNoise(octaves=10, seed=1)

w, h = 8, 8
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = 1
Matrix[0][6] = 3

print(Matrix[0][0]) # prints 1
x, y = 0, 6
print(Matrix[x][y])
print("\n\n\n\n")


def print_array(arr, width, height):
    s = ""
    for i in range(width):
        for i1 in range(height):
            s = s + str(arr[i][i1])

        print(s)
        s = ""


print_array(Matrix, w, h)


for i in range(w):
    for i1 in range(h):
        Matrix[i][i1] = random.randint(1, 5)

print_array(Matrix, w, h)
print("\n\n\n\n")


discord_bot.run()
