from math import floor, ceil


class Player:
    def __init__(self, lvlSpawn):
        col = lvlSpawn["c"]
        row = lvlSpawn["r"]
        self.spawn = {"c": col, "r": row}
        self.position = {"c": col, "r": row}
        self.xVelocity = 0
        self.yVelocity = 0
        self.isRightPressed = False
        self.isLeftPressed = False
        self.isRightClear = True
        self.isLeftClear = True
        self.isGrounded = True

    def update(self, lvl):
        self.xVelocity = 0
        self.yVelocity = 0
        row = floor(self.position["r"])
        loweredCol = floor(self.position["c"])
        raisedCol = ceil(self.position["c"])

        # Collision Detection
        if isInBounds(self, lvl):

            # Ground Detection
            if lvl[row + 1][loweredCol] == 1 or lvl[row + 1][raisedCol] == 1:
                self.isGrounded = True
            else:
                self.isGrounded = False

            # Wall Detection

            # Left
            if lvl[row][loweredCol] == 0:
                self.isLeftClear = True
            else:
                self.isLeftClear = False

            # Right
            if lvl[row][raisedCol] == 0:
                self.isRightClear = True
            else:
                self.isRightClear = False

        else:
            self.reset()

        # Movement

        # Right
        if not self.isRightClear:
            self.xVelocity = 0
        elif self.isRightPressed:
            self.xVelocity = 0.15

        # Left
        if not self.isLeftClear:
            if self.xVelocity < 0:
                self.xVelocity = 0
        elif self.isLeftPressed:
            self.xVelocity = -0.15

        # Gravity
        if not self.isGrounded:
            self.yVelocity = 0.125
        elif (self.position["r"] + self.yVelocity) != self.position["r"]:
            self.yVelocity = 0

        # Change Position
        self.position["c"] += self.xVelocity
        self.position["r"] += self.yVelocity

    def reset(self):
        self.position["c"], self.position["r"] = self.spawn["c"], self.spawn["r"]


def isInBounds(player, lvl):
    row = floor(player.position["r"])
    loweredCol = floor(player.position["c"])
    raisedCol = ceil(player.position["c"])
    longestRow = lvl[0]

    for i in range(len(lvl)):
        if len(lvl[i]) > len(longestRow):
            longestRow = lvl[i]

    return 0 <= row + 1 < len(longestRow) and \
        0 <= loweredCol < len(longestRow) and \
        0 <= raisedCol < len(longestRow) and \
        0 <= row < len(lvl) and \
        0 <= loweredCol < len(lvl[row]) and \
        0 <= raisedCol < len(lvl[row])
