import pygame

pygame.init()

BG_COLOR = (0, 0, 0)
WIDTH, HEIGHT = 1000, 750
GAME_NAME = "FAE COFEA SHOPE"
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

def draw(window):
    pygame.display.update()

def main(window):
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        window.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(window)

    pygame.quit

if __name__ == "__main__":
    main(window)
