import random
import pygame
import sys
from math import ceil, log

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass

    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir
        pass

    def collision(self, x, y):
        head_x = self.get_head()[0]
        head_y = self.get_head()[1]
        if head_x > 23 or head_x < 0 or head_y > 23 or head_y < 0 or (head_x == x and head_y == y):
            return True
        else:
            return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        to_add = DIR.get(self.direction)
        if self.l + 1 != len(self.body):
            self.body.insert(0, tuple(map(sum, zip(self.body[0], to_add))))
        else:
            for i in range(self.l, 0, -1):
                self.body[i] = self.body[i - 1]
            self.body[0] = tuple(map(sum, zip(self.body[0], to_add)))
        for i in range(1, len(self.body)):
            if self.collision(self.body[i][0], self.body[i][1]):
                self.kill()

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)

    def wait_for_key(self):
        # Implementing feature #10
        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                break


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        self.position = (rand_int(WIDTH - 1), rand_int(HEIGHT - 1))
        i = 0
        while i <= len(snake) - 1:
            if snake[i] == self.position:
                self.position = (rand_int(WIDTH), rand_int(WIDTH))
                i = 0
            i += 1

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0

    thefont = pygame.font.SysFont("comic sans", 20)

    # Implementing feature #10
    snake.draw(surface)
    apple.draw(surface)
    screen.blit(surface, (0,0))
    screen.blit(thefont.render("Press any key to begin", 1, (10, 10, 10)), (160, 160))
    pygame.display.update()
    snake.wait_for_key()

    while True:
        # Implementing feature #9
        clock.tick(10 + ceil(2*log(snake.l)))
        snake.check_events()
        draw_grid(surface)
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        if snake.get_head() == apple.position:
            print("The snake ate an apple!")
            apple.place(snake.body)
            snake.l += 1
            score += 1
        screen.blit(surface, (0,0))
        screen.blit(thefont.render("Score: "+str(score), 1, (0, 0, 0)), (0, 0))

        pygame.display.update()
        if snake.dead:
            print(f'You died. Score: {score}')
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()
