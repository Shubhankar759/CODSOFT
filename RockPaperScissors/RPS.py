import pygame

pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Rock Paper Scissors")

round=0

font = pygame.font.SysFont('Roboto',40,bold=True)
Quit = font.render('Quit',True,'white')
Start = font.render('Start',True,'white')
Round_1 = font.render('5 Rounds',True,'white')
Round_2 = font.render('10 Rounds',True,'white')
Round_3 = font.render('15 Rounds',True,'white')
Round_4 = font.render('20 Rounds',True,'white')

Rock = pygame.image.load('Rock.png')
Rock = pygame.transform.scale(Rock,(100,100))
Paper = pygame.image.load('Paper.png')
Paper = pygame.transform.scale(Paper,(100,100))
Scissors = pygame.image.load('Scissors.png')
Scissors = pygame.transform.scale(Scissors,(100,100))


Quit_button =  pygame.Rect(250,350,68,30)
Start_button = pygame.Rect(90,350,68,30)
Round_button_1 = pygame.Rect(135,150,130,30)
Round_button_2 = pygame.Rect(130,200,140,30)
Round_button_3 = pygame.Rect(130,250,140,30)
Round_button_4 = pygame.Rect(130,300,140,30)
Rock_button = pygame.Rect(130,300,200,200)


run =True
Menu_state=True
Rounds_state=False
Game_state=False

def Start_menu():
     pygame.draw.rect(screen,('black'),Quit_button)
     pygame.draw.rect(screen,('black'),Start_button)
    
    
     screen.blit(Quit, (Quit_button.x,Quit_button.y))
     screen.blit(Start,(Start_button.x,Start_button.y))

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
    screen.blit(Rock,(Rock_button.x,Rock_button.y))
   
 
while run:
    
    screen.fill("red")
    
    if Menu_state:    
         Start_menu()
    if Rounds_state:
        Round_menu()
    if Game_state:
        Game()
        
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run= False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if  Quit_button.collidepoint(events.pos):
                run= False 
                
            if Start_button.collidepoint(events.pos):
               Menu_state=False
               Rounds_state=True
               
            if Round_button_1.collidepoint(events.pos):
                round=5
                Rounds_state=False
                Game_state=True
                
            if Round_button_2.collidepoint(events.pos):
                round=10
                Rounds_state=False
                Game_state=True
                
            if Round_button_3.collidepoint(events.pos):
                round=15
                Rounds_state=False
                Game_state=True
                
            if Round_button_4.collidepoint(events.pos):
                round=20
                Rounds_state=False
                Game_state=True
          
    


    pygame.display.update()
   

pygame.quit()