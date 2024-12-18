from settings import *
import components as comps
import pygame



def game_playing(lvl, current_lvl):
    new_lvl = False

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Game Title")

    clock = pygame.time.Clock()
    
    
    right_list = []
    left_list = []
    for i in range(1,12):
        img = f"platformer/images/player/walk000{i}.png"
        right = pygame.image.load(img)
        right = pygame.transform.scale(right, (PLAYER_WIDTH, PLAYER_HEIGHT))
        left = pygame.transform.flip(right, True, False)
        right_list.append(right)
        left_list.append(left)


    block_img = pygame.image.load('platformer/images/ground_rock.png')
    ground_image = pygame.image.load('platformer/images/ground_cave.png')
    enemy_img = pygame.image.load('platformer/images/slime_walk.png')
    door_img = pygame.image.load('platformer/images/lock_yellow.png')
    key_img = pygame.image.load('platformer/images/key_yellow.png')
    locked_door_img = pygame.image.load('platformer/images/lock_red.png')


    player_list = []
    enemy_list = []
    brick_list = []
    ground_list = []
    door_list = []
    e_barrier_list = []
    key_list = []
    locked_door_list = []


    for row in range(len(lvl)):
        y_loc = row * BRICK_HEIGHT

        for col in range(len(lvl[0])):
            x_loc = col * BRICK_WIDTH

            if lvl[row][col] == '1':
                brick = comps.Brick(screen, BLUE, x_loc, y_loc, 
                                    BRICK_WIDTH, BRICK_HEIGHT, block_img)
                brick_list.append(brick)

            elif lvl[row][col] == 'g':
                ground = comps.Ground(screen, BLUE, x_loc, y_loc, 
                                    BRICK_WIDTH, BRICK_HEIGHT, ground_image)
                ground_list.append(ground)

            elif lvl[row][col] == 'p':
                player = comps.Player(x_loc, y_loc + (BRICK_HEIGHT-PLAYER_HEIGHT), 
                                    PLAYER_WIDTH, PLAYER_HEIGHT,
                                    RED, screen, left_list, right_list)
                player_list.append(player)

            elif lvl[row][col] == 'e':
                enemy = comps.Enemy(screen, BLACK, x_loc, y_loc + (BRICK_HEIGHT-ENEMY_HEIGHT), 
                                    ENEMY_WIDTH, ENEMY_HEIGHT, enemy_img)
                enemy_list.append(enemy)

            elif lvl[row][col] == 'd':
                door = comps.Door(screen, GOLD, x_loc, y_loc + (BRICK_HEIGHT-DOOR_HEIGHT), 
                                    DOOR_WIDTH, DOOR_HEIGHT, door_img)
                door_list.append(door)

            elif lvl[row][col] == 'b':
                e_barrier = comps.Enemy_barrier(screen, x_loc, y_loc + (BRICK_HEIGHT-E_BARRIER_HEIGHT), 
                                    E_BARRIER_WIDTH, E_BARRIER_HEIGHT)
                e_barrier_list.append(e_barrier)

            elif lvl[row][col] == 'k':
                key = comps.Key(screen, x_loc, y_loc + (BRICK_HEIGHT-KEY_HEIGHT), 
                                    KEY_WIDTH, KEY_HEIGHT, key_img)
                key_list.append(key)

            elif lvl[row][col] == 'L':
                lock = comps.Key(screen, x_loc, y_loc + (BRICK_HEIGHT-LOCKED_DOOR_HEIGHT), 
                                    LOCKED_DOOR_WIDTH, LOCKED_DOOR_HEIGHT, locked_door_img)
                locked_door_list.append(lock)

            playing = True

    while playing:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing = False


        screen.fill(DARK_GREY)
        
            
        for door in door_list:
            door.draw()
            # door.update(player_list)

        for block in brick_list:
            block.draw_brick()

        for ground in ground_list:
            ground.draw()

        for enemy in enemy_list:
            enemy.draw_enemy()
            enemy.update(e_barrier_list, brick_list, ground_list)
        
        for player in player_list:
            player.update(brick_list, enemy_list, door_list, ground_list, locked_door_list, key_list)
            player.draw()

        if player.collided == True:
            playing = False
            return (current_lvl + 1)
        
        for key in key_list:
            key.draw()
            key.update(player_list)

        for lock in locked_door_list:
            lock.draw()

        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()
    
lvl = 1
layout = lvl-1

game_on = True
while lvl <= len(LEVELS):
    lvl = game_playing(LEVELS[layout], lvl)
    layout = lvl - 1
