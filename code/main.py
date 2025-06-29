import pygame
from os.path import join
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 500

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))


# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing images from parent directory's images folder
# player_surf = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
# player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# player_direction = pygame.math.Vector2()
# player_speed = 300

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

meteor_surf = pygame.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('..', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # update
        all_sprites.update(dt)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)
        # if event.type == pygame.MOUSEMOTION:
        #    player_rect.center = event.pos

    # input
    # print(pygame.mouse.get_rel())
    # keys = pygame.key.get_pressed()
    # player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    # player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    # player_direction = player_direction.normalize() if player_direction else player_direction
    # player_rect.center += player_direction * player_speed * dt
    #
    # recent_keys = pygame.key.get_just_pressed()
    # if recent_keys[pygame.K_SPACE]:
    #     print('fire laser')

    # draw the game
    display_surface.fill('darkgray')
    all_sprites.draw(display_surface)
    pygame.display.update()
    # for pos in star_positions:
    #     display_surface.blit(star_surf, pos)
    #
    # display_surface.blit(meteor_surf, meteor_rect)
    # display_surface.blit(laser_surf, laser_rect)
    # display_surface.blit(player_surf, player_rect)

    # player movement
    # if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
    #     player_direction.y *= -1
    # if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
    #     player_direction.x *= -1
    # player_rect.center += player_direction * player_speed * dt
    # display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()
