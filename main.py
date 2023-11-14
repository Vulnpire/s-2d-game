import pygame
from game import Game

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Desert Fighter")

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000

WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.75)

bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, YELLOW, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

def draw_winner_text(winner, font):
    winner_text = font.render("You lose!" if winner == 1 else "You win!", True, RED)
    screen.blit(winner_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))

def reset_game():
    global intro_count, round_over, round_over_time
    intro_count = 3
    round_over = False
    round_over_time = 0
    wizard.reset()
    warrior.reset()

def check_game_end():
    global score
    if score[0] == 3 or score[1] == 3:
        run = False
        winner = 1 if score[0] == 3 else 2
        draw_winner_text(winner, count_font)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

wizard = Game(1, 200, 310, False, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
warrior = Game(2, 700, 310, True, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
menu_run = True
while menu_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_run = False
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                play_with_friend = True
                menu_run = False
            elif event.key == pygame.K_2:
                play_with_friend = False
                menu_run = False

    screen.fill((0, 0, 0))
    draw_text("1: Play with Friend", count_font, RED, SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 50)
    draw_text("2: Play with AI", count_font, RED, SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 + 50)
    pygame.display.update()

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    draw_health_bar(wizard.health, 20, 20)
    draw_health_bar(warrior.health, 580, 20)

    if intro_count <= 0:
        wizard.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, warrior, round_over)
        if play_with_friend:
            warrior.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, wizard, round_over)
        else:
            warrior.ai_move(wizard, SCREEN_WIDTH, SCREEN_HEIGHT)
        wizard.update()
        warrior.update()
        wizard.draw(screen)
        warrior.draw(screen)

        if not wizard.alive or not warrior.alive:
            round_over = True
            round_over_time = pygame.time.get_ticks()
            winner = 1 if warrior.alive else 2
            score[winner - 1] += 1
            check_game_end()

    else:
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if pygame.time.get_ticks() - last_count_update >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

    pygame.display.update()

    if round_over:
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()