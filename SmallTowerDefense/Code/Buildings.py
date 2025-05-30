import pygame
import GameValues
from random import randint

class Building(pygame.sprite.Sprite):
    incomePerFrame = 0
    
    def __init__(self, pos, group , hp, makeSound, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.rect = self.image.get_rect(center = pos)
        if group != None:
           self.add(group)    
        self.hp = hp
        self.makeSound = makeSound
        
        
    def getIncome(self):
       GameValues.resource += self.incomePerFrame
        
   
class HeadQuarter(Building):
    incomePerFrame = 0.01

    def __init__(self, group , hp):
        randomPos = [randint(GameValues.WIDTH // 5, (4 * GameValues.WIDTH) // 5), randint(GameValues.HEIGHT // 5, (4 * GameValues.HEIGHT) // 5)]
        Building.__init__(self,pos = randomPos, group = group, hp = hp , makeSound = pygame.mixer.Sound("Sounds\createBuilding.mp3") , filename = "Sprites\hq.png")
        self.makeSound.set_volume(0.5)
    
   
class House(Building):
    incomePerFrame = 0.01
    
    def __init__(self, pos, group , hp):
        Building.__init__(self, pos, group, hp, makeSound = pygame.mixer.Sound("Sounds\createBuilding.mp3"), filename = "Sprites\house.png")
        self.makeSound.set_volume(0.15)





