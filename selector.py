import pygame

WHITE = (255,255,255)

class Selector(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.colour=colour
        self.width=width
        self.height=height

        pygame.draw.rect(self.image,self.colour,[0,0,self.width,self.height])
        self.rect=self.image.get_rect()

    def moveUp(self,distance):
        self.rect.y-=distance

    def moveDown(self,distance):
        self.rect.y+=distance
