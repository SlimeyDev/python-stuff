import pygame
import psutil
import colorsys

pygame.init()

font = pygame.font.SysFont('arial', 28)
logo = font.render('Currently Used Memory:', True, (0, 0, 0))

pygame_icon = pygame.image.load("LOGO.jpg")
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('Ram statistics')

width, height = 800, 800

DISPLAY = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()
run = True
cooldown = 0
remaining_ram = psutil.virtual_memory()[2] * 5
col_r = 0
col_g = 0
history = []
line_max_count = 1024
for i in range(line_max_count):
    history.append(0)


def draw():
    global cooldown, remaining_ram, col_r, col_g, history, line_max_count
    cooldown += 1
    if cooldown > 1:
        remaining_ram = psutil.virtual_memory()[2] * 5
        history.append(remaining_ram)
        cooldown = 0
        if len(history) > line_max_count:
            history.pop(0)
    i = 0
    for histitem in history:
        col_r = (histitem / 500) * 255 * 2
        col_r = 255 if col_r > 255 else col_r
        col_r = 0 if col_r < 0 else col_r
        col_g = (1 - (histitem / 500)) * 255 * 2
        col_g = 255 if col_g > 255 else col_g
        col_g = 0 if col_g < 0 else col_g
        pygame.draw.rect(DISPLAY, colorsys.hsv_to_rgb(colorsys.rgb_to_hsv(col_r, col_g, 0)[0], 0.2, colorsys.rgb_to_hsv(col_r, col_g, 0)[2]),
                         pygame.Rect(
            (800.0 / line_max_count) * i,
            800 - histitem,
            int(800.0 / line_max_count) + 1,
            3000
        ))
        pygame.draw.rect(DISPLAY, (col_r, col_g, 0),
                         pygame.Rect(
            (800.0 / line_max_count) * i,
            800 - histitem,
            int(800.0 / line_max_count) + 1,
            3
        ))
        i += 1
    pygame.draw.rect(DISPLAY, (col_r, col_g, 0),
                     pygame.Rect(0, 300, 2, 500))
    pygame.draw.rect(DISPLAY, (col_r, col_g, 0),
                     pygame.Rect(798, 300, 2, 500))
    pygame.draw.rect(DISPLAY, (col_r, col_g, 0),
                     pygame.Rect(0, 300, 800, 2))
    pygame.draw.rect(DISPLAY, (col_r, col_g, 0),
                     pygame.Rect(0, 798, 800, 2))


ram_draw_pixel_size = 10
ram_draw_position = (240, 100)
ram_draw_color_pallete = [
    (0, 0, 0),
    (106, 190, 48),
    (204, 194, 0),
]
ram_draw_font = pygame.font.SysFont('monospace', ram_draw_pixel_size * 5)
ram_draw_percent_sign = ram_draw_font.render('%', True, (255, 255, 255))


def draw_pixel(x, y, color):
    pygame.draw.rect(DISPLAY, ram_draw_color_pallete[color],
                     pygame.Rect(ram_draw_position[0] + (ram_draw_pixel_size * x), ram_draw_position[1] + (ram_draw_pixel_size * y), ram_draw_pixel_size, ram_draw_pixel_size))


def draw_ram():
    global remaining_ram, col_r, col_g
    for i in range(30):
        draw_pixel(i, 0, 0)
    for y in range(12):
        for i in range(28):
            if i / 28 < remaining_ram / 500:
                draw_pixel(i + 1, y + 1, 1)
    for i in range(7):
        draw_pixel(0, i, 0)
    for i in range(7):
        draw_pixel(29, i, 0)
    for i in range(6):
        draw_pixel(1, i + 6, 0)
    for i in range(3):
        draw_pixel(0, i + 11, 0)
    for i in range(30):
        draw_pixel(i, 13, 0)
    for i in range(5):
        draw_pixel(28, i + 6, 0)
    for i in range(3):
        draw_pixel(29, i + 10, 0)
    for y in range(7):
        for i in range(5):
            draw_pixel(i + 3, y + 3, 0)
    for y in range(7):
        for i in range(5):
            draw_pixel(i + 9, y + 3, 0)
    for y in range(7):
        for i in range(5):
            draw_pixel(i + 16, y + 3, 0)
    for y in range(7):
        for i in range(5):
            draw_pixel(i + 22, y + 3, 0)
    for x in range(6):
        for y in range(2):
            draw_pixel(x * 2 + 3, y + 11, 2)
    for x in range(6):
        for y in range(2):
            draw_pixel(x * 2 + 16, y + 11, 2)
    DISPLAY.blit(ram_draw_percent_sign, (ram_draw_position[0] + (ram_draw_pixel_size *
                 22) + 9, ram_draw_position[1] + (ram_draw_pixel_size * 3) + 5))
    ram_draw_num = ram_draw_font.render(
        str(int(remaining_ram / 5) % 10), True, (255, 255, 255))
    DISPLAY.blit(ram_draw_num, (ram_draw_position[0] + (ram_draw_pixel_size *
                 9) + 9, ram_draw_position[1] + (ram_draw_pixel_size * 3) + 5))
    ram_draw_num = ram_draw_font.render(
        str(int(remaining_ram / 50) % 10), True, (255, 255, 255))
    DISPLAY.blit(ram_draw_num, (ram_draw_position[0] + (ram_draw_pixel_size *
                 3) + 9, ram_draw_position[1] + (ram_draw_pixel_size * 3) + 5))
    ram_draw_num = ram_draw_font.render(
        str(int(remaining_ram / 0.5) % 10), True, (255, 255, 255))
    DISPLAY.blit(ram_draw_num, (ram_draw_position[0] + (ram_draw_pixel_size *
                 16) + 9, ram_draw_position[1] + (ram_draw_pixel_size * 3) + 5))
    ram_draw_num = ram_draw_font.render(
        '.', True, (255, 255, 255))
    DISPLAY.blit(ram_draw_num, (ram_draw_position[0] + (ram_draw_pixel_size *
                 15) + 1, ram_draw_position[1] + (ram_draw_pixel_size * 4) + 0))


while run:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    DISPLAY.fill("white")
    DISPLAY.blit(logo, (237, 20))
    draw()
    draw_ram()
    pygame.display.update()
pygame.quit()