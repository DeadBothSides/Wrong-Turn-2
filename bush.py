import pygame

GREEN = (1,50,32)
WHITE = (255,255,255)
PI = 3.14159265358979323846264338327950288419716939937510582097494459230781

class Bush(pygame.sprite.Sprite):
    def __init__(self,radius,speed,colour):
        super().__init__()

        self.image=pygame.Surface([radius,radius])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.radius=radius
        self.speed=speed
        self.colour=colour

        pygame.draw.ellipse(self.image, self.colour, [0,0,self.radius,self.radius],0)
        self.rect=self.image.get_rect()

    def moveForward(self,speed):
        self.rect.y += self.speed * speed / 40
