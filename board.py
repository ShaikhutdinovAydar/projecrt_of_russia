import random
import sqlite3

import pygame


class Board:
    # создание поля
    def __init__(self, width, height, screen):
        self.width = width
        self.screen = screen
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.move_ = 4
        self.health = 5
        y = random.randint(0, self.height - 1)
        x = random.randint(0, self.width - 1)
        self.main_list = [[y, x]]
        self.position_word = []
        self.len_word = 0
        self.word = 0
        self.less_word = ''
        self.counter = 0
        self.count_TRUE_word = 0
        self.cpunt_all_word = 0
        self.learn_list = []

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # def description(self, screen, r):
    #     con = sqlite3.connect("words.db")
    #     cur = con.cursor()
    #     description = cur.execute(f"SELECT word FROM main_words WHERE id = {r}").fetchone()
    #     description, = description
    #     font = pygame.font.Font(None, 25)
    #     text = font.render(f"{description}", 1, (255, 0, 0))
    #     text_x = 50
    #     text_y = 50
    #     screen.blit(text, (text_x, text_y))

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (
                        self.cell_size * i + self.left, self.cell_size * j + self.top, self.cell_size, self.cell_size))
                if self.board[j][i] == 1:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.cell_size * i + self.left, self.cell_size * j + self.top, self.cell_size,
                                      self.cell_size))
                elif str(self.board[j][i]) in "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
                    font = pygame.font.Font(None, 25)
                    text = font.render(f"{self.board[j][i]}", 1, (255, 0, 0))
                    text_x = self.cell_size * i + self.left + 5
                    text_y = self.cell_size * j + self.top
                    screen.blit(text, (text_x, text_y))
                # pygame.draw.rect(screen, (255, 255, 255), (self.cell_size * i + self.left, self.cell_size * j + self.top, self.cell_size, self.cell_size), 1)
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.left, self.top, self.width * self.cell_size, self.cell_size * self.height), 2)

    def move(self, x, y):
        self.move_ = x
        self.move_ = y

    def m_up(self):
        g = str(self.board[(self.main_list[0][0] - 1) % self.height][self.main_list[0][1] % self.width])
        if self.board[(self.main_list[0][0] - 1) % self.height][self.main_list[0][1] % self.width] == 1:
            self.lose()
        self.board[(self.main_list[0][0] - 1) % self.height][self.main_list[0][1] % self.width] = 1
        self.board[self.main_list[-1][0] % self.height][self.main_list[-1][1] % self.width] = 0
        self.main_list.insert(0, [self.main_list[0][0] - 1 % self.height, self.main_list[0][1] % self.width])
        y = self.main_list[0][0]
        x = self.main_list[0][1]
        if [y, x] in self.position_word:
            self.len_word -= 1
            self.health -= 1
            r = self.position_word.index([y, x])
            self.less_word += str(g)
            if self.less_word[-1] != self.word[self.counter]:
                if self.word not in self.learn_list:
                    self.learn_list.append(self.word)
                self.new_word()
            elif self.less_word[-1] == self.word[self.counter]:
                self.counter += 1
                del self.position_word[r]
                if self.len_word == 0:
                    self.count_TRUE_word += 1
                    self.new_word()
        else:
            self.main_list.pop()
        self.move_ = 1

    def m_down(self):
        g = str(self.board[(self.main_list[0][0] + 1) % self.height][self.main_list[0][1] % self.width])
        if self.board[(self.main_list[0][0] + 1) % self.height][self.main_list[0][1] % self.width] == 1:
            self.lose()
        self.board[(self.main_list[0][0] + 1) % self.height][self.main_list[0][1] % self.width] = 1
        self.board[self.main_list[-1][0] % self.height][self.main_list[-1][1] % self.width] = 0
        self.main_list.insert(0, [self.main_list[0][0] + 1 % self.height, self.main_list[0][1] % self.width])
        y = self.main_list[0][0]
        x = self.main_list[0][1]
        if [y, x] in self.position_word:
            self.len_word -= 1
            self.health -= 1
            r = self.position_word.index([y, x])
            self.less_word += str(g)
            if self.less_word[-1] != self.word[self.counter]:
                if self.word not in self.learn_list:
                    self.learn_list.append(self.word)
                self.new_word()
            elif self.less_word[-1] == self.word[self.counter]:
                self.counter += 1
                del self.position_word[r]
                if self.len_word == 0:
                    self.count_TRUE_word += 1
                    self.new_word()
        else:
            self.main_list.pop()
        self.move_ = 2

    def m_left(self):
        g = str(self.board[self.main_list[0][0] % self.height][(self.main_list[0][1] - 1) % self.width])
        if self.board[self.main_list[0][0] % self.height][(self.main_list[0][1] - 1) % self.width] == 1:
            self.lose()
        self.board[self.main_list[0][0] % self.height][(self.main_list[0][1] - 1) % self.width] = 1
        self.board[self.main_list[-1][0] % self.height][self.main_list[-1][1] % self.width] = 0
        self.main_list.insert(0, [self.main_list[0][0] % self.height, self.main_list[0][1] - 1 % self.width])
        y = self.main_list[0][0]
        x = self.main_list[0][1]
        if [y, x] in self.position_word:
            self.len_word -= 1
            self.health -= 1
            r = self.position_word.index([y, x])
            self.less_word += str(g)
            if self.less_word[-1] != self.word[self.counter]:
                if self.word not in self.learn_list:
                    self.learn_list.append(self.word)
                self.new_word()
            elif self.less_word[-1] == self.word[self.counter]:
                self.counter += 1
                del self.position_word[r]
                if self.len_word == 0:
                    self.count_TRUE_word += 1
                    self.new_word()
        else:
            self.main_list.pop()
        self.move_ = 3

    def m_right(self):
        # Узнаём что в следующей координате
        g = str(self.board[(self.main_list[0][0]) % self.height][(self.main_list[0][1] + 1) % self.width])

        # Если он ударяется сам об себя
        if self.board[(self.main_list[0][0]) % self.height][(self.main_list[0][1] + 1) % self.width] == 1:
            self.lose()
        # Добавление хода
        self.board[(self.main_list[0][0]) % self.height][(self.main_list[0][1] + 1) % self.width] = 1
        self.board[(self.main_list[-1][0]) % self.height][(self.main_list[-1][1]) % self.width] = 0
        self.main_list.insert(0, [(self.main_list[0][0]) % self.height, (self.main_list[0][1] + 1) % self.width])

        # Узнаем последнюю координату
        y = self.main_list[0][0]
        x = self.main_list[0][1]
        if [y, x] in self.position_word:
            self.len_word -= 1
            self.health -= 1
            self.less_word += str(g)
            if self.less_word[-1] != self.word[self.counter]:
                if self.word not in self.learn_list:
                    self.learn_list.append(self.word)
                self.new_word()
            elif self.less_word[-1] == self.word[self.counter]:
                self.counter += 1
                r = self.position_word.index([y, x])
                del self.position_word[r]
                if self.len_word == 0:
                    self.count_TRUE_word += 1
                    self.new_word()

        else:
            self.main_list.pop()
        self.move_ = 4

    def next_move(self):
        # Определение куда двигаться
        if self.move_ == 3:
            self.m_left()
        elif self.move_ == 4:
            self.m_right()
        elif self.move_ == 1:
            self.m_up()
        elif self.move_ == 2:
            self.m_down()

    def get_move(self):
        # Отправка вектора
        return self.move_

    def lose(self):
        # Если он сам себя задел
        y = random.randint(0, self.height - 1)
        x = random.randint(0, self.width - 1)
        self.main_list = [[y, x]]
        self.board = [[0] * self.width for _ in range(self.height)]
        self.new_word()

    # def new_apple(self):
    #     while [self.y, self.x] in self.main_list:
    #         self.y = random.randint(0, self.height - 1)
    #         self.x = random.randint(0, self.width - 1)
    #     self.board[self.y][self.x] = -1
    def new_word(self):
        self.screen.fill((0, 0, 0))

        # Подключение базы данных
        con = sqlite3.connect("words.db")
        r = random.randint(1, 8)
        cur = con.cursor()
        word = cur.execute(f"SELECT word FROM main_words WHERE id = {r}").fetchone()
        word, = word
        self.position_word = []
        c = 0
        self.len_word = len(word)

        # Новая доска
        self.board = [[0] * self.width for _ in range(self.height)]
        for i in range(len(self.main_list)):
            self.board[self.main_list[i][0]][self.main_list[i][1]] = 1

        # Добавление Слова
        while True:
            self.y = random.randint(0, self.height - 1)
            self.x = random.randint(0, self.width - 1)
            if [self.y, self.x] not in self.main_list and [self.y, self.x] not in self.position_word:
                self.board[self.y][self.x] = word[c]
                self.position_word.append([self.y, self.x])
                c += 1
            if len(word) == c:
                break

        # Переменные
        self.less_word = ''
        self.cpunt_all_word += 1
        self.word = word
        self.counter = 0

        # В игре
        description = cur.execute(f"SELECT disription FROM main_words WHERE id = {r}").fetchone()
        description, = description
        font = pygame.font.Font(None, 25)
        text = font.render(f"В игре:", 1, (255, 255, 255))
        text_x = 750
        text_y = 150
        self.screen.blit(text, (text_x, text_y))

        # Описание слова
        text = font.render(f"{description}", 1, (255, 255, 255))
        text_x = 50
        text_y = 50
        self.screen.blit(text, (text_x, text_y))
        con.commit()
        con.close()

        # Количество слов
        text = font.render(f"Всего слов: {self.cpunt_all_word}", 1, (255, 255, 255))
        text_x = 750
        text_y = 300
        self.screen.blit(text, (text_x, text_y))

        text = font.render(f"Правильно собранных слов: {self.count_TRUE_word}", 1, (255, 255, 255))
        text_x = 750
        text_y = 250
        self.screen.blit(text, (text_x, text_y))

        text = font.render(f"Слова которые следует подучить:", 1, (255, 255, 255))
        text_x = 750
        text_y = 350
        self.screen.blit(text, (text_x, text_y))

        text_y = 350
        for i in range(len(self.learn_list)):
            text = font.render(f"{self.learn_list[i]}", 1, (255, 255, 255))
            text_x = 750
            text_y += 20
            self.screen.blit(text, (text_x, text_y))

    def ret_word(self):
        return self.less_word
