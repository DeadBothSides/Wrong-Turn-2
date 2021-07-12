import pygame

WHITE=(255,255,255)

class SpeedLines(pygame.sprite.Sprite):
    def __init__(self,width,height,colour):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.colour=colour
        
        pygame.draw.rect(self.image,self.colour,[0,0,self.width,self.height])
        self.rect=self.image.get_rect()

    def moveForward(self,speed):
        self.rect.y += speed
