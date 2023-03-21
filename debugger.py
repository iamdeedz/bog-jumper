import pygame as p


class Debugger:
    def __init__(self, screen):
        p.init()
        self.screen = screen
        self.font = p.font.Font("freesansbold.ttf", 15)

    def update(self, player, lvl):
        title = self.font.render(f"Debugger", True, p.Color("green"))
        xVelocityText = self.font.render(f"Player X Velocity = {player.xVelocity}", True, p.Color("green"))
        yVelocityText = self.font.render(f"Player y Velocity = {player.yVelocity}", True, p.Color("green"))
        xPosText = self.font.render(f"Player x Position = {round(player.position['c'], 2)}", True, p.Color("green"))
        yPosText = self.font.render(f"Player y Position = {round(player.position['r'], 2)}", True, p.Color("green"))
        isGroundedText = self.font.render(f"Player isGrounded = {player.isGrounded}", True, p.Color("green"))
        isRightClearText = self.font.render(f"Player isRightClear = {player.isRightClear}", True, p.Color("green"))
        isLeftClearText = self.font.render(f"Player isLeftClear = {player.isLeftClear}", True, p.Color("green"))
        isRightPressedText = self.font.render(f"Player isRightPressed = {player.isRightPressed}", True, p.Color("green"))
        isLeftPressedText = self.font.render(f"Player isLeftPressed = {player.isLeftPressed}", True, p.Color("green"))
        spawnText = self.font.render(f"Player spawn = {player.spawn}", True, p.Color("green"))
        lvlText = self.font.render(f"Level = {lvl}", True, p.Color("green"))
        texts = [title, xVelocityText, yVelocityText, xPosText, yPosText, lvlText, isGroundedText, isRightClearText,
                 isLeftClearText, spawnText, isRightPressedText, isLeftPressedText]
        for i in range(len(texts)):
            txt = texts[i]
            self.screen.blit(txt, p.Rect(1290, (i * 20) + 20, 0, 0))
