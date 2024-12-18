import pygame
from settings import *


class Player():
    def __init__(self, x_loc, y_loc, width, height, color, display, left_list, right_list):
        self.right_list = right_list
        self.left_list = left_list

        self.run_right = False
        self.run_left = False

        self.current_frame = 0
        self.delay = 10
        self.last = pygame.time.get_ticks()
        
        self.img = self.right_list[0]
        self.rect = self.img.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

        
        self.x_start = x_loc
        self.y_start = y_loc

        self.display = display
        self.velo = 5
        self.x_velo = 8

        self.base_y = y_loc

        self.y_velo = 3
        self.jumping = False
        self.jump_height = height
        self.landed = True

        self.collided = False
        self.locked = True
    

        
    def draw(self):
        self.display.blit(self.img, self.rect)



    def update(self, surface_list, e_surface_list, d_surface_list, g_surface_list, L_door_surface_list, k_surfaces):
        x_change = 0
        y_change = 0

        # list of key presses
        keys = pygame.key.get_pressed()

        # set x_velo based on key presses
        if keys[pygame.K_LEFT]:
            self.now = pygame.time.get_ticks()

            x_change = -1 * self.x_velo
            self.run_left = True
            
            if (self.now - self.last) > self.delay:
                self.last = self.now
                self.current_frame = (self.current_frame + 1) % len(self.left_list)
                self.img = self.left_list[self.current_frame]
            

        elif keys[pygame.K_RIGHT]:
            self.now = pygame.time.get_ticks()
            
            x_change = self.x_velo
            self.run_right = True

            if (self.now - self.last) > self.delay:
                self.last = self.now
                self.current_frame = (self.current_frame + 1) % len(self.right_list)
                self.img = self.right_list[self.current_frame]

        else:
            x_change = 0

            if self.run_left:
                self.img = self.left_list[0]
                self.run_left = False
            elif self.run_right:
                self.img = self.right_list[0]
                self.run_right = False

        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            x_change = 0


        # jump on up or space key press
        if keys[pygame.K_UP] and not self.jumping and self.landed:
            self.jumping = True
            self.landed = False
            self.y_velo = -15
        if keys[pygame.K_SPACE] and not self.jumping and self.landed:
            self.jumping = True
            self.landed = False
            self.y_velo = -15
        if not keys[pygame.K_UP]:
            self.jumping = False
        if not keys[pygame.K_SPACE]:
            self.jumping = False


        # add gravity
        self.y_velo += GRAVITY
        if self.y_velo > 10:
            self.y_velo = 10        # set terminal velocity


        # update change in y
        y_change += self.y_velo


        # check collision
        for surface in surface_list:
            # horizontal collision
            if surface.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                x_change = 0

            # verticle collision
            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player going down
                if self.y_velo >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.landed = True
                    self.y_velo = 0
                # if player going up
                elif self.y_velo < 0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.y_velo = 0
        

        # check collision
        for surface in g_surface_list:
            # horizontal collision
            if surface.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                x_change = 0

            # verticle collision
            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player going down
                if self.y_velo >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.landed = True
                    self.y_velo = 0
                # if player going up
                elif self.y_velo < 0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.y_velo = 0
        

        # check enemy collision
        for enemy in e_surface_list:
            # horizontal collision
            if enemy.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                self.rect.y = self.y_start
                self.rect.x = self.x_start

            # verticle collision
            if enemy.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player going down
                if self.y_velo >= 0:
                    self.rect.y = self.y_start
                    self.rect.x = self.x_start
                # if player going up
                elif self.y_velo < 0:
                    self.rect.y = self.y_start
                    self.rect.x = self.x_start


        # check door collision
        for door in d_surface_list:
            # horizontal collision
            if door.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                self.collided = True

            # verticle collision
            elif door.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player going down
                if self.y_velo >= 0:
                    self.collided = True
                # if player going up
                elif self.y_velo < 0:
                    self.collided = True
            else:
                self.collided = False


        # check key collision
        for key in k_surfaces:
            # horizontal collision
            if self.locked == True:
                if key.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                    self.locked = False



        # check locked door collision
        for door in L_door_surface_list:
            # horizontal collision
            if self.locked == True:
                if door.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                    x_change = 0
        


        # update player location
        self.rect.x += x_change
        self.rect.y += y_change

        # if falling from platform, landed is false
        if y_change > 0:
            self.landed = False

        # return self.collided


class Brick:
    def __init__(self, display, color, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.display = display
        # self.color = color
        # self.width = width
        # self.height = height


    def draw_brick(self):
        self.display.blit(self.img, self.rect)

class Ground:
    def __init__(self, display, color, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.display = display
        # self.color = color
        # self.width = width
        # self.height = height


    def draw(self):
        self.display.blit(self.img, self.rect)


class Enemy_barrier():
    def __init__(self, display, x, y, width, height):
        self.display = display
        self.width = width
        self.height = height

        self.rect = pygame.Rect(x, y, self.width, self.height)

    # def draw(self):
    #      pygame.draw.rect(self.display, WHITE, self.rect)

        
class Enemy():
    def __init__(self, display, color, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.display = display
        self.color = color
        self.width = width
        self.height = height
        self.enemy_velo = -5
        self.start_x = x 
        self.x_change = self.enemy_velo
        


    def draw_enemy(self):
        self.display.blit(self.img, self.rect)
        

    def update(self, b_surfaces, w_surfaces, g_surfaces):
        # check barrier collision
        for barrier in b_surfaces:
            # horizontal collision
            if barrier.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                self.x_change = self.x_change * -1
            elif self.rect.x + E_BARRIER_WIDTH < 0:
                self.rect.x = DISPLAY_WIDTH + E_BARRIER_WIDTH
        for w in w_surfaces:
            # horizontal collision
            if w.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                self.x_change = self.x_change * -1
            elif self.rect.x + E_BARRIER_WIDTH < 0:
                self.rect.x = DISPLAY_WIDTH + BRICK_WIDTH
        for g in g_surfaces:
            # horizontal collision
            if g.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                self.x_change = self.x_change * -1
            elif self.rect.x + LOCKED_DOOR_WIDTH < 0:
                self.rect.x = DISPLAY_WIDTH + LOCKED_DOOR_WIDTH

        
        
        # update x_change
        self.rect.x += self.x_change
                
                
        

class Door():
    def __init__(self, display, color, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()

        self.display = display
        self.color = color
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        self.player_collide = False

    def draw(self):
        self.display.blit(self.img, self.rect)

    
class Key():
    def __init__(self, display, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()

        self.display = display
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        self.collected = False

    def draw(self):
        if self.collected == False:
            self.display.blit(self.img, self.rect)

    def update(self, p_surfaces):
        # check key collision
        for key in p_surfaces:
            # horizontal collision
            if key.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                self.collected = True

class Locked_door():
    def __init__(self, display, x, y, width, height, image):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()

        self.display = display
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        self.display.blit(self.img, self.rect)
