import pygame
import math
import random
import time

pygame.init()

screen_width = 1200
screen_height = 1000
fps = 10000
timer = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chase")
x = 50
y = 50


class Player:
    def __init__(self, x_input, y_input, count_var, speed) -> None:
        self.x = x_input
        self.y = y_input
        self.count = count_var
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def up(self):
        self.y -= self.speed
        if self.y <= 0:
            self.y = screen_height
        self.rect.y = self.y

    def down(self):
        self.y += self.speed
        if self.y >= screen_height:
            self.y = 0
        self.rect.y = self.y

    def left(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = screen_width
        self.rect.x = self.x

    def right(self):
        self.x += self.speed
        if self.x >= screen_width:
            self.x = 0
        self.rect.x = self.x

    def score(self):
        if self.rect.colliderect(point):
            self.count += 1
            point.x = random.randrange(900)
            point.y = random.randrange(900)

    def slowdown(self):
        if self.count > 0:
            self.count -= 1


class Hunter:
    def __init__(self, x_input, y_input, speed, enabled) -> None:
        self.x = x_input
        self.y = y_input
        self.speed = speed
        self.enabled = enabled

    def pathfind(self, x1, y1, x2, y2):
        dx1 = x1 - self.x
        dy1 = y1 - self.y
        dx2 = x2 - self.x
        dy2 = y2 - self.y
        d1 = math.sqrt((dx1 ** 2) + (dy1 ** 2))
        d2 = math.sqrt((dx2 ** 2) + (dy2 ** 2))
        if d1 >= d2:
            angle = math.atan2(dx2, dy2)
        else:
            angle = math.atan2(dx1, dy1)
        inc_x = math.sin(angle)
        inc_y = math.cos(angle)
        self.x += inc_x * self.speed
        self.y += inc_y * self.speed


player1 = Player(250, 300, 0, 6)
player2 = Player(750, 300, 0, 6)
chaser1 = Hunter(50, 50, 1, False)
point = pygame.Rect((500, 500, 30, 30))
count = 0


class Button:
    def __init__(self, text, x_inp, y_inp, enabled, width, height) -> None:
        self.text = text
        self.x_pos = x_inp
        self.y_pos = y_inp
        self.width = width
        self.height = height
        self.enabled = enabled

    def draw(self):
        font = pygame.font.Font(None, 35)
        button_text = font.render(self.text, True, (255, 255, 255))
        button_rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        pygame.draw.rect(screen, (10, 10, 10), button_rect, 0, 5)
        pygame.draw.rect(screen, (255, 255, 255), button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))


multiplayer_button = Button("multiplayer mode", 10, 10, True, 215, 30)

run = True
while run:

    screen.fill((50, 50, 50))
    multiplayer_button.draw()
    player1_score_button = Button(f"Player 1 score: {str(player1.count)}", 10, 50, True, 215, 30)
    player1_score_button.draw()
    player2_score_button = Button(f"Player 2 score: {str(player2.count)}", 10, 90, True, 215, 30)
    player2_score_button.draw()
    timer.tick(fps)
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0, 255, 255), player1.rect)
    pygame.draw.rect(screen, (255, 165, 0), player2.rect)
    if player1.count + player2.count >= 5:
        chaser1.enabled = True
    pygame.draw.rect(screen, (0, 255, 0), point)
    if chaser1.enabled:
        pygame.draw.circle(screen, (255, 0, 0), (chaser1.x, chaser1.y), 10)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and key[pygame.K_LEFT]:
        player1.left()
        player2.left()
    elif key[pygame.K_a] and key[pygame.K_UP]:
        player1.left()
        player2.up()
    elif key[pygame.K_a] and key[pygame.K_RIGHT]:
        player1.left()
        player2.right()
    elif key[pygame.K_a] and key[pygame.K_DOWN]:
        player1.left()
        player2.down()
    elif key[pygame.K_s] and key[pygame.K_DOWN]:
        player1.down()
        player2.down()
    elif key[pygame.K_s] and key[pygame.K_UP]:
        player1.down()
        player2.up()
    elif key[pygame.K_s] and key[pygame.K_LEFT]:
        player1.down()
        player2.left()
    elif key[pygame.K_s] and key[pygame.K_RIGHT]:
        player1.down()
        player2.right()
    elif key[pygame.K_d] and key[pygame.K_DOWN]:
        player1.right()
        player2.down()
    elif key[pygame.K_d] and key[pygame.K_UP]:
        player1.right()
        player2.up()
    elif key[pygame.K_d] and key[pygame.K_RIGHT]:
        player1.right()
        player2.right()
    elif key[pygame.K_d] and key[pygame.K_LEFT]:
        player1.right()
        player2.left()
    elif key[pygame.K_w] and key[pygame.K_DOWN]:
        player1.up()
        player2.down()
    elif key[pygame.K_w] and key[pygame.K_UP]:
        player1.up()
        player2.up()
    elif key[pygame.K_w] and key[pygame.K_LEFT]:
        player1.up()
        player2.left()
    elif key[pygame.K_w] and key[pygame.K_RIGHT]:
        player1.up()
        player2.right()
    elif key[pygame.K_a]:
        player1.left()
    elif key[pygame.K_d]:
        player1.right()
    elif key[pygame.K_s]:
        player1.down()
    elif key[pygame.K_w]:
        player1.up()
    elif key[pygame.K_UP]:
        player2.up()
    elif key[pygame.K_DOWN]:
        player2.down()
    elif key[pygame.K_LEFT]:
        player2.left()
    elif key[pygame.K_RIGHT]:
        player2.right()
    elif key[pygame.K_SPACE]:
        run = False
    if chaser1.enabled:
        chaser1.pathfind(player1.x, player1.y, player2.x, player2.y)
    player1.score()
    player2.score()
    if chaser1.enabled:
        if round(chaser1.x) in range(player1.x - 1, player1.x + 1) and round(chaser1.y) in range(player1.y - 1, player1.y + 1):
            player1.slowdown()
        if round(chaser1.x) in range(player2.x - 1, player2.x + 1) and round(chaser1.y) in range(player2.y - 1, player2.y + 1):
            player2.slowdown()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
print(f"Player1 score: {str(player1.count)}")
print(f"Player2 score: {str(player2.count)}")
pygame.quit()
time.sleep(5)
