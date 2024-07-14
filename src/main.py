import pygame
import sys
from menu import show_menu
from battle import battle_scene
from store import store_scene
from credits import credits_scene
from options import options_scene

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dach - El RPG de Perros Salchichas")

# Funciones de escenas
def go_to_scene(scene):
    if scene == 'Batalla':
        battle_scene(screen)
    elif scene == 'Tienda':
        store_scene(screen)
    elif scene == 'Créditos':
        credits_scene(screen)
    elif scene == 'Opciones':
        options_scene(screen)

# Mostrar el menú principal
show_menu(screen, go_to_scene)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()