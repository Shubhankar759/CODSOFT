# pygame and random module imported
import pygame
import random

#Window icon and name 
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Rock Paper Scissors")
Game_icon=pygame.image.load('Game_logo.png')
pygame.display.set_icon(Game_icon)

#all variables to handle user/computer inputs, number of rounds and result  
round=0
count_round=0
choice=0
comp_choice=0
score_your=0
score_comp=0
result=0

#all fonts used in game
font = pygame.font.SysFont('Roboto',40,bold=True)
font_1=pygame.font.SysFont('Roboto',25,bold=True)
font_2=pygame.font.SysFont('Roboto',45,bold=True)

#all text surfaces used in game
Quit = font.render('Quit',True,'white')
Start = font.render('Start',True,'white')
Round_1 = font.render('5 Rounds',True,'white')
Round_2 = font.render('10 Rounds',True,'white')
Round_3 = font.render('15 Rounds',True,'white')
Round_4 = font.render('20 Rounds',True,'white')
Next = font.render('Next',True,'white')
Retry = font.render('Retry',True,'white')
Exit = font.render('Exit',True,'white')

#all images imported
Rock = pygame.image.load('Rock.png')
Rock = pygame.transform.scale(Rock,(100,100))
Paper = pygame.image.load('Paper.png')
Paper = pygame.transform.scale(Paper,(100,100))
Scissors = pygame.image.load('Scissors.png')
Scissors = pygame.transform.scale(Scissors,(100,100))
Game_icon_ingame = pygame.transform.scale(Game_icon,(300,300))

#all buttons for user interaction
Quit_button =  pygame.Rect(250,350,68,30)
Start_button = pygame.Rect(90,350,68,30)
Round_button_1 = pygame.Rect(135,150,130,30)
Round_button_2 = pygame.Rect(130,200,140,30)
Round_button_3 = pygame.Rect(130,250,140,30)
Round_button_4 = pygame.Rect(130,300,140,30)
Rock_button = Rock.get_rect(center=(70,300))
Paper_button = Paper.get_rect(center=(200,300))
Scissors_button = Scissors.get_rect(center=(330,300))
Next_button = pygame.Rect(173,410,60,30)
Retry_button=pygame.Rect(70,410,70,30)
Exit_button = pygame.Rect(260,410,60,30)

#all states of application
run =True
Menu_state=True
Rounds_state=False
Game_state=False
still_game_state=False
Final_state=False

#collection of surfaces and function to display on current screen
def Start_menu():
     pygame.draw.rect(screen,('black'),Quit_button)
     pygame.draw.rect(screen,('black'),Start_button)
    
     screen.blit(Quit, (Quit_button.x,Quit_button.y))
     screen.blit(Start,(Start_button.x,Start_button.y))
   
     Title=font_2.render("ROCK PAPER SCISSORS",True,'white')
     screen.blit(Title,(12,30))
     
     screen.blit(Game_icon_ingame,(50,50))

def Round_menu():
    
     text_1 = font.render("Choose number of rounds",True,"white")
     
     pygame.draw.rect(screen,('black'),Round_button_1)
     screen.blit(Round_1,(Round_button_1.x,Round_button_1.y))
     
     pygame.draw.rect(screen,('black'),Round_button_2)
     screen.blit(Round_2,(Round_button_2.x,Round_button_2.y))
     
     pygame.draw.rect(screen,('black'),Round_button_3)
     screen.blit(Round_3,(Round_button_3.x,Round_button_3.y))
     
     pygame.draw.rect(screen,('black'),Round_button_4)
     screen.blit(Round_4,(Round_button_4.x,Round_button_4.y))
     
     screen.blit(text_1,(20,50))
     
def Game():
    
    pygame.draw.rect(screen,('black'),Rock_button)
    screen.blit(Rock,Rock_button)
    
    pygame.draw.rect(screen,('black'),Paper_button)
    screen.blit(Paper,Paper_button)
    
    pygame.draw.rect(screen,('black'),Scissors_button)
    screen.blit(Scissors,Scissors_button)
    
    
    text_3 = font.render(f"Round {count_round+1}",True,'white')
    if count_round<round:screen.blit(text_3,(130,10))
    
    if  still_game_state and count_round<=round:
     text_2 = font_1.render("Choose your move",True,"white")
     screen.blit(text_2,(125,220))
     
    if (not still_game_state) and count_round<round:
        pygame.draw.rect(screen,('black'),Next_button)
        screen.blit(Next,(Next_button.x,Next_button.y))
        Comp_bot()
    
    if Final_state and count_round==round:
        pygame.draw.rect(screen,('black'),Retry_button)
        screen.blit(Retry,(Retry_button.x,Retry_button.y))
        
        pygame.draw.rect(screen,('black'),Exit_button)
        screen.blit(Exit,(Exit_button.x,Exit_button.y))
        
        if score_your>score_comp:
            won = font.render('You WON',True,'green')
            screen.blit(won,(140,100))
        elif score_your<score_comp:
            lost= font.render('You LOST',True,'red')
            screen.blit(lost,(140,100))
        else:
            tie = font.render("DRAW",True,'blue')
            screen.blit(tie,(160,100))
        
#all random inputs of computer
def Comp_bot():
     global result
     if comp_choice==1:screen.blit(Rock,(140,60))
     elif comp_choice==2:screen.blit(Paper,(140,60)) 
     elif comp_choice==3:screen.blit(Scissors,(140,60)) 
     
     if comp_choice==1 and choice==3 or comp_choice==3 and choice==2 or comp_choice==2 and choice==1:
         result=-1
     if choice==1 and comp_choice==3 or choice==3 and comp_choice==2 or choice==2 and comp_choice==1:
         result=1
     if choice==comp_choice:
         result=0

# main loop      
while run:
    
    screen.fill("black")#background color
    
    #all states fitted into loop
    if Menu_state:    
         Start_menu()
    if Rounds_state:
        Round_menu()
    if Game_state:
        Game()
        Score_u=font.render(f"{score_your}",True,'green')
        screen.blit(Score_u,(170,190))
        
        seprt=font.render(":",True,'white')
        screen.blit(seprt,(193,190))
        
        Score_comp=font.render(f"{score_comp}",True,'red')
        screen.blit(Score_comp,(210,190))
    
    #for loop responsible for all action taken by user  
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run= False
        #all mouse inputs are collected and processed accordingly
        if events.type == pygame.MOUSEBUTTONDOWN:
            if  Quit_button.collidepoint(events.pos)and Menu_state==True:
                run= False 
                
            if Start_button.collidepoint(events.pos)and Menu_state==True:
               Menu_state=False
               Rounds_state=True
               
            if Rock_button.collidepoint(events.pos) and Game_state==True and still_game_state==True:
                choice=1
                still_game_state=False
                comp_choice= random.randint(1,3)
            if Paper_button.collidepoint(events.pos) and Game_state==True and still_game_state==True:
                choice=2
                still_game_state=False
                comp_choice= random.randint(1,3)
            if Scissors_button.collidepoint(events.pos) and Game_state==True and still_game_state==True:
                choice=3
                still_game_state=False
                comp_choice= random.randint(1,3)
               
            if Round_button_1.collidepoint(events.pos) and Rounds_state==True:
                round=5
                Rounds_state=False
                Game_state=True
                still_game_state=True
                
            if Round_button_2.collidepoint(events.pos)and Rounds_state==True:
                round=10
                Rounds_state=False
                Game_state=True
                still_game_state=True
                
            if Round_button_3.collidepoint(events.pos)and Rounds_state==True:
                round=15
                Rounds_state=False
                Game_state=True
                still_game_state=True
                
            if Round_button_4.collidepoint(events.pos)and Rounds_state==True:
                round=20
                Rounds_state=False
                Game_state=True
                still_game_state=True
                
            if Next_button.collidepoint(events.pos):
               if count_round<round:
                    count_round+=1
                    still_game_state=True
               if count_round==round:
                   Final_state=True
              
               if result==1:score_your+=1
               if result==-1:score_comp+=1
                    
            if Retry_button.collidepoint(events.pos) and Final_state==True:
                count_round=0
                still_game_state=True
                score_your=0
                score_comp=0
            
            if Exit_button.collidepoint(events.pos) and Final_state==True:
                Game_state=False
                still_game_state=True
                Final_state=False
                Menu_state=True
                count_round=1
     
    #updating screen after every single input
    pygame.display.update()

#end of application
pygame.quit()