import pygame 
import random
import math
from pygame import mixer 
# intitalize the module pygame first step
pygame.init()
# setting window
mixer.music.load("C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\background.wav")
mixer.music.play(-1)
screen = pygame.display.set_mode((800,600))
# adding images
playerimage = pygame.image.load('C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\my.png')
playerimage1 = pygame.transform.scale(playerimage,(60,50))
enemyimage = pygame.image.load('C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\finall ufo.png')
#background image
bg =  pygame.image.load('C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\back.jpg')
bg1 = pygame.transform.scale(bg,(800,600))
# its a coordinate of sapceship 
playerX = 370
playerY = 480
player_movement = 0
# player_1 = 0
#its a coordinate of the enemy 
enemyX = []
enemyY = []
enemyimage1 = []
enemy_movement_X = []
enemy_movement_Y = []
no_of_enemies = 8
for i in range(no_of_enemies):
    enemyimage1.append(pygame.transform.scale(enemyimage,(60,50)))
    
    enemyX.append(random.randint(0,770))
    
    enemyY.append(random.randint(50,150))
    
    enemy_movement_X.append(0.5)
    
    enemy_movement_Y.append(30)
    
#score
score = 0 
textX = 10
textY = 10
font = pygame.font.Font("freesansbold.ttf",32)
def show_score(x,y):
    scoreval = font.render("Score: " + str(score), True,(255,255,255))
    screen.blit(scoreval,(x,y))
        
bulletimage = pygame.image.load('C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\bullet.png')
bulletimage1 = pygame.transform.scale(bulletimage,(40,30))
# Enemy management
bulletX = 0
bulletY = 490
bullet_movement_X = 0
bullet_movement_Y = 4
bullet_state = "ready"
def player(x,y):
    screen.blit(playerimage1,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimage1[i],(x,y))# its a function to mange the coordinnate
def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage1,(x,y))
    
# collision time
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance <= 27:
        return True
    else:
        return False
over_font = pygame.font.Font("freesansbold.ttf",64)
def gameover(x,y):
    sver = over_font.render("GAMEOVER",True,(255,255,255))
    screen.blit(sver,(x,y))
#setting icon and title
pygame.display.set_caption("First Game")
icon = pygame.image.load('C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\ufo2.png')
pygame.display.set_icon(icon)

# looping until cross event occurs
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(bg1,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # movement event in pygame 
        if event.type == pygame.KEYDOWN:
            # print("Key stroke is pressed")    
            if event.key == pygame.K_LEFT:
                player_movement -= 0.6                          
                # print("Left arrow is pressed")     
            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed")  
                player_movement += 0.6          
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletmusic = mixer.Sound("C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\laser.wav")
                    bulletmusic.play()
                    bulletX  = playerX
                    fire(bulletX,playerY)                                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("it is released")  
                player_movement = 0
                 
    playerX = playerX + player_movement               
    # playerY = playerY + player_1
    if playerX < 0:
        playerX = 0
    if playerX > 740:
        playerX = 740  
    for i in range(no_of_enemies):
        
        #Checking if gamover
            if enemyY[i] > 480:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                gameover(200,250)
                break
            enemyX[i] = enemyX[i] + enemy_movement_X[i]        
            if enemyX[i] < 0:
                enemy_movement_X[i] += 0.5
                enemyY[i] = enemyY[i] + enemy_movement_Y[i]
            if enemyX[i] > 750:
                enemy_movement_X[i] -=0.5
                enemyY[i] = enemyY[i] + enemy_movement_Y[i]
    
            collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                bulletY = 490
                bullet_state = "ready"  
                score += 1                       
               
                enemyX[i] = random.randint(0,740)
                enemyY[i] = random.randint(50,150)
                print(score)      
                explosion = mixer.Sound("C:\\Users\\ritish\\Desktop\\Programming language\\python practice 2020\\pygame\\explosion.wav")
                explosion.play()
            if score > 5:   
                enemyX[i] = enemyX[i] + enemy_movement_X[i]        
                if enemyX[i] < 0:
                    enemy_movement_X[i] += 0.5
                    enemyY[i] = enemyY[i] + enemy_movement_Y[i]
                if enemyX[i] > 750:
                    enemy_movement_X[i] -=0.5
                    enemyY[i] = enemyY[i] + enemy_movement_Y[i]
                    
            enemy(enemyX[i],enemyY[i],i)                   
    if bulletY <=0:
        bulletY = 490
        bullet_state = "ready"        
    if bullet_state is "fire":
        fire(bulletX,bulletY)
        bulletY -= bullet_movement_Y
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()            