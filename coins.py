import pygame

WHITE=(255,255,255)


class Coin(pygame.sprite.Sprite):
    def __init__(self,radius,points,light_colour,dark_colour,base_colour,text_x,text_y,text_colour,font_size):
        super().__init__()
        self.image=pygame.Surface([radius,radius])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.radius=radius
        self.light_colour=light_colour
        self.base_colour=base_colour
        self.points=points
        self.base_colour = base_colour
        self.light_colour = light_colour
        self.dark_colour = dark_colour
        

        pygame.draw.circle(self.image,self.base_colour,[0,0],self.radius,0)
        pygame.draw.circle(self.image,self.dark_colour,[0,0],self.radius,10,False,False,False,True)
        pygame.draw.circle(self.image,self.light_colour,[0,0],self.radius,10,True,True,True,False)
        pygame.draw.circle(self.image,self.dark_colour,[0,0],self.radius,10)
        font=pygame.font.Font('freesansbold.ttf',font_size)
        
        text=font.render(str(self.points),True,text_colour)
        
        

        
