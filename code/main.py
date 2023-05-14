import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE, FPS, WATER_COLOR, BLACK
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('GAME PYTHON')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Timer
        self.timer_font = pygame.font.SysFont('Arial', 40)
        self.timer_value = 10  # Cambiar el valor inicial a 30 segundos
        self.timer_text = self.timer_font.render(str(self.timer_value), True, WHITE)
        self.timer_rect = self.timer_text.get_rect(center=(WIDTH // 2, 50))
        self.timer_running = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_x:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            if self.timer_running:
                self.update_timer()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            self.screen.blit(self.timer_text, self.timer_rect)
            pygame.display.update()
            self.clock.tick(FPS)
            

    def update_timer(self):
        if self.timer_value > 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.level.start_time >= 1000:
                self.level.start_time = current_time
                self.timer_value -= 1
                self.timer_text = self.timer_font.render(str(self.timer_value), True, WHITE)
        else:
            self.timer_running = False
            self.show_game_over()

    def show_game_over(self):
        game_over_font = pygame.font.SysFont('Comic Sans', 80)
        game_over_text = game_over_font.render("Game Over", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Wait for 3 seconds before restarting the game
        self.reset_game()

    def reset_game(self):
        self.level = Level()  # Crear una nueva instancia de Level
        self.timer_value = 10  # Restablecer el valor del temporizador a 30 segundos
        self.timer_text = self.timer_font.render(str(self.timer_value), True, WHITE)
        self.timer_running = True


if __name__ == '__main__':
    game = Game()
    game.run()
