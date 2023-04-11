from levels import *
from player import *
import pygame as p

width = 1280
height = 720
fps = 60
blockWidth = width / 40
blockHeight = height / 20
images = {}
gameStates = ["startScreen", "inGame", "gameOver"]
isRestarting = False


def main():
    gameState = gameStates[0]
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    p.display.set_caption("Bog Jumper")
    loadImages()
    levelName = "test"
    level = test
    player = Player(levelSpawns[levelName])
    running = True
    while running:
        if gameState == gameStates[0]:
            # Start Screen

            screen.fill(p.Color("light grey"))

            # Title
            font = p.font.Font("freesansbold.ttf", 30)
            title = font.render("Bog Jumper", True, p.Color("grey 50"))
            titleRect = title.get_rect()
            titleRect.center = (width / 2, height / 2 - 50)
            screen.blit(title, titleRect)

            # Start Text
            font = p.font.Font("freesansbold.ttf", 20)
            startText = font.render("Click Anywhere to Start", True, p.Color("grey 50"))
            startRect = startText.get_rect()
            startRect.center = (width / 2, height / 2)
            screen.blit(startText, startRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    gameState = gameStates[1]

        elif gameState == gameStates[1]:
            # In Game

            if player.lives <= 0:
                gameState = gameStates[2]
                continue

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_RIGHT:
                        player.isRightPressed = True
                        player.orientation = "right"
                    if e.key == p.K_LEFT:
                        player.isLeftPressed = True
                        player.orientation = "left"
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
            drawGame(screen, level, player, images, blockWidth, blockHeight)

        elif gameState == gameStates[2]:
            # Game Over

            screen.fill(p.Color("light grey"))

            # Game Over Text
            font = p.font.Font("freesansbold.ttf", 30)
            gameOverText = font.render("Game Over!", True, p.Color("grey 50"))
            gameOverRect = gameOverText.get_rect()
            gameOverRect.center = (width / 2, height / 2 - 50)
            screen.blit(gameOverText, gameOverRect)

            # Score Text
            font = p.font.Font("freesansbold.ttf", 20)
            scoreText = font.render(f"Your Score was {player.score}", True, p.Color("grey 50"))
            scoreRect = scoreText.get_rect()
            scoreRect.center = (width / 2, height / 2)
            screen.blit(scoreText, scoreRect)

            # Restart Text
            restartText = font.render("Click Anywhere to Restart", True, p.Color("grey 50"))
            restartRect = restartText.get_rect()
            restartRect.center = (width / 2, height / 2 + 50)
            screen.blit(restartText, restartRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    global isRestarting
                    isRestarting = True
                    return

        clock.tick(fps)
        p.display.update()


def loadImages():
    items = ["block", "player"]
    for item in items:
        images[item] = p.transform.scale(p.image.load("images/" + item + ".png"), (blockWidth, blockHeight))


def loop():
    global isRestarting
    isRestarting = False

    main()

    if isRestarting:
        loop()


if __name__ == '__main__':
    loop()
