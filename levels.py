import pygame as p

test = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
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


def drawLevel(screen, lvl, images, blockDimensions, offsets):
    blockWidth, blockHeight = blockDimensions
    xOffset, yOffset = offsets
    for r in range(len(lvl)):
        for c in range(len(lvl[r])):
            if lvl[r][c] == 1:
                screen.blit(images["block"],
                            p.Rect((c * blockWidth) + xOffset,
                                   (r * blockHeight) + yOffset,
                                   blockWidth, blockHeight))


def drawSprites(screen, player, images, blockDimensions, offsets):
    blockWidth, blockHeight = blockDimensions
    xOffset, yOffset = offsets
    if player.orientation == "right":
        screen.blit(images["player"],
                    p.Rect((player.position["c"] * blockWidth) + xOffset,
                           (player.position["r"] * blockHeight) + yOffset,
                           blockWidth, blockHeight))
    else:
        screen.blit(p.transform.flip(images["player"], True, False),
                    p.Rect((player.position["c"] * blockWidth) + xOffset,
                           (player.position["r"] * blockHeight) + yOffset,
                           blockWidth, blockHeight))


def drawGame(screen, lvl, player, images, blockWidth, blockHeight):
    xOffset = blockWidth * 5
    yOffset = blockHeight * 5
    drawLevel(screen, lvl, images, [blockWidth, blockHeight], [xOffset, yOffset])
    drawSprites(screen, player, images, [blockWidth, blockHeight], [xOffset, yOffset])
    drawText(screen, player)
