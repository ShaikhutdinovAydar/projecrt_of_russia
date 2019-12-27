import pygame
from board import Board

pygame.init()
clock = pygame.time.Clock()
size = width, height = 1050, 850
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))
fps = 10
# ...
# поле 5 на 7
board = Board(30, 30, screen)
board.set_view(100, 150, 20)
board.new_word()
running = True
drawing = True
c = 0
u = 0
while running:
    for event in pygame.event.get():
        k = board.get_move()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 274 and k != 1 and k != 2:
            board.m_down()
        if event.type == pygame.KEYDOWN and event.key == 273 and k != 2 and k != 1:
            board.m_up()
        if event.type == pygame.KEYDOWN and event.key == 276 and k != 4 and k != 3:
            board.m_left()
        if event.type == pygame.KEYDOWN and event.key == 275 and k != 3 and k != 4:
            board.m_right()
    if drawing:
        board.next_move()
    c += 1
    if c == fps:
        u += 1
        c = 0
    pygame.draw.rect(screen, (0, 0, 0), (920, 150, 50, 50))
    font = pygame.font.Font(None, 25)
    text = font.render(f"0{u // 60}:{u % 60}", 1, (255, 255, 255))
    text_x = 920
    text_y = 150
    screen.blit(text, (text_x, text_y))
    text = font.render(f"Вы собрали слово:", 1, (255, 255, 255))
    text_x = 750
    text_y = 200
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (920, 200, 50, 50))
    screen.blit(font.render(f"{str(board.ret_word())}", 1, (255, 255, 255)), (920, 200))

    board.render(screen)
    pygame.display.flip()
    clock.tick(fps)
# ...
pygame.quit()
