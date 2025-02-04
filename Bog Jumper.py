from levels import Levels, drawGame
from player import *
from urllib.request import urlopen
import pygame as p
import io

width = 1080
height = 607.50
fps = 144
blockWidth = width / 36
blockHeight = height / 20
images = {}
gameStates = ["startScreen", "inGame", "gameOver", "levelComplete", "gameComplete", "infoScreen"]
isRestarting = False


def main():
    gameState = gameStates[0]
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()

    # Loading Images
    screen.fill(p.Color("light grey"))
    font = p.font.Font("freesansbold.ttf", 30)
    loading = font.render("Loading...", True, p.Color("grey 50"))
    loadingRect = loading.get_rect()
    loadingRect.center = (width / 2, height / 2)
    screen.blit(loading, loadingRect)
    p.display.update()

    loadImages()

    p.display.set_caption("Bog Jumper")
    p.display.set_icon(images["player"])

    levels = Levels()
    levelIndex = 1
    levelName = f"level{levelIndex}"
    level = levels.levels[levelName]
    player = Player(levels.levelSpawns[levelName], False)
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

            # Normal Mode Text
            font = p.font.Font("freesansbold.ttf", 20)
            startText = font.render("Left-Click for Normal Mode", True, p.Color("grey 50"))
            startRect = startText.get_rect()
            startRect.center = (width / 2, height / 2)
            screen.blit(startText, startRect)

            # Practice Mode Text
            font = p.font.Font("freesansbold.ttf", 20)
            startText = font.render("Right-Click for Practice Mode", True, p.Color("grey 50"))
            startRect = startText.get_rect()
            startRect.center = (width / 2, height / 2 + 50)
            screen.blit(startText, startRect)

            # Controls
            font = p.font.Font("freesansbold.ttf", 20)
            controls = font.render("Use Arrow Keys to Move", True, p.Color("grey 50"))
            controlsRect = controls.get_rect()
            controlsRect.center = (width / 2, height / 2 + 100)
            screen.blit(controls, controlsRect)

            # Credits
            font = p.font.Font("freesansbold.ttf", 20)
            credits = font.render("Created by: Diarmuid Eager ¦ Artwork by Sam McEvoy", True, p.Color("grey 50"))
            creditsRect = credits.get_rect()
            creditsRect.center = (width / 2, height - 50)
            screen.blit(credits, creditsRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        player.isPracticeMode = False
                        gameState = gameStates[1]
                    elif e.button == 3:
                        player.isPracticeMode = True
                        player.lives = 999
                        gameState = gameStates[1]

        elif gameState == gameStates[1]:
            # In Game

            if player.lives <= 0:
                gameState = gameStates[2]
                continue

            if player.isAtFinish:
                if levelIndex == len(levels.levels):
                    gameState = gameStates[4]
                else:
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
            drawGame(screen, level, levelIndex, player, images, blockWidth, blockHeight)

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

            # Next Level Text
            font = p.font.Font("freesansbold.ttf", 20)
            nextLevelText = font.render(f"Click for the next level", True, p.Color("grey 50"))
            nextLevelRect = nextLevelText.get_rect()
            nextLevelRect.center = (width / 2, height / 2 + 50)
            screen.blit(nextLevelText, nextLevelRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    levelIndex += 1
                    levelName = f"level{levelIndex}"
                    level = levels.levels[levelName]
                    player = Player(levels.levelSpawns[levelName], player.isPracticeMode)
                    gameState = gameStates[1]

        elif gameState == gameStates[4]:
            # Game Complete

            screen.fill(p.Color("light grey"))

            # Game Complete Text
            font = p.font.Font("freesansbold.ttf", 30)
            gameCompleteText = font.render("Congratulations! Game Complete! Thanks for playing!", True, p.Color("grey "
                                                                                                                "50"))
            gameCompleteRect = gameCompleteText.get_rect()
            gameCompleteRect.center = (width / 2, height / 2 - 50)
            screen.blit(gameCompleteText, gameCompleteRect)

            # Lizard Text
            font = p.font.Font("freesansbold.ttf", 20)
            lizardText = font.render(f"Click to Learn More About the Lizard!", True, p.Color("grey 50"))
            lizardRect = lizardText.get_rect()
            lizardRect.center = (width / 2, height / 2 + 50)
            screen.blit(lizardText, lizardRect)

            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    gameState = gameStates[5]

        elif gameState == gameStates[5]:
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
    items = ["block", "player", "star", "super-star", "heart", "flag"]
    for item in items:
        imgUrl = f"https://iamdeedz.github.io/bog/{item}.png"
        imgStr = urlopen(imgUrl).read()
        imgFile = io.BytesIO(imgStr)
        images[item] = p.transform.scale(p.image.load(imgFile), (blockWidth, blockHeight))
    bgUrl = f"https://iamdeedz.github.io/bog/background.png"
    bgStr = urlopen(bgUrl).read()
    bgFile = io.BytesIO(bgStr)
    images["background"] = p.transform.scale(p.image.load(bgFile), (width, height))


if __name__ == '__main__':
    main()
