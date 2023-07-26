import pygame, sys
from random import randint

pygame.init()

quantity = 5
selected_difficulty = 1

difficulty_square_position = []

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width + width * 2, screen_height + height * 2]
        self.mouse_state = pygame.mouse.get_pressed()[0]
        self.mouse_last_state = False
        self.selected_difficulty = 0

    def update(self):
        self.mouse_state = pygame.mouse.get_pressed()[0]

        if not self.mouse_state and self.mouse_last_state:
            self.rect.center = pygame.mouse.get_pos()
        self.mouse_last_state = self.mouse_state

    def collision(self):
        pygame.sprite.spritecollide(player, target_group, True)

        if pygame.sprite.spritecollide(player, difficulty_group, True):
            if player.rect == difficulty_group.lostsprites:
                print('here')

        return self.selected_difficulty

            
                    


class Target(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height

    def update(self, quantity):
        
        if len(target_group) <= 0:

            for targets in range(quantity):
                new_target = Target(self.width, self.height)
                new_target.rect.center = [randint(self.width / 2, screen_width - self.width / 2), randint(self.height / 2, screen_height - self.height / 2)]
                target_group.add(new_target)

class Difficulty(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.last_x_position = 0
        self.width = width
        self.height = height

    def selector(self):
        if len(difficulty_group) <= 0:

            for difficulty in range(3):
                self.last_x_position += screen_width / 4
                new_square = Difficulty(self.width, self.height)
                new_square.rect.center = [self.last_x_position, screen_height / 2]

                difficulty_square_position.append(new_square.rect)
                print(difficulty_square_position)

                difficulty_group.add(new_square)
                


def level_main():
    game_loop = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            sys.exit()

    player.update()
    player.collision()
    target.update(quantity)

    screen.fill(screen_color)
    target_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

    return game_loop

def intro():
    game_loop = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            sys.exit()

    screen.fill(screen_color)

    player.update()
    selected_difficulty = player.collision()
    difficulty.selector()

    difficulty_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()

    return game_loop, selected_difficulty

def level_manager():
    level = 'intro'

    if level == 'intro':
        game_loop, selected_difficulty = intro()

    if level == 'main_game':
        game_loop = level_main()
    
    return game_loop, selected_difficulty

screen_color = 'black'
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60

player = Player(30, 30)
player_group = pygame.sprite.Group()
player_group.add(player)

target = Target(50, 50)
target_group = pygame.sprite.Group()
game_loop = True

difficulty = Difficulty(50, 50)
difficulty_group = pygame.sprite.Group()

while game_loop:
    game_loop, selected_difficulty = level_manager()
    clock.tick(fps)