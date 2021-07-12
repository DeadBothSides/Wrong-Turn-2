import pygame

GREEN = (0,255,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)

#Sprite Class goes here
#class = def but as a pygame control, Car is a variable and the bit inside the brackets is calling the sprite class event
class Car(pygame.sprite.Sprite):
    #This is defining the constructor __init__ it is used when the sprite is first created, it defines all of the properties
    #Self is basically us referencing the current object.
    def __init__(self,color,width,height,speed):
        #Call the parent class (Sprite) constructor
        super().__init__()

        #Sets the color of the car, and its x y width and height
        #Set the background color and set it to be transparent or the same as the background
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Initialises attributes of the car
        self.width=width
        self.height=height
        self.color=color
        self.speed=speed
        #Make the shape, make all the actual numbers = the variable as these will be put in through functions
        pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])
        #Fetch the rectangle object that has the dimesnions of the image
        self.rect = self.image.get_rect()
    #Movement

    #This takes 2 arguments, the first one is called self. we know what that is
    #The second one is pixels, use ur brain dingus
    def moveRight(self,pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels


    def moveForward(self,speed):
        self.rect.y += self.speed * speed / 20
    def moveBackward(self,speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self,speed):
        self.speed=speed
    
    def repaint(self,color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0,0,self.width, self.height])
