#from pygame import mixer
# from pygame.locals import *
# import pygame
import turtle
pen = turtle.Turtle()


# pygame.init()
# width = 1000
# height = 500
# window = pygame.display.set_mode((width, height))
# bg_img = pygame.image.load('wall1.jpg')
# bg_img = pygame.transform.scale(bg_img, (width, height))

# mixer.init()
# mixer.music.load('Music File/bensound-summer_wav_music.wav')
# mixer.music.play()

# runing = True
# while runing:
#     window.blit(bg_img, (0, 0))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             runing = False
#     pygame.display.update()
# pygame.quit()


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def heart():
    pen.fillcolor("red")
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
    pen.color("pink")
    pen.write("I love you 3000", font=("verdana", 12, "bold"))


heart()
txt()
pen.ht()
turtle.exitonclick()
