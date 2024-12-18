import pygame as pg
import math

# Constant Variables
WHITE = (255, 255, 255)  # (r, g, b)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

FPS = 60

PI = math.pi



# Game set up
pg.init()

screen = pg.display.set_mode([600, 400])
clock = pg.time.Clock()

playing = True

# Functions
def rect(x1, y1, width, height, color):
        pg.draw.rect(screen, color, [x1, y1, width, height])

"""ex.4"""
# font = pg.font.SysFont('Times New Roman', 20, True, True)
    
# text = font.render('''"Once upon a midnight dreary, while I pondered, weak and weary,\nOver many a quaint and curious volume of forgotten lore—\n While I nodded, nearly napping, suddenly there came a tapping,\nAs of some one gently rapping, rapping at my chamber door.\n'’Tis some visitor,' I muttered, 'tapping at my chamber door—Only this and nothing more.'"\n-Edgar Allen Poe''', True, BLACK)
    
# Main game loop
while playing:

    # the event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    # game logic


    # clear the screen
    screen.fill(WHITE)

    # Draw code should go here

    # pg.draw.rect(screen, RED, [20, 20, 100, 50])
    # pg.draw.arc(screen, BLUE, [200, 200, 100, 100], PI/2, PI)
    # pg.draw.arc(screen, RED, [200, 200, 100, 100], 0, PI/2)
    # pg.draw.arc(screen, BLACK, [200, 200, 100, 100], PI, 3*PI/2)
    # pg.draw.arc(screen, GREEN, [200, 200, 100, 100], 3*PI/2, 2*PI)
    """ex.1"""
    # pg.draw.line(screen, BLACK, [40, 20], [300, 20])

    # pg.draw.line(screen, BLACK, [100, 100], [250, 100])
    # pg.draw.line(screen, BLACK, [100, 100], [175, 250])
    # pg.draw.line(screen, BLACK, [175, 250], [250, 100])

    # x = 450
    # y = 100
    # while y <= 275:
    #     y2 = y + 5
    #     pg.draw.line(screen, BLACK, [x, y], [x, y2])
    #     y += 10

    """ex.2(function further up under "Functions")"""
    # rect(20, 20, 150, 100, YELLOW)
    # rect(190, 20, 150, 100, ORANGE)
    # rect(360, 20, 150, 100, BLUE)

    """ex.3"""
    # pg.draw.circle(screen, GREEN, [100, 100], 50)
    # pg.draw.circle(screen, RED, [100, 100], 50, width = 2)

    # pg.draw.ellipse(screen, GREEN, [210, 50, 150, 100])
    # pg.draw.ellipse(screen, RED, [210, 50, 150, 100], width=2)

    # pg.draw.rect(screen, GREEN, [420, 30, 100, 75])
    # pg.draw.rect(screen, RED, [420, 30, 100, 75], width=2)

    # pg.draw.arc(screen, GREEN, [75, 200, 75, 100], 0, 5*PI/4, width=300)

    # pg.draw.polygon(screen, GREEN, [(300, 200), (350, 225), (400, 300), (365, 320), (300, 250), (250, 320)])
    # pg.draw.polygon(screen, RED, [(300, 200), (350, 225), (400, 300), (365, 320), (300, 250), (250, 320)], width=2)
    
    """ex.4"""
    
    # screen.blit(text, (20, 20))

    # update the screen with new drawings
    pg.display.flip()

    # limit to "FPS" frames per second
    clock.tick(FPS)

pg.quit()
