import pygame

def show_menu(screen, change_scene):
    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fuente
    font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)

    # Títulos
    title_text = font.render('Dach - El RPG de Perros Salchichas', True, WHITE)
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4))

    # Botones
    button_texts = ['Batalla', 'Tienda', 'Créditos', 'Opciones']
    buttons = []
    for i, text in enumerate(button_texts):
        button_text = button_font.render(text, True, BLACK)
        button_rect = button_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + i * 70))
        buttons.append((button_text, button_rect))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, (button_text, button_rect) in enumerate(buttons):
                    if button_rect.collidepoint(mouse_pos):
                        if i == 0:
                            change_scene('Batalla')
                        elif i == 1:
                            change_scene('Tienda')
                        elif i == 2:
                            change_scene('Créditos')
                        elif i == 3:
                            change_scene('Opciones')

        # Dibujar en la pantalla
        screen.fill((34, 177, 76))  # Fondo verde
        screen.blit(title_text, title_rect)

        for button_text, button_rect in buttons:
            pygame.draw.rect(screen, WHITE, button_rect.inflate(20, 20))  # Dibujar el fondo del botón
            screen.blit(button_text, button_rect)

        pygame.display.flip()