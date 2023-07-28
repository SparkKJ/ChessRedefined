import pygame, sys, random
pygame.init()
width = 1300
height = 600
timer = pygame.time.Clock()
fps = 60 #frames change/time
font = pygame.font.SysFont('roboto',40)
middle_font = pygame.font.SysFont('roboto',30)
small_font = pygame.font.SysFont('roboto',25)
from pygame.locals import QUIT

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess Redefined')#name
size = 70,70 #for easy change during early stages
size_potion = 150,150
spell = 0
black_witch = pygame.image.load('assets/black_witch.png') #pieces iamge
black_witch = pygame.transform.scale(black_witch, (80, 80))
black_witch_small = pygame.transform.scale(black_witch, (size))
black_king = pygame.image.load('assets/black_king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (size))
black_pawn = pygame.image.load('assets/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (size))
black_heir = pygame.image.load('assets/black_heir.png')
black_heir = pygame.transform.scale(black_heir, (80, 80))
black_heir_small = pygame.transform.scale(black_heir, (size))
black_switcher = pygame.image.load('assets/black_switcher.png')
black_switcher = pygame.transform.scale(black_switcher, (80, 80))
black_switcher_small = pygame.transform.scale(black_switcher, (size))
black_spawner = pygame.image.load('assets/black_spawner.png')
black_spawner = pygame.transform.scale(black_spawner, (80, 80))
black_spawner_small = pygame.transform.scale(black_spawner, (size))
black_spellcaster = pygame.image.load('assets/black_spell_caster.png')
black_spellcaster = pygame.transform.scale(black_spellcaster, (80, 80))
black_spellcaster_small = pygame.transform.scale(black_spellcaster, (size))
black_airstriker = pygame.image.load('assets/black_air_striker.png')
black_airstriker = pygame.transform.scale(black_airstriker, (80, 80))
black_airstriker_small = pygame.transform.scale(black_airstriker, (size))

white_witch = pygame.image.load('assets/white_witch.png')
white_witch = pygame.transform.scale(white_witch, (80, 80))
white_witch_small = pygame.transform.scale(white_witch, (size))
white_king = pygame.image.load('assets/white_king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (size))
white_pawn = pygame.image.load('assets/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (size))
white_heir = pygame.image.load('assets/white_heir.png')
white_heir = pygame.transform.scale(white_heir, (80, 80))
white_heir_small = pygame.transform.scale(white_heir, (size))
white_switcher = pygame.image.load('assets/white_switcher.png')
white_switcher = pygame.transform.scale(white_switcher, (80, 80))
white_switcher_small = pygame.transform.scale(white_switcher, (size))
white_spawner = pygame.image.load('assets/white_spawner.png')
white_spawner = pygame.transform.scale(white_spawner, (80, 80))
white_spawner_small = pygame.transform.scale(white_spawner, (size))
white_spellcaster = pygame.image.load('assets/white_spell_caster.png')
white_spellcaster = pygame.transform.scale(white_spellcaster, (80, 80))
white_spellcaster_small = pygame.transform.scale(white_spellcaster, (size))
white_airstriker = pygame.image.load('assets/white_air_striker.png')
white_airstriker = pygame.transform.scale(white_airstriker, (80, 80))
white_airstriker_small = pygame.transform.scale(white_airstriker, (size))

damage_potion = pygame.image.load('assets/damage_potion.png') #spells image
damage_potion = pygame.transform.scale(damage_potion, (size_potion))
death_potion = pygame.image.load('assets/death_potion.png')
death_potion = pygame.transform.scale(death_potion, (size_potion))
health_potion = pygame.image.load('assets/health_potion.png')
health_potion = pygame.transform.scale(health_potion, (size_potion))
invincibility_potion = pygame.image.load('assets/invincibility_potion.png')
invincibility_potion = pygame.transform.scale(invincibility_potion, (size_potion))
heart = pygame.image.load('assets/heart.png')
heart = pygame.transform.scale(heart, (80,80))
golden_heart = pygame.image.load('assets/golden_heart.png')
golden_heart = pygame.transform.scale(golden_heart, (80,80))
spells_image = [damage_potion,death_potion,health_potion,invincibility_potion]
spells_list = ['damage_potion','death_potion','health_potion','invincibility_potion']
spells_white = ['damage_potion','death_potion','health_potion','invincibility_potion']
spells_black = ['damage_potion','death_potion','health_potion','invincibility_potion']

white_pieces = ['switcher','airstriker','spellcaster','witch','king','spawner','airstriker','switcher','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]#location
black_pieces = ['switcher','airstriker','spellcaster','witch','king','spawner','airstriker','switcher','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]#location
white_image = [white_switcher,white_airstriker,white_spellcaster,white_king,white_witch,white_spawner,white_pawn]
black_image = [black_switcher,black_airstriker,black_spellcaster,black_king,black_witch,black_spawner,black_pawn]
white_image_small = [white_switcher_small,white_airstriker_small,white_spellcaster_small,white_king_small,white_witch_small,white_spawner_small,white_pawn_small]
black_image_small = [black_switcher_small,black_airstriker_small,black_spellcaster_small,black_king_small,black_witch_small,black_spawner_small,black_pawn_small]

white_captured_pieces = []
black_captured_pieces = []

piece_list = ['switcher','airstriker','spellcaster','king','witch','spawner','pawn']
turn = 0#0 is not selected , 1 is selected while below 2,it is white turn,3 and 4 works similarly for black
selection = 100#selected piece
valid_moves = []#movement
sniper_location = []#shooting
sniper_damage_white = 1#base damage
sniper_damage_black = 1
switch = 0#for many variable if 0,1,2 is used 0 stands for not active,1 is active,2 is used and therefore cant use again
snipe = 0
status = ['White to move','Black to move','Draw','Checkmate:White Wins','Checkmate:Black Wins']
winner = ''
radius1 = [1,0,-1]#airstriker's one square radius attack calculation
game_over = False
spell_locate = 100#like selection
death_piece = 100#like selection
invincibile_white = False#inv spell not used for white
invincibile_black = False#inv ... for black
death_piece_white = 100#like selection
death_piece_black = 100
count_white = 0#turn calculation for invincibile
count_black = 0
white_piece_health = [5,4,3,5,8,3,4,5,2,2,2,2,2,2,2,2]#[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] test
black_piece_health = [5,4,3,5,8,3,4,5,2,2,2,2,2,2,2,2]#[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] test

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(display, 'light grey',
                             [660 - (column * 150), row * 75, 75, 75])
        else:
            pygame.draw.rect(display, 'light grey',
                             [735 - (column * 150), row * 75, 75, 75])
        pygame.draw.rect(display,'grey',[0,0,208,height])# the boxes
        pygame.draw.rect(display,'gold',[0,0,210,600],5)
        pygame.draw.rect(display,'gold',[0,0,210,65],5)
        pygame.draw.rect(display,'brown',[210,0,600,600],2)
display.blit(font.render(status[turn],True,'black'),(20,20))#whose turn

def draw_pieces():#draw pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            display.blit(white_pawn, (white_locations[i][0] * 75 + 20 +185, white_locations[i][1] * 75 - 25))
        else:
            display.blit(white_image[index], (white_locations[i][0] * 75 + 15 + 190, white_locations[i][1] * 75 - 25))
        if turn < 2:
            if selection == i:
              if switch == 1 or snipe == 1:#special ability is highlighted by purple selection
                    color = 'purple'
              else:
                    color = 'red'#else normal is red for white and blue for black
              pygame.draw.rect(display, color, [white_locations[i][0] * 75 + 210, white_locations[i][1] * 75 ,
                                                 75, 75], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            display.blit(black_pawn, (black_locations[i][0] * 75 + 20 + 185, black_locations[i][1] * 75 - 25))
        else:
            display.blit(black_image[index], (black_locations[i][0] * 75 + 15 + 190, black_locations[i][1] * 75 - 25))
        if turn >= 2:
            if selection == i:
              if switch == 1 or snipe == 1:
                    color = 'purple'
              else:
                    color = 'blue'
              pygame.draw.rect(display, color , [black_locations[i][0] * 75 + 210, black_locations[i][1] * 75 ,
                                                  75, 75], 2)

def draw_spells():#draw spells
  if turn < 2:
    if 'spellcaster' in white_pieces:#only when spellcaster alive
      for i in range(len(spells_white)):
        display.blit(spells_image[spells_list.index(spells_white[i])], (i * 100 + 800 , 200))
  else:
    if 'spellcaster' in black_pieces:
      for i in range(len(spells_black)):
        display.blit(spells_image[spells_list.index(spells_black[i])], (i * 100 + 800 , 200))
    
def check_pawn(position, color):#for the rest if there is a check it is validating the moves and attacks 
    moves_list = []
    if color == 'black':
        if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_spellcaster_and_spawner(position, color):#moves and attack
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                  
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_switcher(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) in friends_list:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_witch(position, color):#combine the move and attack of the two pieces
    moves_list = check_spellcaster_and_spawner(position, color)
    second_list = check_switcher(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = black_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_airstriker(position, color):#similar to switcher
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
          if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and (position[0] + (chain * x), position[1] + (chain * y)) not in enemies_list:
              moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
          chain += 1
    return moves_list

def piece_remove_white():#remove black piece
  if black_piece_health[black_piece]<1:
                        global invincibile_piece_black#error if it does have this
                        if invincibile_black:
                          global invincibile_piece_black#double the protection
                          if black_piece < invincibile_piece_black:
                            invincibile_piece_black -= 1
                        black_piece_health.pop(black_piece)   
                        if snipe != 1:#king not in snipe mode
                           white_locations[selection] = click_coords
                        else:#king not move after kill in snipe mode
                          global sniper_damage_white
                          sniper_damage_white += 1 #increase base damage
                        if black_pieces[black_piece] == 'witch':#witch death damage
                          white_piece = selection
                          white_piece_health[white_piece] -= 3
                          black_piece_health[random.randint(0,len(black_piece_health)-1)] += 3#transfer health to friendly
                          if white_piece_health[white_piece]<1:
                            if white_pieces[white_piece] == 'king':#gameover
                               winner = 'Black'
                            black_captured_pieces.append(white_pieces[white_piece])# captured at the side
                            white_pieces.pop(white_piece)#no more 
                            white_locations.pop(white_piece)#same
                            white_piece_health.pop(white_piece)#also
                            
                        white_captured_pieces.append(black_pieces[black_piece])#captured
                        black_pieces.pop(black_piece)#remove piece
                        black_locations.pop(black_piece)#remove
                                     

def piece_remove_black():#same thing but different colour
  if white_piece_health[white_piece]<1:
                        global invincibile_piece_health_white
                        if invincibile_white:
                          global invincibile_piece_white 
                          if white_piece < invincibile_piece_white:
                            invincibile_piece_white -= 1
                        white_piece_health.pop(white_piece)
                        if snipe != 1:
                           black_locations[selection] = click_coords
                        else:
                          global sniper_damage_black
                          sniper_damage_black += 1
                        if white_pieces[white_piece] == 'witch':
                          black_piece = selection
                          black_piece_health[black_piece] -= 3
                          white_piece_health[random.randint(0,len(white_piece_health)-1)] += 3
                          if black_piece_health[black_piece]<1:
                            if black_pieces[black_piece] == 'king':
                               winner = 'White'
                            white_captured_pieces.append(black_pieces[black_piece])
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                            black_piece_health.pop(black_piece)
                            
                        black_captured_pieces.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        
                        
def check_options(pieces, locations, turn):#all options
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'switcher':
            moves_list = check_switcher(location, turn)
        elif piece == 'spawner' or piece == 'spellcaster':
            moves_list = check_spellcaster_and_spawner(location, turn)
        elif piece == 'witch':
            moves_list = check_witch(location, turn)
        elif piece == 'king':
              moves_list = check_king(location, turn)
        elif piece == 'airstriker':
            moves_list = check_airstriker(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list
  
def check_valid_moves(): #specific piece selection
    if turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves,attack):#the grey dots as move,blue or red dots to attack 
  if switch == 1:
    if turn <= 1 and (((white_locations[selection])[0])%2==0 and ((white_locations[selection])[-1])%2==0) or (((white_locations[selection])[-1])%2!=0 and ((white_locations[selection])[0])%2!=0):#lost my sanity differentiating white and black squares
      move = switch_list
      
    elif turn > 1 and (((black_locations[selection])[0])%2!=0 and ((black_locations[selection])[-1])%2==0) or (((black_locations[selection])[-1])%2!=0 and ((black_locations[selection])[0])%2==0):#used to be combined with the top one but had to split in case readability penalise
      move = switch_list
    else:
      move = attack
    for i in range(len(move)):#use a colour not red or blue so brown but looks like red
           pygame.draw.circle(display, 'brown', (move[i][0] * 75 + 210 + 37.5, move[i][1] * 75 + 37.5), 5)
  elif snipe == 1:
    for i in range(len(sniper_location)):
            pygame.draw.circle(display, 'brown', (sniper_location[i][0] * 75 + 210 + 37.5, sniper_location[i][1] * 75 + 37.5), 5)
  else:#if no special ability activated then as normal
    if turn < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(attack)):
        pygame.draw.circle(display, color, (attack[i][0] * 75 + 210 + 37.5, attack[i][1] * 75 + 37.5), 5)
    if snipe == 0:#not active
      for i in range(len(moves)):
        pygame.draw.circle(display, 'grey', (moves[i][0] * 75 + 210 + 37.5, moves[i][1] * 75 + 37.5), 5)
  
def draw_captured():#quite obvious
    for i in range(len(white_captured_pieces)):
        captured_piece = white_captured_pieces[i]
        index = piece_list.index(captured_piece)
        display.blit(black_image_small[index], (825 + 25 * i, 5))
    for i in range(len(black_captured_pieces)):
        captured_piece = black_captured_pieces[i]
        index = piece_list.index(captured_piece)
        display.blit(white_image_small[index], (825 + 25 * i, 100))

def draw_game_over():#also obvious
    pygame.draw.rect(display, 'black', [200, 200, 400, 70])
    display.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    display.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

black_options = check_options(black_pieces, black_locations, 'black')#move for black
white_options = check_options(white_pieces, white_locations, 'white')  #moves for white
run = True
while run:
    timer.tick(fps)#time
    display.fill('dark grey')#background
    draw_board()
    draw_pieces()
    draw_captured()
    draw_spells()
    attack = []
    moves = []
    switch_list = []
    health_x = (pygame.mouse.get_pos()[0]-208) // 75#for piece definition later on but in early stage for health only
    health_y = pygame.mouse.get_pos()[1] // 75#divide by 75 to get square,the top 208 is the box for definition
    health_locate = (health_x,health_y)
    if (health_locate in white_locations or health_locate in black_locations) and not game_over:#define piece
        if health_locate in white_locations:
            if invincibile_white and invincibile_piece_white == white_locations.index(health_locate):#if piece is invincible
              health = invincibile_piece_health_white#its default health became 100 for one turn so need use b4
              heart_kind = golden_heart#golden heart for better experience 
            else:
              health = white_piece_health[white_locations.index(health_locate)]
              heart_kind = heart
            piece_name = white_pieces[white_locations.index(health_locate)]
            display.blit(white_image[piece_list.index(piece_name)], (65, 120))#piece image
        else:#same thing but black
            if invincibile_black and invincibile_piece_black == black_locations.index(health_locate):
              health = invincibile_piece_health_black
              heart_kind = golden_heart
            else:
              health = black_piece_health[black_locations.index(health_locate)]
              heart_kind = heart
            piece_name = black_pieces[black_locations.index(health_locate)]
            display.blit(black_image[piece_list.index(piece_name)], (65, 120))
        for i in range(health):#draw hearts
          display.blit(heart_kind, (i*15-10, 60))
        if piece_name == 'pawn':#all the definition here and the commas so they all in box
          description = ['Once A Pawn Forever A Pawn.Or Maybe Not.They Can','Quite Literally Move Two Squares On Their First Move As','Long As The Square Is Empty.']
          ability = ['MOVE:Two Square','Forward On Its First','Turn And One Otherwise','ATTACK:Deals TWO','Damage To Enemy','Pieces Diagonally','Forward One Square','There Is No More','En Passant And','Promotion']
        elif piece_name == 'switcher':
          description = ['What If You Gave Rooks Wings...']
          ability = ['MOVE:Horizontally And','Vertically As Long As','Nothing Is In Its Path','ATTACK:Deals TWO','Damage To Enemy','Pieces In Its Path','SPECIAL ABILITY:Press','ENTER to Switch Places','With A Piece In Its Path','Corresponding To The','Colour Of Its Square']
        elif piece_name == 'spellcaster':
          description = ["The Bishop's Been Learning Magic At Hogwarts Since The",'Last Update.When Was That Anyway']
          ability = ['MOVE:Diagonally As','Long As Nothing Is In','Its Path','ATTACK:Deals TWO','Damage To Enemy','Pieces In Its Path','SPECIAL ABILITY:Cast','A Spell Per Turn To','Boost Pieces Or','Damage Enemy Pieces','Immune To Enemy','Spells']
        elif piece_name == 'spawner':
          description = ['No Time To Code.To Be Continued...']
          ability = ['MOVE:Diagonally As','Long As Nothing Is In','Its Path','ATTACK:Deals TWO','Damage To Enemy','Pieces In Its Path']
        elif piece_name == 'airstriker':
          description = ['There Are A Queen, Two Rooks, There Seems To Be','Something Missing Here']
          ability = ['MOVE:Horizontally And','Vertically Even If A','Piece Is In Its Path',"ATTACK:Its Does't?",'SPECIAL ABILITY:Deals','ONE Damage To Enemy','Pieces In a One Square','Radius Upon Landing','At A New Location']
        elif piece_name == 'king':
          description = ["King Took A Trip To America.Now He's Back, With A Taste",'Of Freedom']
          ability = ['MOVES:One Square','Radius','ATTACK:Deals Two','Damage To Enemy','Pieces In Its Path','SPECIAL ABILITY:','Press ENTER To','Activate Sniper Mode:','Sniping Pieces At Least','3 Squares Diagonally,','Horizontally, Vertically','Dealing A Base Damage','Of One And One Extra','For Each Piece Killed In','Sniper Mode']
        elif piece_name == 'witch':
          description = ['The Queen Or Now The Witch, Learnt Some Dark Magic.','Taking Her Down Comes With A Hefty Cost']
          ability = ['MOVE:Diagonally,','Horizontally Or ','Vertically As Long As','Nothing Is In Its Path','ATTACK:Deals TWO','Damage To Enemy ','Pieces In Its Path','SPECIAL ABILITY:','Transfer 3 Hearts From','The Enemy Piece That','Killed It To A Random','Friendly Piece']
        piece_name = piece_name.title()#better if capitalise
        display.blit(small_font.render(f'{piece_name}:', True, 'black'), (8, 200))#name
        for i in range(len(ability)):#display all in box
          info = ability[i]
          display.blit(small_font.render(f'{info}', True, 'black'), (8, 230+ i*20))
        for i in range(len(description)):#background info on the other side
          describe = description[i]
          display.blit(small_font.render(f'{describe}', True, 'black'), (820, 400+ i*20))          
    if spell == 1:# spell, 0 unactive, 1 active, 2 black used,3 white used
            pygame.draw.rect(display,'gold',[spell_locate*100+825,200,100,150],3)#highlight selection
            if turn < 2:#whites turn
              if spells_white[spell_locate] == 'health_potion' or spells_white[spell_locate] == 'invincibility_potion':
                 if click_coords in white_locations:#buff own piece
                   if spells_white[spell_locate] == 'health_potion':
                     buff = 3
                   else:
                     buff = 100
                     invincibile_piece_white = white_locations.index(click_coords)
                     invincibile_piece_health_white = white_piece_health[white_locations.index(click_coords)]
                     invincibile_white = True
                   white_piece_health[white_locations.index(click_coords)] += buff#add health
                   spell = 3#white used its spell that turn
                   spells_white.pop(spell_locate)#remove spell
              elif spells_white[spell_locate] == 'damage_potion' or spells_white[spell_locate] == 'death_potion':
                 if click_coords in black_locations and black_pieces[black_locations.index(click_coords)] != 'spellcaster':#attack black
                   spell = 3#white used it spell that turn
                   black_piece_health[black_locations.index(click_coords)] -= 3
                   if spells_white[spell_locate] == 'death_potion':
                     black_piece_health[black_locations.index(click_coords)] += 1#death potion only minus 2 damage
                     death_piece_black = black_locations.index(click_coords)#mark it as ummovable piece,harder that expected since piece dying change it location in the list of pieces alive especially with airstriker being able to solo eight, one health piece
                     
                   spells_white.pop(spell_locate)#used
                   black_piece = black_locations.index(click_coords)#easier reference the selected enemy piece
                   if black_piece_health[black_piece]<1:#piece died
                        if black_pieces[black_piece] == 'king':# if king died then gg
                           winner = 'White'
                        white_captured_pieces.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_piece_health.pop(black_piece)
            else:#blacks turn same thing so I not annotate
              if spells_black[spell_locate] == 'health_potion' or spells_black[spell_locate] == 'invincibility_potion':
                 if click_coords in black_locations:
                   if spells_black[spell_locate] == 'health_potion':
                     buff = 3
                   else:
                     buff = 100
                     invincibile_piece_black = black_locations.index(click_coords)
                     invincibile_piece_health_black = black_piece_health[black_locations.index(click_coords)]
                     invincibile_black = True
                   black_piece_health[black_locations.index(click_coords)] += buff
                   spell = 2
                   spells_black.pop(spell_locate)
              elif spells_black[spell_locate] == 'damage_potion' or spells_black[spell_locate] == 'death_potion':
                  if click_coords in white_locations and white_pieces[white_locations.index(click_coords)] != 'spellcaster':
                     spell = 2
                     white_piece_health[white_locations.index(click_coords)] -= 3
                     if spells_black[spell_locate] == 'death_potion':
                        white_piece_health[white_locations.index(click_coords)] += 1
                        death_piece_white = white_locations.index(click_coords)
                        
                     spells_black.pop(spell_locate)
                     white_piece = white_locations.index(click_coords)
                     if white_piece_health[white_piece]<1:
                         if white_pieces[white_piece] == 'king':
                           winner = 'Black'
                         black_captured_pieces.append(white_pieces[white_piece])
                         white_pieces.pop(white_piece)
                         white_locations.pop(white_piece)
                         white_piece_health.pop(white_piece)
    if turn > 1:
      display.blit(font.render(f'Black To Move', True, 'black'), (8, 20))#no explanation needed
    else:
      display.blit(font.render(f'White To Move', True, 'black'), (8, 20))
    if selection != 100:#if not selection not in list range
        valid_moves = check_valid_moves()#moves
        for i in valid_moves:
          if (turn <= 1 and i in white_locations) or (turn > 1 and i in black_locations):#for switchers ability,own piece
             switch_list.append(i)
          elif i in black_locations or i in white_locations:
             attack.append(i)
          else:
             moves.append(i)
        draw_valid(moves,attack)
    if turn < 2:
        for i in range(len(spells_white)):
          if (i*100+825)<pygame.mouse.get_pos()[0]<(i*100+925) and 200<pygame.mouse.get_pos()[1]<350:#hover over the spell
            spell_name = spells_white[i]#spell is the one hovered
            display.blit(middle_font.render(f'{spell_name}', True, 'black'), (8, 100))#name
            display.blit(spells_image[spells_list.index(spell_name)], (30, 118))#image
            if spell_name == 'health_potion':
              description = ['Buff:','Increase The Health Of','One Of Your Piece By','Three']#definitions
            elif spell_name == 'damage_potion':
              description = ['Nerf:','Decrease The Health Of','One Of The Enemy','Piece By Three']
            elif spell_name == 'invincibility_potion':
              description = ['Buff:','Make One Of Your Piece','Invincible(Unable To Die)','For A Turn']
            else:
              description = ['Nerf:','Decrease The Health Of','One Of The Enemy','Piece By One And','Immoblise It For A Turn']
            for i in range(len(description)):#so in box
              describe = description[i]
              display.blit(small_font.render(f'{describe}', True, 'black'), (8, 280+ i*20))  
    for event in pygame.event.get():
        if event.type == QUIT:#dont quit support the game
            run = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN and selection != 100 and ((turn<2 and selection<=len(white_pieces))or(turn>1 and selection<=len(black_pieces))):#problems arrive without the turn and selection part
                if (white_pieces[selection] == 'switcher' and turn<2) or (black_pieces[selection] == 'switcher' and turn>1) and switch != 2:
                    if switch == 0:#activated switcher ability with return/enter and currently not activated
                       switch = 1#activate
                    else:
                       switch = 0#else if activated then unactivate
                elif (white_pieces[selection] == 'king' and turn<2) or (black_pieces[selection] == 'king' and turn>1):#activate sniper mode
                    if snipe == 0:#like switcher
                       snipe = 1
                    else:
                       snipe = 0
        if snipe == 1:#all 8 directions like witch
                  sniper_location = []
                  if turn < 2:
                    enemies_list = black_locations
                    friends_list = white_locations
                    position = white_locations[selection]
                  else:
                    friends_list = black_locations
                    enemies_list = white_locations
                    position = black_locations[selection]
                  for i in range(8):
                    path = True
                    chain = 1
                    if i == 0:
                       x = 0
                       y = 1
                    elif i == 1:
                       x = 0
                       y = -1
                    elif i == 2:
                       x = 1
                       y = 0
                    elif i == 3:
                       x = -1
                       y = 0
                    elif i == 4:
                        x = 1
                        y = -1
                    elif i == 5:
                        x = -1
                        y = -1
                    elif i == 6:
                        x = 1
                        y = 1
                    else:
                        x = -1
                        y = 1
                    while path:
                       if (position[0] + (chain * x), position[1] + (chain * y))  not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:#continue if no friendly piece obstruct
                          if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                            path = False#enemy obstruct
                            if chain > 3: #if squares not more than 3 than dont count as able to snipe
                             sniper_location.append((position[0] + (chain * x), position[1] + (chain * y)))
                          chain += 1#piece increment but restart when the direction been through
                       else:
                          path = False 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_spell = event.pos[0]#clicked
            y_spell = event.pos[1]
            x_coord = (x_spell-208) // 75
            y_coord = y_spell // 75
            click_coords = (x_coord, y_coord)
            if turn <= 1:#some parts use turn < 2 but same thing,whites turn
                
                for i in range(len(spells_white)):#if clicked spells
                   if (i*100+825)<x_spell<(i*100+925) and 200<y_spell<350 and spell != 3 and 'spellcaster' in white_pieces:
                      if spell_locate == i and spell == 1:# if spell active and not used change to deactive
                        spell = 0
                      else: #if deactive then active
                        spell = 1
                        spell_locate = i#which spell clicked
                if spell == 2:#if black used change to not used so white can use but the turn before black cant 
                  spell = 0
                if death_piece_white != 100:
                  if count_white == 2:#one turn past
                     death_piece_white = 100#no more immoblise piece
                     count_white = 0#0 turn
                  else:
                    count_white = 1#white turn past
                if count_black == 1:#if black turn past
                  count_black = 2#white turn then turn is up like above count_white == 2: which will make there no more immoblise piece
                if click_coords in white_locations and switch != 1 and snipe != 1:#selecting piece
                    selection = white_locations.index(click_coords)
                    if turn == 0:#havent select piece
                        turn = 1#selected piece
                if selection == death_piece_white:#if trying to move death piece then cant click
                   selection = 100
                if click_coords in moves and selection != 100 and switch != 1 and snipe != 1:#move
                    white_locations[selection] = click_coords#moving it to clicked location if nothing there
                    if white_pieces[selection] == 'airstriker':#only piece that does damage moving,vulnerable against death potion
                      for i in radius1:#the radius1 [0,1,-1] which i spent mental strength thinking of to not hardcode
                        for e in radius1:
                          if ((x_coord + i),(y_coord + e)) in black_locations:#if in one square then 
                            black_piece = black_locations.index(((x_coord + i),(y_coord + e)))#which black piece 
                            black_piece_health[black_piece] -= 1#minus one health
                            piece_remove_white()# if no more health then remove
                            if 'king' in white_captured_pieces:#gg
                             winner = 'White'
                    if invincibile_black:#after whites turn which is moving or attack or sniping then black piece no longer invincibile
                      invincibile_black = False
                      black_piece_health[invincibile_piece_black] = invincibile_piece_health_black#original health
                      
                    turn = 2#blacks turn
                    selection = 100#nothing selected
                    valid_moves = []#shift to blacks moves
                    switch = 0#no special abilities active
                    spell = 0
                if click_coords in attack and selection != 100 and switch != 1 and snipe != 1:# cant attack or move while special ability on
                    black_piece = black_locations.index(click_coords)#attacking enemy piece 
                    black_piece_health[black_piece] -= 2#minus health
                    piece_remove_white()#if no health then bye
                    if 'king' in white_captured_pieces:#gg
                          winner = 'White'
                    if invincibile_black:#same as moves
                      invincibile_black = False
                      black_piece_health[invincibile_piece_black] = invincibile_piece_health_black
                      
                    turn = 2#same as moves
                    selection = 100
                    valid_moves = []
                    switch = 0
                    spell = 0
                if switch == 1:
                    if turn <= 1: #if i werent the one who thought of this i would not know what this meant 
                      if (((white_locations[selection])[0])%2==0 and ((white_locations[selection])[-1])%2==0) or (((white_locations[selection])[0])%2!=0 and ((white_locations[selection])[-1])%2!=0):#square white
                        if click_coords in switch_list:
                          white_locations[white_locations.index(click_coords)] = white_locations[selection]#swap whites
                          white_locations[selection] = click_coords#switch
                      else: #square black
                        if click_coords in attack:
                          black_locations[black_locations.index(click_coords)] = white_locations[selection]#swap white with black
                          white_locations[selection] = click_coords
                      switch = 2
                    elif turn > 1:
                      if (((black_locations[selection])[0])%2!=0 and ((black_locations[selection])[-1])%2!=0) or (((black_locations[selection])[0])%2==0 and ((black_locations[selection])[-1])%2==0):#square black
                        if click_coords in switch_list:
                          black_locations[black_locations.index(click_coords)] = black_locations[selection]#swap blacks
                          black_locations[selection] = click_coords
                      else:#square white
                        if click_coords in attack:
                          white_locations[white_locations.index(click_coords)] = black_locations[selection]#swap black with white
                          black_locations[selection] = click_coords
                      switch = 2
                if snipe == 1:#annotated before in moves,attack...
                  if click_coords in sniper_location:
                      black_piece = black_locations.index(click_coords)
                      black_piece_health[black_piece] -= sniper_damage_white
                      piece_remove_white()
                      if 'king' in white_captured_pieces:
                           winner = 'White'
                      if invincibile_black:
                         invincibile_black = False
                         black_piece_health[invincibile_piece_black] = invincibile_piece_health_black
                         inv_piece_black = 0
                      snipe = 0
                      turn = 2
                      selection = 100
                      valid_moves = []
                      switch = 0         
                if 'king' in white_captured_pieces:
                          winner = 'White'
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white') 
                break    
            if turn > 1:#like white but black
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                for i in range(len(spells_black)):
                   if (i*100+825)<x_spell<(i*100+925) and 200<y_spell<350 and spell != 2 and 'spellcaster' in black_pieces:
                      if spell_locate == i and spell == 1:
                        spell = 0
                      else:
                        spell = 1
                        spell_locate = i
                if spell == 3:
                  spell = 0
                if death_piece_black != 100:
                  if count_black == 2:
                     death_piece_black = 100
                     count_black = 0
                  else:
                    count_black = 1
                if count_white == 1:
                  count_white = 2
                if click_coords in black_locations and switch != 1 and snipe != 1:
                    selection = black_locations.index(click_coords)
                    if turn == 2:
                        turn = 3
                if selection == death_piece_black:
                   selection = 100    
                if click_coords in moves and selection != 100 and switch != 1 and snipe != 1:
                    black_locations[selection] = click_coords
                    if black_pieces[selection] == 'airstriker':
                      for i in radius1:
                        for e in radius1:
                          if ((x_coord + i),(y_coord + e)) in white_locations:
                            white_piece = white_locations.index(((x_coord + i),(y_coord + e)))
                            white_piece_health[white_piece] -= 1
                            piece_remove_black()
                            if 'king' in black_captured_pieces:
                              winner = 'Black'
                    if invincibile_white:
                      invincibile_white = False
                      white_piece_health[invincibile_piece_white] = invincibile_piece_health_white
                      inv_piece_white = 0
                    turn = 0
                    selection = 100
                    valid_moves = []
                    switch = 0
                    spell = 0
                if click_coords in attack and selection != 100 and switch != 1 and snipe != 1:
                    white_piece = white_locations.index(click_coords)
                    white_piece_health[white_piece] -= 2
                    piece_remove_black()
                    if 'king' in black_captured_pieces:
                          winner = 'Black'
                    if invincibile_white:
                      invincibile_white = False
                      white_piece_health[invincibile_piece_white] = invincibile_piece_health_white
                    turn = 0
                    selection = 100
                    valid_moves = []
                    switch = 0
                    spell = 0
                if snipe == 1:
                  if click_coords in sniper_location:
                    white_piece = white_locations.index(click_coords)
                    white_piece_health[white_piece] -= sniper_damage_black
                    piece_remove_black()
                    if 'king' in black_captured_pieces:
                           winner = 'Black'
                    if invincibile_white:
                      invincibile_white = False
                      white_piece_health[invincibile_piece_white] = invincibile_piece_health_white
                      inv_piece_white = 0
                    snipe = 0
                    turn = 0
                    selection = 100
                    valid_moves = []
                    switch = 0
                if switch == 1:
                    if click_coords in switch_list:
                      black_locations[black_locations.index(click_coords)] = black_locations[selection]
                      black_locations[selection] = click_coords
                      switch = 2
                      
                    if click_coords in attack:
                      white_locations[white_locations.index(click_coords)] = black_locations[selection]
                      black_locations[selection] = click_coords
                      switch = 2
                if 'king' in black_captured_pieces:
                  winner = 'Black'
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                break
        if event.type == pygame.KEYDOWN and game_over:#gg
            if event.key == pygame.K_RETURN:#restart if return
                game_over = False#start
                winner = ''#no winner
                white_pieces = ['switcher','airstriker','spellcaster','witch','king','spawner','airstriker','switcher','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
                white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                black_pieces = ['switcher','airstriker','spellcaster','witch','king','spawner','airstriker','switcher','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
                black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                white_captured_pieces = []#restart everything
                black_captured_pieces = []
                white_piece_health = [5,4,3,5,8,3,4,5,2,2,2,2,2,2,2,2]
                black_piece_health = [5,4,3,5,8,3,4,5,2,2,2,2,2,2,2,2]
                spells_white = ['damage_potion','death_potion','health_potion','invincibility_potion']
                spells_black = ['damage_potion','death_potion','health_potion','invincibility_potion']
                sniper_damage_white = 0
                sniper_damage_black = 0
                turn = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
    if winner != '':#there is winner
        game_over = True
        draw_game_over()
    pygame.display.flip()
pygame.quit()#my history has 33061 edits,doing this for my game not wa3 anymore.I accept sponsors for my game.DO consider.