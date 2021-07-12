import pygame,random
from car import Car
from bush import Bush
from border import Border
from coins import Coin
from selector import Selector
from speed_lines import SpeedLines
pygame.init()

#COLOURS
GREEN = (0,225,0)
DARK_GREEN = (1,50,32)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
BLUE = (100,100,255)
BLACK = (0,0,0)
DARK_GREY = (50,50,50)
LIGHT_GREY = (200,200,200)
GREY = (150,150,150)
MATT_GREY = (25,25,25)
GOLD = (238,181,1)
LIGHT_GOLD = (243,199,13)
DARK_GOLD = (233,173,3)
SKY_BLUE = (0,89,179)
custom=(0,0,0)
FLAME = (255,162,0)
DARK_WHITE = (254,254,254)
DARK_RED = (135,1,1)

colourList=[RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE,BLACK,GOLD]

#Random Number Function (ran = random)
def ran(start,end):
    number=random.randint(start,end)
    return number

#Variables
colorList = (RED,GREEN,PURPLE,YELLOW,CYAN,BLUE)
selectList=[1,2,3]
playerColour=RED

#CONSTANTs
SCREENWIDTH=800
SCREENHEIGHT=900
MAINHEIGHT=SCREENHEIGHT-200
SIZE = (SCREENWIDTH,SCREENHEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Wrong Turn")
super_large_font=pygame.font.Font('freesansbold.ttf',150)
font = pygame.font.Font('freesansbold.ttf',32)
medium_font = pygame.font.Font('freesansbold.ttf',45)
large_font = pygame.font.Font('freesansbold.ttf',70)


def play():
    #GAME VARIABLES
    speed=1
    score=0
    crash=False
    textdisplayed=False
    carryOn = True
    pygame.time.set_timer(pygame.USEREVENT,1000)
    time=0
    coins=0
    destination = 10000
    totaltime=0
    clock = pygame.time.Clock()
    distance=0
    playerspeed=0
    crash_complete=False
    brake=False
    time_top_speed=0
    max_speed=False
    #Sprites



    #Creating Sprites
    #Sprite name = Car( FUNCTION THIS IS THE FUNCTION FROM CAR.PY, color, width, height)

    
    

    playerCar = Car(playerColour,60,80,70)
    playerCar.rect.x = 160
    playerCar.rect.y = MAINHEIGHT - 100
    
    car1 = Car(PURPLE,60,80,random.randint(50,100))
    car1.rect.x = 60
    car1.rect.y = -100

    car2 = Car(YELLOW,60,80,random.randint(50,100))
    car2.rect.x = 160
    car2.rect.y = -600

    car3 = Car(CYAN,60,80,random.randint(50,100))
    car3.rect.x = 260
    car3.rect.y = -300

    car4 = Car(BLUE,60,80,random.randint(50,100))
    car4.rect.x = 360
    car4.rect.y = -900

    bush1 = Bush(ran(50,60),100,DARK_GREEN)
    bush1.rect.x = ran(440,800)
    bush1.rect.y = -ran(10,100)

    bush2 = Bush(ran(50,60),100,DARK_GREEN)
    bush2.rect.x=ran(440,800)
    bush2.rect.y=-ran(10,100)

    bush3=Bush(ran(50,60),100,DARK_GREEN)
    bush3.rect.x=ran(440,800)
    bush3.rect.y=-ran(10,100)

    bush4=Bush(ran(50,60),100,DARK_GREEN)
    bush4.rect.x=ran(440,800)
    bush4.rect.y=-ran(10,100)

    bush5 = Bush(ran(50,60),100,DARK_GREEN)
    bush5.rect.x = ran(440,800)
    bush5.rect.y=-ran(200,600)

    bush6 = Bush(ran(50,60),100,DARK_GREEN)
    bush6.rect.x=ran(440,800)
    bush6.rect.y=-ran(200,600)

    bush7 = Bush(ran(50,60),100,DARK_GREEN)
    bush7.rect.x=ran(440,800)
    bush7.rect.y=-ran(200,600)

    bush8 = Bush(ran(50,60),100,DARK_GREEN)
    bush8.rect.x=ran(440,800)
    bush8.rect.y=-ran(200,600)

    bush9 = Bush(ran(50,60),100,DARK_GREEN)
    bush9.rect.x=ran(440,600)
    bush9.rect.y=-ran(200,800)

    explosion_radius=(ran(120,130))
    explosion=Bush(explosion_radius,0,FLAME)
    explosion.rect.x=-200
    explosion.rect.y=0

    borderl = Border(100,MAINHEIGHT)
    borderl.rect.x=-80
    borderl.rect.y=0

    borderr = Border(100,MAINHEIGHT)
    borderr.rect.x=780
    borderr.rect.y=0

    speedlines1_height=ran(300,600)
    speedlines1=SpeedLines(ran(5,10),speedlines1_height,DARK_WHITE)
    speedlines1.rect.x=ran(0,SCREENWIDTH)
    speedlines1.rect.y=0-speedlines1_height*ran(200,600)

    speedlines2_height=ran(300,600)
    speedlines2=SpeedLines(ran(5,10),speedlines2_height,DARK_WHITE)
    speedlines2.rect.x=ran(0,SCREENWIDTH)
    speedlines2.rect.y=0-speedlines2_height*ran(200,600)

    speedlines3_height=ran(300,600)
    speedlines3=SpeedLines(ran(5,10),speedlines3_height,DARK_WHITE)
    speedlines3.rect.x=ran(0,SCREENWIDTH)
    speedlines3.rect.y=0-speedlines3_height*ran(200,600)

    speedlines4_height=ran(300,600)
    speedlines4=SpeedLines(ran(5,10),speedlines4_height,DARK_WHITE)
    speedlines4.rect.x=ran(0,SCREENWIDTH)
    speedlines4.rect.y=0-speedlines4_height*ran(200,600)

    

    coin1=Coin(10,10,LIGHT_GOLD,DARK_GOLD,GOLD,10,10,DARK_GOLD,32)



    
    #Speed lines list
    all_speedlines_list = pygame.sprite.Group()
    all_speedlines_list.add(speedlines1)
    all_speedlines_list.add(speedlines2)
    all_speedlines_list.add(speedlines3)
    all_speedlines_list.add(speedlines4)
    

    #This is a list, hence the name list, it puts all the sprites in a group fir ez detecting, they also must be so that update can be used
    all_bushes_list = pygame.sprite.Group()
    all_bushes_list.add(bush1)
    all_bushes_list.add(bush2)
    all_bushes_list.add(bush3)
    all_bushes_list.add(bush4)
    all_bushes_list.add(bush5)
    all_bushes_list.add(bush6)
    all_bushes_list.add(bush7)
    all_bushes_list.add(bush8)
    all_bushes_list.add(bush9)

    #this adds our playerCar to the group of sprites
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(bush1)
    all_sprites_list.add(bush2)
    all_sprites_list.add(bush3)
    all_sprites_list.add(bush4)
    all_sprites_list.add(bush5)
    all_sprites_list.add(bush6)
    all_sprites_list.add(bush7)
    all_sprites_list.add(bush8)
    all_sprites_list.add(bush9)
    all_sprites_list.add(borderl)
    all_sprites_list.add(borderr)
    all_sprites_list.add(explosion)
    all_sprites_list.add(speedlines1)
    all_sprites_list.add(speedlines2)
    all_sprites_list.add(speedlines3)
    all_sprites_list.add(speedlines4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    all_borders_list = pygame.sprite.Group()
    all_borders_list.add(borderl)
    all_borders_list.add(borderr)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if crash == False:
                    time +=1
                    totaltime+=time
                    if max_speed == True:
                        time_top_speed+=1
            if event.type == pygame.QUIT:
                carryOn = False
            if crash == True:
                pygame.time.wait(500)
                explosion.rect.x=-200
                explosion.rect.y=0
                playerCar.rect.x=-200
                playerCar.rect.y=0
                crash_complete=True
                return False,distance,score,totaltime,time_top_speed

            #This detects when the type of event is key pressed
            elif event.type==pygame.KEYDOWN:
                #This detects if the key that is pressed down is Key X
                if event.key==pygame.K_x:
                    #Quits the game
                    carryOn=False
        if speed >= 4:
            speed = 3.9
            max_speed=True
        else:
            max_speed=False

        if playerCar.rect.x >= 40 and playerCar.rect.x <= 400:
            if speed >= 4:
                speed = 3.9
                max_speed=True
            else:
                max_speed=False
        else:
            if speed >= 3:
                speed-=0.05
                max_speed=True
            else:
                max_speed=False
        #This makes key == to the key pressed
        if crash==False:
            if speed <= 0:
                speed = 0
                min_speed=True
            else:
                min_speed=False
            keys = pygame.key.get_pressed()
            #If key is equal to Key Left arrow
            if keys[pygame.K_SPACE]:
                speed-=0.005
                if speed >= 1:
                    if keys[pygame.K_RIGHT]:
                        playerCar.moveRight(10)
                        print("no")
                    if keys[pygame.K_LEFT]:
                        playerCar.moveLeft(10)
                        print("hi")
            elif not keys[pygame.K_SPACE]:
                if min_speed == False:
                    if keys[pygame.K_LEFT]:
                        #Then playercar.will carry the procedure move left 5
                        playerCar.moveLeft(5)
                    if keys[pygame.K_RIGHT]: 
                        playerCar.moveRight(5)
                    if keys[pygame.K_DOWN]:
                        speed -= 0.01
                    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                        speed -=0.0025
                if keys[pygame.K_UP]:
                    speed += 0.005

            if keys[pygame.K_DOWN] or keys[pygame.K_SPACE]:
                brake=True
            else:
                brake=False

        #SPEED LINES CALCULATIONS
        for speedlines in all_speedlines_list:
            if speed >= 2:
                speedlines.moveForward(speed*10)
            else:
                speedlines.rect.y=-ran(600,3000)
            if speedlines.rect.y > SCREENHEIGHT:
                speedlines.rect.y=-ran(600,900)*2-ran(200,600)
                speedlines.rect.x=ran(0,SCREENWIDTH)
            
        
        #Distance Calculations
        playerspeed=speed
        if min_speed == True:
            playerspeed = speed
        if max_speed == True:
            playerspeed=4
        distance+=playerspeed

        #Score Calculations
        score = distance/100 + coins

        #Car Speed and shit
        for car in all_coming_cars:
            carspeed = speed
            if crash==False:
                if carspeed <= 1:
                    carspeed=1.5
            car.moveForward(carspeed)
            if car.rect.y > MAINHEIGHT:
                car.changeSpeed(random.randint(50,100))
                car.repaint(random.choice(colorList))
                car.rect.y=-200

        for bush in all_bushes_list:
            bush.moveForward(speed)
            if bush.rect.y > MAINHEIGHT:
                bush.rect.y=-ran(1,200)

        #Collision detection
        border_collision_list=pygame.sprite.spritecollide(playerCar,all_borders_list,False)
        car_collision_list=pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        bush_collision_list=pygame.sprite.spritecollide(playerCar,all_bushes_list,False)
        if crash_complete == False:
            for border in border_collision_list:
                speed=0
                crash=True
                explosion.rect.x=playerCar.rect.x-explosion_radius/4
                explosion.rect.y=playerCar.rect.y-20
                if textdisplayed==False:
                    print("Car Crash!")
                    textdisplayed=True
            for car in car_collision_list:
                speed=0
                crash=True
                explosion.rect.x=playerCar.rect.x-explosion_radius/4
                explosion.rect.y=playerCar.rect.y-20
                if textdisplayed==False:
                    print("Car Crash!")
                    textdisplayed=True
            for bush in bush_collision_list:
                speed=0
                crash=True
                explosion.rect.x=playerCar.rect.x-explosion_radius/4
                explosion.rect.y=playerCar.rect.y-20
                if textdisplayed==False:
                    print("Tree wipeout!")
                    textdisplayed=True

        all_sprites_list.update()
    
        screen.fill(GREEN)
        pygame.draw.rect(screen,GREY,[40,0,400,MAINHEIGHT])
        pygame.draw.line(screen,WHITE,[40,0],[40,MAINHEIGHT],5)
        pygame.draw.line(screen,WHITE,[440,0],[440,MAINHEIGHT],5)
        pygame.draw.line(screen,WHITE,[140,0],[140,MAINHEIGHT],4)
        pygame.draw.line(screen,WHITE,[240,0],[240,MAINHEIGHT],4)
        pygame.draw.line(screen,WHITE,[340,0],[340,MAINHEIGHT],4)



        #Reset section
        #Resets sprites
        all_sprites_list.draw(screen)

        #THIS IS NOT A RESET JUST AN OVERLAY FIX
        pygame.draw.rect(screen,MATT_GREY,[0,700,SCREENWIDTH,200],0)
        pygame.draw.rect(screen,DARK_GREY,[0,700,SCREENWIDTH,200],10)
        circle_centre=(125,840)
        pygame.draw.circle(screen,LIGHT_GREY,circle_centre,100,0,True,True)
        pygame.draw.circle(screen,GREY,circle_centre,100,5,True,True)
        pygame.draw.rect(screen,LIGHT_GREY,[SCREENWIDTH/2-100,740,200,101])
        pygame.draw.rect(screen,GREY,[SCREENWIDTH/2-100,740,200,101],5)
        pygame.draw.rect(screen,LIGHT_GREY,[SCREENWIDTH/2+170,740,200,101])
        pygame.draw.rect(screen,GREY,[SCREENWIDTH/2+170,740,200,101],5)
        pygame.draw.rect(screen,LIGHT_GREY,[SCREENWIDTH/2-160,740,35,101])
        pygame.draw.rect(screen,GREY,[SCREENWIDTH/2-160,740,35,101],5)

        
        brake_triangle_points = ((257.5,750),(270,771.65063509),(245,771.65063509))
        if brake == True:
            pygame.draw.polygon(screen,RED,brake_triangle_points,0)
        else:
            pygame.draw.polygon(screen,DARK_RED,brake_triangle_points,0)

        fake_speed=str(int(round(speed*24,0)))+"m/s"
        fake_distance=str(int(round(distance,0)))+"m"
        fake_score=str(int(round(score,0)))+"pts"
        speed_display=font.render(str(fake_speed),True,BLACK)
        distance_display=font.render(str(fake_distance),True,BLACK)
        score_display=font.render(str(fake_score),True,BLACK)
        screen.blit(score_display,(580,780))
        screen.blit(distance_display,(310,780))
        screen.blit(speed_display,(90,780))

        if distance >= 500:
            print("YOU WIN")
            return True,distance,score,totaltime,time_top_speed

        
        #Resets Screen
        pygame.display.flip()
        clock.tick(60)

def startingScreen():
    #Starting Screen variables
    carryOn = True
    clock=pygame.time.Clock()

    #Sprites
    selector=Selector(BLACK,30,30)
    selector.rect.x=150
    selector.rect.y=208

    start_screen_sprite = pygame.sprite.Group()
    start_screen_sprite.add(selector)

    
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if selector.rect.y >= 608:
                selector.rect.y = 208
            else:
                selector.moveDown(100)
            pygame.time.wait(100)
        if keys[pygame.K_UP]:
            if selector.rect.y <= 208:
                selector.rect.y = 608
            else:
                selector.moveUp(100)
            pygame.time.wait(100)
        if keys[pygame.K_RETURN]:
            pygame.time.wait(100)
            if selector.rect.y == 208:
                return 1
            elif selector.rect.y == 308:
                return 2
            elif selector.rect.y == 408:
                return 3
            elif selector.rect.y == 508:
                return 4
            elif selector.rect.y == 608:
                return 5



        screen.fill(SKY_BLUE)
        title=large_font.render("Wrong Turn",True,WHITE)
        play_option=medium_font.render("Play",True,WHITE)
        customise_option=medium_font.render("Customise",True,WHITE)
        leaderboard_option=medium_font.render("Leaderboard",True,WHITE)
        info_option=medium_font.render("Information",True,WHITE)
        quit_option=medium_font.render("Quit",True,WHITE)
        screen.blit(title,(210,100))
        screen.blit(play_option,(210,200))
        screen.blit(customise_option,(210,300))
        screen.blit(leaderboard_option,(210,400))
        screen.blit(info_option,(210,500))
        screen.blit(quit_option,(210,600))

        start_screen_sprite.update()
        start_screen_sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
            
def customise():
    carryOn = True
    clock = pygame.time.Clock()
    right_arrow_points=((450,700),(500,700),(500,675),(550,725),(500,775),(500,750),(450,750))
    left_arrow_points=((350,700),(300,700),(300,675),(250,725),(300,775),(300,750),(350,750))
    custom=(0,0,0)
    colourchoice=0
    colorList = (RED,GREEN,PURPLE,YELLOW,CYAN,BLUE)

    #Sprites
    customise_sprites_list=pygame.sprite.Group()
    coming_cars_list=pygame.sprite.Group()

    speed=ran(25,50)
    car1=Car(ORANGE,ran(180,210),ran(280,310),speed)
    car1.rect.x =450
    car1.rect.y=-ran(0,500)

    coming_cars_list.add(car1)

    customise_sprites_list.add(car1)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                carryOn= False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            colourchoice-=1
            if colourchoice <= 0:
                colourchoice= len(colourList)-1
            pygame.time.wait(100)
            
        elif keys[pygame.K_RIGHT]:
            colourchoice+=1
            if colourchoice == len(colourList):
                colourchoice=0
            pygame.time.wait(100)
        if keys[pygame.K_RETURN]:
            pygame.time.wait(100)
            return colourList[colourchoice]
        
        playerCar=Car(colourList[colourchoice],200,300,0)
        playerCar.rect.x= 150
        playerCar.rect.y= 200
        customise_sprites_list.add(playerCar)

        for car in coming_cars_list:
            car.moveForward(speed)
            if car.rect.y>=SCREENHEIGHT:
                car.repaint(random.choice(colorList))
                car.changeSpeed(ran(10,25))
                car.rect.y=-ran(500,5000)


        screen.fill(GREEN)
        customise_sprites_list.update()
        pygame.draw.rect(screen,GREY,[100,0,600,SCREENHEIGHT])
        pygame.draw.line(screen,WHITE,[SCREENWIDTH/2,0],[SCREENWIDTH/2,SCREENHEIGHT],10)
        pygame.draw.polygon(screen,BLACK,right_arrow_points,0)
        pygame.draw.polygon(screen,BLACK,left_arrow_points,0)

        customise_sprites_list.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

def win(win_list):
    carryOn = True
    score="Score: " +str(int(round(win_list[2],0))) +"pts"
    time_top_speed="Top Speed Time: "+str(win_list[3]) +"s"
    totaltime="Total Time: "+str(win_list[4])+ "s"
    clock = pygame.time.Clock()
    time=0
    pygame.time.set_timer(pygame.USEREVENT,100)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn=False
            if event.type == pygame.USEREVENT:
                time +=0.1


        screen.fill(SKY_BLUE)
        win_display= large_font.render("You Win!",True,WHITE)
        distance_display= font.render("Distance Travelled: 10000",True,WHITE)
        score_display= font.render(score,True,WHITE)
        time_top_speed_display= font.render(time_top_speed,True,WHITE)
        totaltime_display= font.render(totaltime,True,WHITE)

        screen.blit(win_display,(80,100))
        if time >= 0.5:
            screen.blit(distance_display,(100,250))
        if time >= 1:
            screen.blit(totaltime_display,(100,300))
        if time >= 1.5:
            screen.blit(time_top_speed_display,(100,350))
        if time >= 2:
            pygame.draw.line(screen,WHITE,[100,400],[400,400],5)
        if time >= 3:
            screen.blit(score_display,(100,425))
        if time > 3.5:
            pygame.draw.rect(screen,WHITE,[200,500,400,50])
            pygame.draw.rect(screen,GREY,[200,500,400,50],5)
            text=font.render("SPACEBAR",True,GREY)
            screen.blit(text,(305,510))
            

        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            carryOn=False

        pygame.display.flip()
        clock.tick(60)


def lose(win_list):

    carryOn = True
    score="Score: " +str(int(round(win_list[2],0))) +"pts"
    distance="Distance Travelled: "+str(int(round(win_list[1],0))) +"m"
    time_top_speed="Top Speed Time: "+str(win_list[3]) +"s"
    totaltime="Total Time: "+str(win_list[4])+ "s"
    clock = pygame.time.Clock()
    time=0
    pygame.time.set_timer(pygame.USEREVENT,100)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn=False
            if event.type == pygame.USEREVENT:
                time +=0.1


        screen.fill(SKY_BLUE)
        win_display= super_large_font.render("You Lose",True,WHITE)
        distance_display= font.render(distance,True,WHITE)
        score_display= font.render(score,True,WHITE)
        time_top_speed_display= font.render(time_top_speed,True,WHITE)
        totaltime_display= font.render(totaltime,True,WHITE)

        screen.blit(win_display,(80,100))
        if time >= 0.5:
            screen.blit(distance_display,(100,250))
        if time >= 1:
            screen.blit(totaltime_display,(100,300))
        if time >= 1.5:
            screen.blit(time_top_speed_display,(100,350))
        if time >= 2:
            pygame.draw.line(screen,WHITE,[100,400],[400,400],5)
        if time >= 3:
            screen.blit(score_display,(100,425))
        if time > 3.5:
            pygame.draw.rect(screen,WHITE,[200,500,400,50])
            pygame.draw.rect(screen,GREY,[200,500,400,50],5)
            text=font.render("SPACEBAR",True,GREY)
            screen.blit(text,(305,510))
            

        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            carryOn=False

        pygame.display.flip()
        clock.tick(60)
    
while True:
    select = startingScreen()
    if select == 1:
        win_list=play()
        if win_list[0] == True:
            win(win_list)
        elif win_list[0] == False:
            lose(win_list)
            pass
    elif select == 2:
        playerColour=customise()
    elif select == 3:
        print("nicest")
    elif select == 4:
        print("sexy")
    elif select == 5:
        break
pygame.quit()
