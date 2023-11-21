import pygame
import sys

#a executer : pip install pygame


# Initialisation de Pygame
pygame.init()

# Paramètres de base du jeu
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 5
ROBOT_SPEED = 4
WHITE = (255, 255, 255)
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Position initiale de la balle et des raquettes
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED
paddle_player = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_robot = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Fonction pour dessiner les éléments du jeu
def draw(ball_x, ball_y, paddle_player, paddle_robot):
    screen.fill((0, 0, 0))  # Écran noir
    pygame.draw.ellipse(screen, WHITE, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))
    pygame.draw.rect(screen, WHITE, paddle_player)
    pygame.draw.rect(screen, WHITE, paddle_robot)
    pygame.display.flip()

# Boucle principale du jeu
def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Déplacement du joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle_player.top > 0:
            paddle_player.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_player.bottom < HEIGHT:
            paddle_player.y += PADDLE_SPEED

        # Déplacement du robot
        if paddle_robot.centery < ball_y and paddle_robot.bottom < HEIGHT:
            paddle_robot.y += ROBOT_SPEED
        elif paddle_robot.centery > ball_y and paddle_robot.top > 0:
            paddle_robot.y -= ROBOT_SPEED

        # Déplacement de la balle
        ball_x += ball_dx
        ball_y += ball_dy

        # Rebondissement de la balle
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
            ball_dy = -ball_dy
        if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
            ball_dx = -ball_dx

        # Collision avec les raquettes
        if paddle_player.colliderect((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            ball_dx = -ball_dx
        if paddle_robot.colliderect((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            ball_dx = -ball_dx

        draw(ball_x, ball_y, paddle_player, paddle_robot)
        clock.tick(60)

# Lancement du jeu
game_loop()
