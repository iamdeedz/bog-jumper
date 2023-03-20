import pygame as p


class Debugger:
    def __init__(self, screen):
        p.init()
        self.screen = screen
        self.font = p.font.Font("freesansbold.ttf", 15)

    def update(self, player, lvl):
        xVelocity, yVelocity = player.xVelocity, player.yVelocity
        xPosition, yPosition = round(player.position["c"], 2), round(player.position["r"], 2)
        isGrounded = player.isGrounded
        isRightClear, isLeftClear = player.isRightClear, player.isLeftClear
        spawn = player.spawn
        title = self.font.render(f"Debugger", True, p.Color("green"))
        xVelocityText = self.font.render(f"Player X Velocity = {xVelocity}", True, p.Color("green"))
        yVelocityText = self.font.render(f"Player y Velocity = {yVelocity}", True, p.Color("green"))
        xPosText = self.font.render(f"Player x Position = {xPosition}", True, p.Color("green"))
        yPosText = self.font.render(f"Player y Position = {yPosition}", True, p.Color("green"))
        isGroundedText = self.font.render(f"Player isGrounded = {isGrounded}", True, p.Color("green"))
        isRightClearText = self.font.render(f"Player isRightClear = {isRightClear}", True, p.Color("green"))
        isLeftClearText = self.font.render(f"Player isLeftClear = {isLeftClear}", True, p.Color("green"))
        spawnText = self.font.render(f"Player spawn = {spawn}", True, p.Color("green"))
        lvlText = self.font.render(f"Level = {lvl}", True, p.Color("green"))
        texts = [title, xVelocityText, yVelocityText, xPosText, yPosText, lvlText, isGroundedText, isRightClearText,
                 isLeftClearText, spawnText]
        for i in range(len(texts)):
            txt = texts[i]
            self.screen.blit(txt, p.Rect(1290, (i * 20) + 20, 0, 0))
