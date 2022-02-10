import turtle
import random
import asyncio

colors = ['red', 'orange', 'yellow', 'green2', 'cyan', 'blue', 'magenta']

turtle.shape('classic')
turtle.shapesize(2)
turtle.pensize(2)
turtle.bgcolor('black')
turtle.color(random.choice(colors))

async def colorSwitch(colors):
    while 1:
        await asyncio.sleep(1)
        turtle.color(random.choice(colors))
        

async def main():
    while 1:
        turtle.speed(100)
        angle = random.randint(-360, 360)
        turtle.right(angle)
        print(f'angle: {angle}')
        length = random.randint(5, 10)
        turtle.forward(length)
        print(f'length: {length}')
        await asyncio.sleep(0)
        
async def run():
    await asyncio.gather(colorSwitch(colors), main())

asyncio.run(run())