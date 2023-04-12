from levels import *
from player import *
import pygame as p

width = 1280
height = 720
fps = 60
blockWidth = width / 40
blockHeight = height / 20
images = {}
gameStates = ["startScreen", "inGame", "gameOver", "levelComplete", "infoScreen"]
isRestarting = False


def main():
    gameState = gameStates[0]
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    p.display.set_caption("Bog Jumper")
    p.display.set_icon(p.image.load("images/player.png"))
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

            if player.isAtFinish:
                gameState = gameStates[3]
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

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False

        elif gameState == gameStates[3]:
            # Level Complete

            screen.fill(p.Color("light grey"))

            # Level Complete Text
            font = p.font.Font("freesansbold.ttf", 30)
            levelCompleteText = font.render("Level Complete!", True, p.Color("grey 50"))
            levelCompleteRect = levelCompleteText.get_rect()
            levelCompleteRect.center = (width / 2, height / 2 - 50)
            screen.blit(levelCompleteText, levelCompleteRect)

            # Score Text
            font = p.font.Font("freesansbold.ttf", 20)
            scoreText = font.render(f"Your Score was {player.score}", True, p.Color("grey 50"))
            scoreRect = scoreText.get_rect()
            scoreRect.center = (width / 2, height / 2)
            screen.blit(scoreText, scoreRect)

            # Surprise Text
            font = p.font.Font("freesansbold.ttf", 20)
            surpriseText = font.render(f"Click to Learn More About the Lizard!", True, p.Color("grey 50"))
            surpriseRect = surpriseText.get_rect()
            surpriseRect.center = (width / 2, height / 2 + 50)
            screen.blit(surpriseText, surpriseRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    gameState = gameStates[4]

        elif gameState == gameStates[4]:
            # Info Screen

            screen.fill(p.Color("light grey"))

            # Title

            font = p.font.Font("freesansbold.ttf", 30)
            title = font.render("The Viviparous Lizard!", True, p.Color("grey 50"))
            titleRect = title.get_rect()
            titleRect.center = (width / 2, 250)
            screen.blit(title, titleRect)

            # Info Text
            infoText = [
                "The Viviparous Lizard is Ireland's only lizard!",
                "It can be found in Europe and Central Asia.",
                "It is a carnivore that mainly eats small insects like flies, spiders and even snails.",
                "Viviparous Lizards have a very good sense of smell. When they smell a predator, they will start ",
                "to flick their tongue very rapidly to determine the distance to the predator. If the predator ",
                "is nearby, they will either play dead or camouflage themselves with their surroundings."
            ]

            font = p.font.Font("freesansbold.ttf", 20)
            for line in infoText:
                text = font.render(line, True, p.Color("grey 50"))
                textRect = text.get_rect()
                textRect.centerx = width / 2
                textRect.y = infoText.index(line) * 30 + 300
                screen.blit(text, textRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False

        clock.tick(fps)
        p.display.update()


def loadImages():
    items = ["block", "player", "star", "heart", "flag"]
    for item in items:
        images[item] = p.transform.scale(p.image.load("images/" + item + ".png"), (blockWidth, blockHeight))
    images["background"] = p.transform.scale(p.image.load("images/background.png"), (width, height))


if __name__ == '__main__':
    main()
