from levels import *
from player import *
from debugger import *
import pygame as p

width = 1680
height = 720
fps = 60
blockWidth = (width - 400) / 40
blockHeight = height / 20
images = {}


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    p.display.set_caption("Bog Jumper")
    loadImages()
    levelName = "test"
    level = test
    player = Player(levelSpawns[levelName])
    debugger = Debugger(screen)
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_RIGHT:
                    player.isRightPressed = True
                if e.key == p.K_LEFT:
                    player.isLeftPressed = True
                if e.key == p.K_UP:
                    player.isUpPressed = True
            elif e.type == p.KEYUP:
                if e.key == p.K_RIGHT:
                    player.isRightPressed = False
                if e.key == p.K_LEFT:
                    player.isLeftPressed = False
                if e.key == p.K_UP:
                    player.isUpPressed = False
        screen.fill(p.Color("black"))
        player.update(level)
        debugger.update(player, levelName)
        drawGame(screen, level, player, images, blockWidth, blockHeight)
        clock.tick(fps)
        p.display.update()


def loadImages():
    items = ["block", "player"]
    for item in items:
        images[item] = p.transform.scale(p.image.load("images/" + item + ".png"), (blockWidth, blockHeight))


if __name__ == "__main__":
    main()

#  https://ibb.co/02HtJfV
#  https://ibb.co/M7H9rS2
