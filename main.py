import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def textDarw(self, text, pos_x, pos_y):
        pygame.font.init()
        FONT = pygame.font.Font("Assets/Mono.ttf", 36)
        text_surface = FONT.render(text, True, BLACK)
        self.screen.blit(text_surface, [pos_x, pos_y])

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.pos_x = WIDTH/2
        self.pos_y = HEIGHT/2
        self.player = Player('Rocket.png', self.pos_x, self.pos_y)
        self.player_healty = 3
        self.all_sprites.add(self.player)
        self.platforms = pygame.sprite.Group()
        self.enemyRocket = pygame.sprite.Group()
        for plat in PLATFORMS_LIST:
            p = Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for enemy in ENEMY_LIST:
            e = enemyRocket(*enemy)
            self.all_sprites.add(e)
            self.enemyRocket.add(e)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            collision = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if collision:
                self.player_healty -= 1
                self.new()


    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(DARK_BLUE)
        self.all_sprites.draw(self.screen)
        self.textDarw(str(self.player_healty), 20, 20)
        
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()

pygame.quit()