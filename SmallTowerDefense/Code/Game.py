import pygame
import sys
import GameValues
from GameValues import buildings, gUI
from Buildings import HeadQuarter, House
from GUI import resСounter, ShopSlot

pygame.init()

sc = pygame.display.set_mode((GameValues.WIDTH, GameValues.HEIGHT))
clock = pygame.time.Clock()


hq = HeadQuarter(buildings, 10)
text = resСounter(gUI)
button = ShopSlot([26, 85], gUI, "Sprites\icons\houseIcon.png", House([500, 500], None, 10), 3 ,sc)
house = House([500, 500], buildings, 10)
pygame.mixer.music.load("Sounds\\background.mp3")

pygame.mixer.music.play(-1)
buildings.draw(sc)
gUI.draw(sc)      


pygame.display.update()

while True:
    
    clock.tick(GameValues.FPS)

    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            if button.rect.collidepoint(event.pos):
                button.Click()
            elif button.locateMode and not pygame.sprite.spritecollideany(button.objectGen, buildings):
                button.locateMode = False
                button.objectGen.makeSound.play()
                objectAdd = House(button.objectGen.rect.center, buildings,button.objectGen.hp)
                GameValues.resource -= button.cost
                

    sc.fill(GameValues.BLACK)
    buildings.draw(sc)
    gUI.update(mousePos)
    gUI.draw(sc)
    
    pygame.display.update()

    
