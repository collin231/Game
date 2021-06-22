#games.py
#To be able to use the pygame functions  i would need to import pygame which i installed

import pygame


# prepares the pygame modules to get started 

pygame.init()

#These are the size of how the screen of the game will be displayed in terms of height and widthy

screen_width = 1049

screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

#the image of game characters (players and enemies ) will be loaded into the game through a pygame function
#these images must be in the same folder as the code
player = pygame.image.load("Player1.jpg")#https://www.google.com/url?sa=i&url=https%3A%2F%2Fsteemit.com%2Fenjoy%2F%40palashsaxena%2Fsmall-captain-america-2018-07-18-07-28-15&psig=AOvVaw03NruSRUpma9PIN5YsAMhW&ust=1616517460410000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCKjQ5Y7vxO8CFQAAAAAdAAAAABAD

enemy = pygame.image.load("enemy1.jpg")#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngkey.com%2Fdetail%2Fu2e6a9a9y3w7i1w7_avengers-villains-clipart-marvel-villain-in-chair%2F&psig=AOvVaw3duV8AIIVfyLSNl_wn7KDV&ust=1616517721492000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCLCanv-rxO8CFQAAAAAdAAAAABBC

enemy2 = pygame.image.load("enemy2.jpg")#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwebstockreview.net%2Fimage%2Favengers-clipart-villain-marvel%2F62913.html&psig=AOvVaw3duV8AIIVfyLSNl_wn7KDV&ust=1616517721492000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCLCanv-rxO8CFQAAAAAdAAAAABBI

enemy3 = pygame.image.load("enemy3.jpg")#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F645211084108692938%2F&psig=AOvVaw3duV8AIIVfyLSNl_wn7KDV&ust=1616517721492000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCLCanv-rxO8CFQAAAAAdAAAAABA6

#the "get" function is used to get the image's size in terms of width and height
# these measurments are stored in varibles "width" and "height" for each character
image_height = player.get_height()

image_width = player.get_width()

enemy_height = enemy.get_height()

enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()

enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()

enemy3_width = enemy3.get_width()

#the game prints out instructions to the user so they understand how to use the game

print("Welcome to the marvel game\nThe instructions are simple:\nDodge the enemies coming to you\nIf the enemies touch you then you lose\nIf pass through without you touching them then your win")

# the characters are given a starting point when the game begins so they starting points are stored in varible
#the points are on the y and x axis

playerXPosition = 100

playerYPosition = 100

enemyXPosition =  screen_width

enemyYPosition =  1

enemy2XPosition =  screen_width

enemy2YPosition =  230

enemy3XPosition =  screen_width

enemy3YPosition =  460

#for the player to be able to move they need to be input from the user which is by pressing keys on the keyboard
#varibles that will hold the keys need to be false as they can only be true when the game starts and the player starts pressing 
#this is to be able to use the if statement

keyUp= False

keyDown = False

keyRight=False

keyLeft=False

#to able to keep the game going and moving we need to use a while loop which allows everything to keep going until a certain the loop turns false(in this case, quiting, wining or losing)

while 1:
 #screeen fill allows you to have color or clear back        
    screen.fill(100)
#this implaits the start postions of the character as stated above
    screen.blit(player, (playerXPosition, playerYPosition))
         
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
         
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
         
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
#the flip function upadtes the screen in a way that the players and enemies can move around
    pygame.display.flip()

#the for loop allows all the event in the game such as pressing of keys, quiting the game, winnig and losing 
    for event in pygame.event.get():
# this if statement allows the game to stop when the user opts for the quit option 
        if event.type == pygame.QUIT:
            
            pygame.quit()
            
            exit(0) 
# this if statment is used when the user presses the up,down,left,right keys 
#pygame has function for keys which is k_ followed by the key
        if event.type == pygame.KEYDOWN:
             
            if event.key == pygame.K_UP: 
                keyUp = True
            
            if event.key == pygame.K_DOWN:
                keyDown = True
            
            if event.key ==pygame.K_LEFT:
                keyLeft=True
            
            if event.key==pygame.K_RIGHT:
                keyRight=True
#when the user is not pressing  a certain key it needs to be false so that it doesnt keep runing in the loop
#pygame has function for keys which is k_ followed by the key

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            
            if event.key == pygame.K_DOWN:
                keyDown = False
            
            if event.key ==pygame.K_LEFT:
                keyLeft=False
            
            if event.key==pygame.K_RIGHT:
                keyRight=False   
# once the for loop is running a direction for those keys need to be set otherwise there wont move
#a if statment is used to move the player depending on which postison he is in
#these statment also ensure that the user stays within the screen and not go out 
    if keyUp == True:
        
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        
        if playerXPosition > 0 : 
            playerXPosition -= 1
    if keyRight == True:
        
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1

# new variables need to be created for the bounding/creating the boxes of which the characters(player and enemies) are in
#this is for the program to be able to recoginze the if there is any collision of the boxes
    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition

    playerBox.left = playerXPosition

    enemyBox = pygame.Rect(enemy.get_rect())

    enemy2Box = pygame.Rect(enemy2.get_rect())

    enemy3Box = pygame.Rect(enemy3.get_rect())

    enemyBox.top = enemyYPosition

    enemy2Box.top = enemy2YPosition

    enemy3Box.top = enemy3YPosition
    
    enemyBox.left = enemyXPosition

    enemy2Box.left = enemy2XPosition

    enemy3Box.left = enemy3XPosition

#if statment is used in event that the boxes between the player and one of the enemies collide which will result in losing 
#a the user will see a message if they lose and the game will quit based on the statment

    if playerBox.colliderect(enemyBox):

        print("YOU LOST,TRY AGAIN!")
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
    
        
        print("YOU LOST,TRY AGAIN!")
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        
        print("YOU LOST,TRY AGAIN!")
        
        pygame.quit()
        exit(0)

#if the user doesnt lose then another if statment will be used to print a message if they win and the game will quit based on the statment 
#the win is only possibble once all the enemies being off the

    if (enemyXPosition < 0 - enemy_width) and (enemy2XPosition < 0 - enemy2_width) and (enemy3XPosition < 0 - enemy3_width) :
        
        print("YOU ARE PART OF THE AVENGERS YOU WON!")

        pygame.quit()
        
        exit(0)

#the speed of the enemies will be calculated based on the on the X axis 

    enemyXPosition -= 0.16
 
    enemy2XPosition -= 0.28
 
    enemy3XPosition -= 0.45
      
        
