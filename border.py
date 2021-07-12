import pygame

WHITE = (255,255,255)
GREY = (69,69,69)

class Border(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image=pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height

        pygame.draw.rect(self.image,GREY,[0,0,self.width,self.height],0)
        self.rect=self.image.get_rect()
