import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размера окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Установка названия окна
pygame.display.set_caption('Название игры')

# Загрузка и растягивание изображения фона
# Замените 'back.jpg' на соответствующий путь к вашему файлу
background_image = pygame.image.load('back.jpg')
background_image = pygame.transform.scale(background_image, (width, height))  # Растягиваем изображение

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)   # Для выделения кнопок
BLACK = (0, 0, 0)    # Для стен

# Шрифты
font = pygame.font.SysFont('Arial', 48)

# Текст кнопок
title_text = font.render('Прятки', True, WHITE)
play_button_text = font.render('ИГРАТЬ', True, WHITE)
exit_button_text = font.render('ВЫХОД', True, WHITE)

# Позиции
title_pos = (width // 2 - title_text.get_width() // 2, 100)
play_button_pos = (width // 2 - play_button_text.get_width() // 2, 300)
exit_button_pos = (width // 2 - exit_button_text.get_width() // 2, 400)

# Прямоугольники для кнопок
play_button_rect = pygame.Rect(play_button_pos[0] - 10, play_button_pos[1] - 10, play_button_text.get_width() + 20, play_button_text.get_height() + 20)
exit_button_rect = pygame.Rect(exit_button_pos[0] - 10, exit_button_pos[1] - 10, exit_button_text.get_width() + 20, exit_button_text.get_height() + 20)

# Загрузка карты из файла map.txt
def load_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Рисование карты
def draw_map(screen, game_map):
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == '#':
                pygame.draw.rect(screen, BLACK, rect)
            elif tile == '*':
                pass  # Свободное пространство не требует отрисовки

# Константы для карты
TILE_SIZE = 40

# Загрузка карты
game_map = load_map('map.txt')

# Основной цикл игры
running = True
show_map = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                show_map = True

    screen.blit(background_image, (0, 0))

    if not show_map:
        # Отображение заголовка и кнопок
        screen.blit(title_text, title_pos)
        pygame.draw.rect(screen, BLUE, play_button_rect)
        screen.blit(play_button_text, play_button_pos)
        pygame.draw.rect(screen, RED, exit_button_rect)
        screen.blit(exit_button_text, exit_button_pos)
    else:
        # Рисуем карту
        draw_map(screen, game_map)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
