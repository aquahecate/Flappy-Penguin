import pygame
from sys import exit
from random import randint

def displayscore ():
    currenttime = int (pygame.time.get_ticks()/1000) - starttime
    scoremessage = font.render (f'Score: {currenttime}', False, 'Navy blue')
    scoremessagerect = scoremessage.get_rect (center = (700,45))
    screen.blit (scoremessage, scoremessagerect)
    return currenttime


def penganimation ():
    global pengcurrentpos, pengindex

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        pengcurrentpos = pengsurface1
    else:
        pengindex += 0.1
        if pengindex >= len (penglist):
            pengindex = 0
        pengcurrentpos = penglist[int (pengindex)]


pygame.init ()

#basic setup
screen = pygame.display.set_mode ((800,450))
pygame.display.set_caption ("Flappy Penguin")
clock = pygame.time.Clock ()
font = pygame.font.Font ('font/Pixeltype.ttf',40)

#endscreen
endsurface = pygame.Surface ((800,450))
endsurface.fill ('#2a55a3')

endpeng = pygame.image.load ('graphics/endpenguin.png').convert_alpha()
endpeng = pygame.transform.scale (endpeng, (260,160))
endpengrect = endpeng.get_rect (center = (400,200))


#background
bgsurface = pygame.image.load ('graphics/water.png').convert_alpha()
bgsurface = pygame.transform.scale (bgsurface, (800,450))

#player-penguin upwards
pengsurface1 = pygame.image.load ('graphics/peng1.png').convert_alpha()
pengsurface1 = pygame.transform.scale (pengsurface1, (150,90))
pengrect = pengsurface1.get_rect (center = (100,200))

pengmask = pygame.mask.from_surface (pengsurface1)

#player-penguin downwards
pengsurface2 = pygame.image.load ('graphics/peng2.png').convert_alpha()
pengsurface2 = pygame.transform.scale (pengsurface2, (150,90))

#player-penguin list
pengindex = 0
penglist = [pengsurface1, pengsurface2]
pengcurrentpos = penglist [pengindex]



penggravity = 0


#obstacle-pipes
width = 60
height = 200
gap = 200

pipeupsurface = pygame.image.load ('graphics/pipeup.png').convert_alpha()
pipeupsurface = pygame.transform.scale (pipeupsurface, (width,height))
pipeuprect = pipeupsurface.get_rect (midbottom = (800,200))


pipedownsurface = pygame.transform.flip (pipeupsurface,False,True)
pipedownrect = pipedownsurface.get_rect (midbottom = (800,600))


pipeupmask = pygame.mask.from_surface (pipeupsurface)
pipedownmask = pygame.mask.from_surface (pipedownsurface)


#timer
pipetimer = pygame.USEREVENT + 1
pygame.time.set_timer (pipetimer, 900)



gameactive = True

starttime = 0
currenttime = 0

score = 0

pipelist = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

  
        if event.type == pipetimer:
            randompipepost = randint (150,300)
            randompipeposb = randint (150,300)
            penguinheight = 120


            bottompipe = pipedownsurface.get_rect (midtop = (800, randompipeposb + penguinheight))
            toppipe = pipeupsurface.get_rect (midbottom = (800, randompipepost - penguinheight))
    
            
            pipelist.extend ([bottompipe, toppipe])
            
    
        if gameactive:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                penggravity = -15

            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameactive = True
                pengrect.midbottom = (100,225)
                penggravity = 0
                starttime = int (pygame.time.get_ticks ()/1000)
                pipelist.clear()


                
                    

    if gameactive: 
         penggravity += 1
         pengrect.y += penggravity
         screen.blit (bgsurface,(0,0))

         penganimation()
         screen.blit (pengcurrentpos, pengrect)
         
         if pengrect.centery >= 450 or pengrect.centery <= 0:
            gameactive = False

        
         for pipe in pipelist:
             pipe.x -= 5


         for pipe in pipelist:
            offsetx = pipe.x - pengrect.x
            offsety = pipe.y - pengrect.y

            currentpipemask = pipedownmask if pipe.bottom >=450 else pipeupmask

            if pengmask.overlap (currentpipemask, (offsetx, offsety)):
                gameactive = False

            pipelist = [pipe for pipe in pipelist if pipe.right > -60]


         for pipe in pipelist:
             if pipe.bottom >= 450:
                 screen.blit (pipedownsurface, pipe)
             else:
                 screen.blit (pipeupsurface, pipe)

         score = displayscore()
        


    else:
        screen.blit (endsurface, (0,0))
        endmessage = font.render ('press Space to restart the game', False, 'White')
        endmessagerect = endmessage.get_rect (center = (400,100))
        screen.blit (endmessage, endmessagerect)

        screen.blit (endpeng, endpengrect)


        scoretext = font.render (f'Your Score: {score}', False, 'White')
        scoretextrect = scoretext.get_rect (center = (400,300))
        screen.blit (scoretext,scoretextrect)



    pygame.display.update()

    clock.tick (60)

    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/aquahecate/Flappy-Penguin
    git push -u origin main

