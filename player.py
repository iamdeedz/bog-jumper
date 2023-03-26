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
        self.isUpPressed = False
        self.isRightClear = True
        self.isLeftClear = True
        self.isTopClear = True
        self.isGrounded = True
        self.longestRow = None

    def update(self, lvl):
        self.xVelocity = 0
        self.yVelocity = 0
        row = floor(self.position["r"])
        loweredCol = floor(self.position["c"])
        raisedCol = ceil(self.position["c"])

        # Check if player is below map
        if row > len(lvl):
            self.reset()

        # Collision Detection

        # Ceiling Detection
        try:
            if lvl[row - 1][loweredCol] == 0 or lvl[row - 1][raisedCol] == 0:
                self.isTopClear = True
            else:
                self.isTopClear = False
        except IndexError:
            self.isTopClear = False

        # Ground Detection
        try:
            if lvl[row + 1][loweredCol] == 1 or lvl[row + 1][raisedCol] == 1:
                self.isGrounded = True
            else:
                self.isGrounded = False
        except IndexError:
            self.isGrounded = False

        # Wall Detection

        # Left
        try:
            if lvl[row][loweredCol] == 0:
                self.isLeftClear = True
            else:
                self.isLeftClear = False
        except IndexError:
            self.isLeftClear = True

        # Right
        try:
            if lvl[row][raisedCol] == 0:
                self.isRightClear = True
            else:
                self.isRightClear = False
        except IndexError:
            self.isRightClear = True

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
