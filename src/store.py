import pygame

def store_scene(screen):
    font = pygame.font.Font(None, 74)
    text = font.render('Tienda', True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((34, 177, 76))
        screen.blit(text, text_rect)
        pygame.display.flip()