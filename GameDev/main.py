import pygame as pg
import math
import random

# Constant Variables
WHITE = (255, 255, 255)  # (r, g, b)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BRIGHT_BLUE = (46, 192, 255)
GREY = (140, 140, 140)
BROWN = (59, 33, 1)
DARK_GREEN = (1, 36, 2)
LIGHT_GREY = (203, 204, 200)
DARK_GREY = (29, 29, 29)
GOLD = (162, 136, 1)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FLAKE_SPEED = 1
FLAKE_RADIUS = 5
BULLET_RADIUS = 10

FPS = 60

PI = math.pi
start_screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pg.time.Clock()
"""game over screen"""
game_over_screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Functions
def draw_car(x, y):
    pg.draw.polygon(screen, YELLOW, ((x+(SCREEN_WIDTH/50), y+(SCREEN_HEIGHT/1.12)), (x+(SCREEN_WIDTH/(100/11)), y+(SCREEN_HEIGHT/1.12)), (x+(SCREEN_WIDTH/10), y+SCREEN_HEIGHT/(700/595)), (x+(SCREEN_WIDTH/(100/3)), y+SCREEN_HEIGHT/(700/595))))
    pg.draw.rect(screen, YELLOW, [x, y+(SCREEN_HEIGHT/1.12), (SCREEN_WIDTH/(100/13)), (SCREEN_HEIGHT/17.5)])
    pg.draw.circle(screen, BLACK, (x+(SCREEN_WIDTH/40), y+(SCREEN_HEIGHT/(700/665))), SCREEN_WIDTH/(1000/15))
    pg.draw.circle(screen, BLACK, (x+(SCREEN_WIDTH/(1000/105)), y+(SCREEN_HEIGHT/(700/665))), SCREEN_WIDTH/(1000/15))

def draw_cloud(x, y):
    pg.draw.ellipse(screen, LIGHT_GREY, [x, y, 70, 50])
    pg.draw.ellipse(screen, LIGHT_GREY, [x+40, y, 70, 50])
    pg.draw.ellipse(screen, LIGHT_GREY, [x+15, y-25, 70, 50])

def draw_falling_objs(x, y, x2, y2):
    pg.draw.circle(screen, BLACK, (x, y), 40)
    pg.draw.rect(screen, BLACK, [x2, y2, 80, 80])


def draw_gun(x, y):
    pg.draw.circle(screen, GOLD, [x, y], BULLET_RADIUS)
    


def game_over(score, high_score, falling_objs_speed, falling_objs2_speed):
    font = pg.font.SysFont('Times New Roman', 50, True, True)
    score_text = font.render(f"Your score was {score}", True, WHITE)
    objs_end_speed = font.render(f"Falling Objects Speed: {falling_objs_speed} & {falling_objs2_speed}", True, WHITE)
    h_score = font.render(f"High Score: {high_score}", True, WHITE)
    game_over_screen.fill(BLACK)
    game_over_screen.blit(score_text, (40, 200))
    game_over_screen.blit(h_score, (40, 300))
    game_over_screen.blit(objs_end_speed, (40, 400))

def game_play():
    # Game set up
    pg.init()

    

    playing = True

    flakes = []
    # Create Lists
    for i in range(50):
        loc = [random.randint(0, SCREEN_WIDTH), 
            random.randint(0, SCREEN_HEIGHT)]
        flakes.append(loc)

    cloud_x = 0
    cloud_speed = 1
    car_x = (SCREEN_WIDTH/(-10))
    falling_objs_y = -50
    falling_objs_x = random.randrange(SCREEN_WIDTH)
    falling_objs_y2 = -50
    falling_objs_x2 = random.randrange(SCREEN_WIDTH)
    falling_objs_speed = 10
    falling_objs2_speed = 15
    end = False

    score = 0
    high_score = 0

    # speed and initial location for car
    x_speed = 0
    # y_speed = 0

    x_loc = 100
    y_loc = 0

    bullet_xloc = None
    bullet_yloc = None
    bullet_speed = 0
    bullets = []

    pg.mouse.set_visible(False)
        


    # Main game loop
    while playing:

        # the event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_speed = -21
                elif event.key == pg.K_RIGHT:
                    x_speed = 21
                if event.key == pg.K_SPACE:
                    bullet_speed = -25
                    bullet_xloc = x_loc+60
                    bullet_yloc = 600
                    bullets.append([bullet_xloc, bullet_yloc])

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_speed = 0

        mouse_pos = pg.mouse.get_pos()

        x_loc += x_speed

        if x_loc <= 0:
            x_loc = 0
        elif x_loc >= SCREEN_WIDTH-(SCREEN_WIDTH/(100/13)):
            x_loc = SCREEN_WIDTH-(SCREEN_WIDTH/(100/13))

        # game logic


        # clear the screen
        screen.fill(BRIGHT_BLUE)


        # Draw code should go here
        pg.draw.rect(screen, GREY, [0, SCREEN_HEIGHT-((1/4)*SCREEN_HEIGHT), SCREEN_WIDTH, SCREEN_HEIGHT-((2/4)*SCREEN_HEIGHT)])
        lines_x = 0
        while lines_x <= SCREEN_WIDTH:
            pg.draw.line(screen, YELLOW, (lines_x, SCREEN_HEIGHT-((1/8)*SCREEN_HEIGHT)), ((lines_x+40), SCREEN_HEIGHT-((1/8)*SCREEN_HEIGHT)), width=4)
            lines_x += SCREEN_WIDTH/20
        pg.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT-((5/8)*SCREEN_HEIGHT), SCREEN_WIDTH, SCREEN_HEIGHT-((319/512)*SCREEN_HEIGHT)])
        house_x = SCREEN_WIDTH/25
        while house_x <= SCREEN_WIDTH:
            pg.draw.rect(screen, RED, [house_x, SCREEN_HEIGHT - ((1/2)*SCREEN_HEIGHT), SCREEN_WIDTH/8, SCREEN_HEIGHT/5])
            pg.draw.rect(screen, BLACK, [house_x + SCREEN_WIDTH/16, SCREEN_HEIGHT-((3/8)*SCREEN_HEIGHT), SCREEN_WIDTH/40, SCREEN_HEIGHT/13])
            pg.draw.polygon(screen, BLACK, [(house_x, SCREEN_HEIGHT - ((1/2)*SCREEN_HEIGHT)), (house_x + SCREEN_WIDTH/8, SCREEN_HEIGHT - ((1/2)*SCREEN_HEIGHT)), (house_x + SCREEN_WIDTH/16, SCREEN_HEIGHT - ((3/5)*SCREEN_HEIGHT)), (house_x, SCREEN_HEIGHT - ((1/2)*SCREEN_HEIGHT))])
            pg.draw.polygon(screen, GREY, [(house_x, SCREEN_HEIGHT - ((77/256)*SCREEN_HEIGHT)), (house_x + SCREEN_WIDTH/16, SCREEN_HEIGHT - ((77/256)*SCREEN_HEIGHT)), (house_x + SCREEN_WIDTH/10, SCREEN_HEIGHT - ((1/4)*SCREEN_HEIGHT)), (house_x + SCREEN_WIDTH/32, SCREEN_HEIGHT - ((1/4)*SCREEN_HEIGHT))])
            pg.draw.rect(screen, BROWN, [house_x + SCREEN_WIDTH/(20/3), SCREEN_HEIGHT/(7/4), SCREEN_WIDTH/40, SCREEN_HEIGHT/7])
            pg.draw.polygon(screen, DARK_GREEN, [(house_x + SCREEN_WIDTH/(1000/127), SCREEN_HEIGHT/(28/17)), (house_x + SCREEN_WIDTH/(500/81), SCREEN_HEIGHT/(70/39)), (house_x + SCREEN_WIDTH/(1000/197), SCREEN_HEIGHT/(28/17))])
            pg.draw.polygon(screen, DARK_GREEN, [(house_x + SCREEN_WIDTH/(1000/127), SCREEN_HEIGHT/(70/41)), (house_x + SCREEN_WIDTH/(500/81), SCREEN_HEIGHT/(140/73)), (house_x + SCREEN_WIDTH/(1000/197), SCREEN_HEIGHT/(70/41))])
            pg.draw.polygon(screen, DARK_GREEN, [(house_x + SCREEN_WIDTH/(1000/127), SCREEN_HEIGHT/(70/39)), (house_x + SCREEN_WIDTH/(500/81), SCREEN_HEIGHT/2), (house_x + SCREEN_WIDTH/(1000/197), SCREEN_HEIGHT/(70/39))])
            house_x+=SCREEN_WIDTH/5

        
        if bullets:
            for bullet in bullets:
                bullet[1] += bullet_speed
                draw_gun(bullet[0], bullet[1])

            b_left_side = bullet[0]
            b_right_side = (bullet[0]+BULLET_RADIUS)

            if bullet[1] <= falling_objs_y+80 and b_right_side > (falling_objs_x-40) and b_right_side < (falling_objs_x + 40):
                falling_objs_y = 0
                falling_objs_x = random.randrange(SCREEN_WIDTH)
                bullet[1] = -50
                score += 1
            elif bullet[1] <= falling_objs_y and b_left_side > (falling_objs_x-40) and b_left_side < (falling_objs_x + 40):
                falling_objs_y = 0
                falling_objs_x = random.randrange(SCREEN_WIDTH)
                bullet[1] = -50
                score+=1

            elif bullet[1] <= falling_objs_y2+80 and b_right_side > falling_objs_x2 and b_right_side < (falling_objs_x2 + 80):
                falling_objs_y2 = 0
                falling_objs_x2 = random.randrange(SCREEN_WIDTH)
                bullet[1] = -50
                score+=1
            elif bullet[1] <= falling_objs_y2 and b_left_side > falling_objs_x2 and b_left_side < (falling_objs_x2 + 80):
                falling_objs_y2 = 0
                falling_objs_x2 = random.randrange(SCREEN_WIDTH)
                bullet[1] = -50
                score+=1
        draw_car(x_loc, y_loc)

        # car_x += 5
        # if car_x > SCREEN_WIDTH:
        #     car_x = SCREEN_WIDTH/(100/(-15))
        
        # draw_cloud(mouse_pos[0]-50, mouse_pos[1]-15)
        draw_cloud(cloud_x, 100)
        
        
        draw_falling_objs(falling_objs_x, falling_objs_y, falling_objs_x2, falling_objs_y2)
        
        
        if falling_objs_y <= SCREEN_HEIGHT:
            falling_objs_y += falling_objs_speed
        else:
            falling_objs_y = -50
            falling_objs_x = random.randrange(SCREEN_WIDTH)
            # score += 1
            # falling_objs_speed+=1
        
        if falling_objs_y2 <= SCREEN_HEIGHT:
            falling_objs_y2 += falling_objs2_speed
        else:
            falling_objs_y2 = -50
            falling_objs_x2 = random.randrange(SCREEN_WIDTH)
            # score += 1
            # falling_objs2_speed+=0.5
        
        

        if cloud_x == 0:
            cloud_speed = 1
        elif cloud_x == SCREEN_WIDTH:
            cloud_speed = -1
        cloud_x += cloud_speed
            

        for i in range(len(flakes)):
            pg.draw.circle(screen, WHITE, flakes[i], FLAKE_RADIUS)
            flakes[i][1] += FLAKE_SPEED

            if flakes[i][1] > SCREEN_HEIGHT:
                flakes[i] = [random.randint(0, SCREEN_WIDTH),
                            random.randint(-20, -6)]
        

        # falling_obj_1_r = 

        if (falling_objs_y + 60) >= (y_loc+(SCREEN_HEIGHT/1.12)) and (falling_objs_x-40) >= x_loc and (falling_objs_x-40) <= (x_loc + 130):
            # playing = False
            end = True
            if high_score < score:
                high_score = score
            # lives = lives - 1
        elif (falling_objs_y + 60) >= (y_loc+(SCREEN_HEIGHT/1.12)) and (falling_objs_x+40) >= x_loc and (falling_objs_x+40) <= (x_loc + 130):
            # playing = False
            end = True
            if high_score < score:
                high_score = score
            # lives = lives - 1
        if (falling_objs_y2 + 60) >= (y_loc+(SCREEN_HEIGHT/1.12)) and falling_objs_x2 >= x_loc and falling_objs_x2 <= (x_loc + 130):
            # playing = False
            end = True
            if high_score < score:
                high_score = score
            # lives = lives - 1
        elif (falling_objs_y2 + 60) >= (y_loc+(SCREEN_HEIGHT/1.12)) and (falling_objs_x2+80) >= x_loc and (falling_objs_x2+80) <= (x_loc + 130):
            # playing = False
            end = True
            if high_score < score:
                high_score = score
            # lives = lives - 1
        

        # print(lives)
        # if lives <= 0:
        #     end == True

        """game ends"""
        if end == True:
            game_over(score, high_score, falling_objs_speed, falling_objs2_speed)
            falling_objs_y = 0
            falling_objs_y2 = 0
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                end = False
                score = 0
                falling_objs_speed = 10
                falling_objs2_speed = 15
        elif event.type == pg.KEYUP:
            if event.key == pg.K_r:
                end = False
                score = 0
                falling_objs_speed = 10
                falling_objs2_speed = 15


        # update the screen with new drawings
        pg.display.flip()

        # limit to "FPS" frames per second
        clock.tick(FPS)

"""needs work"""
# def gamestart():
#     start_font = pg.font.SysFont('Times New Roman', 50, True, True)
#     start_txt = start_font.render("To Begin Game", True, BLACK)
#     start_txt_line_2 = start_font.render("Tap Spacebar", True, BLACK)

#     start_screen.fill(WHITE)
#     start_screen.blit(start_txt, (40, 200))
#     start_screen.blit(start_txt_line_2, (40, 250))

# gamestart()
game_play()


pg.quit()
