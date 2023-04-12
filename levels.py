import pygame as p

test = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]
for _ in range(5):
    test.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

levelSpawns = {"test": {"r": 1, "c": 2}}


def drawText(screen, player):
    # Score Text
    font = p.font.Font("freesansbold.ttf", 15)
    scoreText = font.render(f"Score: {player.score}", True, p.Color("white"))
    screen.blit(scoreText, p.Rect(25, 25, 0, 0))

    # Lives Text
    font = p.font.Font("freesansbold.ttf", 15)
    livesText = font.render(f"Lives Remaining: {player.lives}", True, p.Color("white"))
    screen.blit(livesText, p.Rect(25, 50, 0, 0))


def drawLevel(screen, lvl, player, images, blockDimensions, offsets):
    blockWidth, blockHeight = blockDimensions
    xOffset, yOffset = offsets

    # Camera Scroll
    if player.position["c"] > 25:
        xOffset -= (player.position["c"] - 25) * blockWidth

    for r in range(len(lvl)):
        for c in range(len(lvl[r])):
            if lvl[r][c] == 1:
                screen.blit(images["block"],
                            p.Rect((c * blockWidth) + xOffset,
                                   (r * blockHeight) + yOffset,
                                   blockWidth, blockHeight))


def drawSprites(screen, lvl, player, images, blockDimensions, offsets):
    blockWidth, blockHeight = blockDimensions
    xOffset, yOffset = offsets
    playerXOffset = xOffset

    # Camera Scroll
    if player.position["c"] > 25:
        xOffset -= (player.position["c"] - 25) * blockWidth

    # Player
    if player.orientation == "right":
        screen.blit(images["player"],
                    p.Rect((player.position["c"] * blockWidth + xOffset),
                           (player.position["r"] * blockHeight + yOffset),
                           blockWidth, blockHeight))
    else:
        screen.blit(p.transform.flip(images["player"], True, False),
                    p.Rect((player.position["c"] * blockWidth) + xOffset,
                           (player.position["r"] * blockHeight) + yOffset,
                           blockWidth, blockHeight))

    # Stars
    for r in range(len(lvl)):
        for c in range(len(lvl[r])):
            if lvl[r][c] == 2:
                screen.blit(images["star"],
                            p.Rect((c * blockWidth) + xOffset,
                                   (r * blockHeight) + yOffset,
                                   blockWidth, blockHeight))

    # Hearts
    for r in range(len(lvl)):
        for c in range(len(lvl[r])):
            if lvl[r][c] == 3:
                screen.blit(images["heart"],
                            p.Rect((c * blockWidth) + xOffset,
                                   (r * blockHeight) + yOffset,
                                   blockWidth, blockHeight))

    # Flag
    for r in range(len(lvl)):
        for c in range(len(lvl[r])):
            if lvl[r][c] == 4:
                screen.blit(images["flag"],
                            p.Rect((c * blockWidth) + xOffset,
                                   (r * blockHeight) + yOffset,
                                   blockWidth, blockHeight))


def drawGame(screen, lvl, player, images, blockWidth, blockHeight):
    xOffset = blockWidth * 5
    yOffset = blockHeight * 5
    drawLevel(screen, lvl, player, images, [blockWidth, blockHeight], [xOffset, yOffset])
    drawSprites(screen, lvl, player, images, [blockWidth, blockHeight], [xOffset, yOffset])
    drawText(screen, player)
