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
        self.player_health = 3
        self.enemy = enemyRocket(0, 0, "EnemyRocket.png")

    def textDarw(self, text, pos_x, pos_y, color, size):
        pygame.font.init()
        FONT = pygame.font.Font("Assets/Mono.ttf", size)
        text_surface = FONT.render(text, True, color)
        self.screen.blit(text_surface, [pos_x, pos_y])

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.pos_x = WIDTH/4
        self.pos_y = HEIGHT/2
        self.player = Player('Rocket.png', self.pos_x, self.pos_y)
        self.bullet = Bullet()
        self.all_sprites.add(self.player)
        self.platforms = pygame.sprite.Group()
        self.enemyRocket = pygame.sprite.Group()
        for plat in PLATFORMS_LIST:
            p = Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for enemy in ENEMY_LIST:
            self.e = enemyRocket(*enemy)
            self.all_sprites.add(self.e)
            self.enemyRocket.add(self.e)
        if self.player_health <= 0:
            self.player.kill()
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        collision = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if collision:
            self.player_health -= 1
            self.new()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    pygame.quit()
                    quit()
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                if event.key == pygame.K_SPACE:
                    self.bullet.rect.center = self.player.rect.center
                    self.all_sprites.add(self.bullet)
            if self.player_health <= 0:
                select = "Restart"
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                select = "Restart"
                            elif event.key == pygame.K_RIGHT:
                                select = "Menu"
                            if event.key == pygame.K_RETURN:
                                if select == "Restart":
                                    self.player_health = 3
                                    self.new()
                                if select == "Menu":
                                    self.show_start_screen()
                    if select == "Restart":
                        text_Restart = self.textDarw("Restart", 50, 300, RED, 30)
                    else:
                        text_Restart = self.textDarw("Restart", 50, 300, DARK_RED, 30)
                    if select == "Menu":
                        text_Menu = self.textDarw("Menu", 200, 300, RED, 30)
                    else:
                        text_Menu = self.textDarw("Menu", 200, 300, DARK_RED, 30)
                    pygame.display.flip()


    def draw(self):
        self.screen.fill(DARK_BLUE)
        self.all_sprites.draw(self.screen)
        self.textDarw(str(self.player_health), 20, 20, BLACK, 40)
        if self.player_health <= 0:
            self.textDarw("GameOver", WIDTH / 4, 150, BLACK, 50)
        
        pygame.display.flip()

    def show_start_screen(self):
        menu = True
        selected = "Start"

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "Start"
                    elif event.key == pygame.K_DOWN:
                        selected = "Quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "Start":
                            self.new()
                        if selected == "Quit":
                            pygame.quit()
                            quit()

            self.screen.fill(DARK_BLUE)
            if selected == "Start":
                text_start = self.textDarw("Start", (WIDTH / 3), (HEIGHT / 3), RED, 50)
            else:
                text_start = self.textDarw("Start", (WIDTH / 3), (HEIGHT / 3), DARK_RED, 50)
            if selected == "Quit":
                text_quit = self.textDarw("Quit", (WIDTH / 3), (HEIGHT / 2), RED, 50)
            else:
                text_quit = self.textDarw("Quit", (WIDTH / 3), (HEIGHT / 2), DARK_RED, 50)
            pygame.display.flip()


    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()

pygame.quit()