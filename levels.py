import pygame as p

test = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]
for _ in range(5):
    test.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

levelSpawns = {"test": {"r": 1, "c": 2}
               }


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
    screen.blit(images["player"],
                p.Rect((player.position["c"] * blockWidth) + xOffset,
                       (player.position["r"] * blockHeight) + yOffset,
                       blockWidth, blockHeight))


def drawGame(screen, lvl, player, images, blockWidth, blockHeight):
    xOffset = blockWidth * 5
    yOffset = blockHeight * 5
    drawLevel(screen, lvl, images, [blockWidth, blockHeight], [xOffset, yOffset])
    drawSprites(screen, player, images, [blockWidth, blockHeight], [xOffset, yOffset])
