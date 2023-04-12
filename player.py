from math import floor, ceil


class Player:
    def __init__(self, lvlSpawn):
        col = lvlSpawn["c"]
        row = lvlSpawn["r"]
        self.spawn = {"c": col, "r": row}
        self.position = {"c": col, "r": row}
        self.xVelocity = 0
        self.yVelocity = 0
        self.lives = 1
        self.score = 0
        self.isRightPressed = False
        self.isLeftPressed = False
        self.isUpPressed = False
        self.isRightClear = True
        self.isLeftClear = True
        self.isTopClear = True
        self.isGrounded = True
        self.isAtFinish = False
        self.orientation = "right"

    def update(self, lvl):
        row = floor(self.position["r"])
        loweredCol = floor(self.position["c"])
        raisedCol = ceil(self.position["c"])

        # Check if player is in bounds
        if row > len(lvl) or row < -3:
            self.reset()
            self.lives -= 1

        # Collision Detection

        # Ceiling Detection
        try:
            if lvl[row - 1][loweredCol] == 0 or lvl[row - 1][raisedCol] == 0:
                self.isTopClear = True
            else:
                self.isTopClear = False
        except IndexError:
            self.isTopClear = True

        # Ground Detection
        try:
            if loweredCol < 0:
                self.isGrounded = False
            elif lvl[row + 1][loweredCol] == 1 or lvl[row + 1][raisedCol] == 1:
                self.isGrounded = True
            else:
                self.isGrounded = False
        except IndexError:
            self.isGrounded = False

        # Wall Detection

        # Left
        try:
            if loweredCol < 0:
                self.isLeftClear = True
            elif lvl[row][loweredCol] == 0 or \
                    lvl[row][loweredCol] == 2 or \
                    lvl[row][loweredCol] == 3 or \
                    lvl[row][loweredCol] == 4:
                self.isLeftClear = True
            else:
                self.isLeftClear = False
        except IndexError:
            self.isLeftClear = True

        # Right
        try:
            if loweredCol < 0:
                self.isRightClear = True
            elif lvl[row][raisedCol] == 0 or \
                    lvl[row][raisedCol] == 2 or \
                    lvl[row][raisedCol] == 3 or \
                    lvl[row][raisedCol] == 4:
                self.isRightClear = True
            else:
                self.isRightClear = False
        except IndexError:
            self.isRightClear = True

        # Movement

        # Right
        if not self.isRightClear:
            if self.xVelocity > 0:
                self.xVelocity = 0
        elif not self.isRightPressed:
            self.xVelocity = 0
        else:
            self.xVelocity = 0.15

        # Left
        if not self.isLeftClear:
            if self.xVelocity < 0:
                self.xVelocity = 0
        elif self.xVelocity <= 0 and not self.isLeftPressed:
            self.xVelocity = 0
        elif self.isLeftPressed:
            self.xVelocity = -0.15

        # Jumping
        if self.isUpPressed and self.isGrounded:
            self.yVelocity = -0.25

        # Gravity
        if self.yVelocity < 0:
            if self.yVelocity > -0.05 or not self.isTopClear:
                self.yVelocity = 0
            else:
                self.yVelocity *= 0.85
        else:
            if self.isGrounded:
                self.yVelocity = 0
            else:
                self.yVelocity = 0.125

        self.position["c"] += self.xVelocity
        self.position["r"] += self.yVelocity

        self.checkForCollectables(lvl)

    def checkForCollectables(self, lvl):
        row = floor(self.position["r"])
        loweredCol = floor(self.position["c"])
        raisedCol = ceil(self.position["c"])

        try:
            # Stars
            if lvl[row][loweredCol] == 2:
                self.score += 1
                lvl[row][loweredCol] = 0

            if lvl[row][raisedCol] == 2:
                self.score += 1
                lvl[row][raisedCol] = 0

            # Hearts
            if lvl[row][loweredCol] == 3:
                self.lives += 1
                lvl[row][loweredCol] = 0

            if lvl[row][raisedCol] == 3:
                self.lives += 1
                lvl[row][raisedCol] = 0

            # Flag
            if lvl[row][loweredCol] == 4:
                self.isAtFinish = True

            if lvl[row][raisedCol] == 4:
                self.isAtFinish = True

        except IndexError:
            pass

    def reset(self):
        self.position["c"], self.position["r"] = self.spawn["c"], self.spawn["r"]
