import pygame
import GameValues
from Buildings import House

class Text(pygame.sprite.Sprite):
    
    def __init__(self, massage, group, pos = [0, 0] ,font = None, fontSize = 15, color = GameValues.RED, backgroundColor = None , smooth = True):
        pygame.sprite.Sprite.__init__(self)
        self.massage = massage
        self.color = color
        self.backgroundColor = backgroundColor
        self.smooth = smooth
        self.f = pygame.font.SysFont(font, fontSize)
        self.image = self.f.render(self.massage, self.smooth, self.color, self.backgroundColor)
        self.rect = self.image.get_rect(center = pos)
        self.add(group)

    
    def Font(self, font = None, fontSize = 15):
        self.f = pygame.font.SysFont(font, fontSize)
        self.image = self.f.render(self.massage, self.smooth, self.color, self.backgroundColor)
    
    def Massage(self, massage):
        self.massage = massage
        self.image = self.f.render(self.massage, self.smooth, self.color, self.backgroundColor)

class resСounter(Text):

    def __init__(self, group):
        super().__init__("Resources: " + str(int(GameValues.resource)), group, font= 'serif', fontSize = 23  , color= GameValues.WHITE)
        self.rect.center = [self.rect.width // 2 + 5,self.rect.height // 2 + 5]
        
    def update(self, pos):
        for sprite in GameValues.buildings.sprites():
            sprite.getIncome()
        self.Massage("Resources: " + str(int(GameValues.resource)))
        
class Button(pygame.sprite.Sprite):
    
    def __init__(self, pos, group, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.add(group)
        
    def Click(self):
        pass
    
    
    
class ShopSlot(Button):
    
    locateMode = False
    
    def __init__(self, pos, group, filename, objectGen, cost, screen):
        super().__init__(pos, group ,filename)
        self.objectGen = objectGen
        self.cost = cost
        self.screen = screen

    def Click(self):
        if GameValues.resource >= self.cost:
            self.locateMode = True
            self.objectGen.rect.center = self.rect.center
         
        
    def update(self, pos):
                
        if self.locateMode:
            self.objectGen.rect.center = pos
            self.screen.blit(self.objectGen.image, self.objectGen.rect)
            
            
class Shop(pygame.sprite.Sprite):
    shop = pygame.sprite.Group()

    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        one = ShopSlot([200, 200], self.shop, "Sprites\icons\houseIcon.png",  House([500, 500], None, 10), screen)
        two =  ShopSlot([300, 200], self.shop, "Sprites\icons\houseIcon.png",  House([500, 500], None, 10), screen)
        shopSlots =  [one, two]
        self.rect = pygame.Rect.unionall(shopSlots)
        self.image = pygame.Surface((200, 200))
        

        
    
