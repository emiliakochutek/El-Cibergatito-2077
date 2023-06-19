import pygame
from sys import exit
from random import choice
from cat import Cat
from paper import Paper
from constant_stuff import *

cat = pygame.sprite.GroupSingle()
cat.add(Cat())
obstacle_group = pygame.sprite.Group()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1600)


class GameState():
    def __init__(self):
        self.state = 'start'
        self.score = 0
        self.start_time = 0

        self.user_text = ''
        self.answer = ''

        self.person = ''
        self.infinitive = ''
        self.total_score = 0

    def state_manager(self):
        if self.state == 'start': self.start()
        if self.state == 'main': self.main()
        if self.state == 'spanish': self.spanish()

    def display_score(self):
        current_time = self.get_current_time() - self.start_time
        score_surf = SCORE_FONT.render(f'Score: {current_time + self.total_score}', True, 'White')
        score_rect = score_surf.get_rect(center = (WIDTH/2, 80))
        SCREEN.blit(score_surf, score_rect)
        return current_time

    def collision(self):
        if pygame.sprite.spritecollide(cat.sprite, obstacle_group, True):
            obstacle_group.empty()
            return True
        return False

    def get_current_time(self):
        return int(pygame.time.get_ticks() / 1000)

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'main'
                self.score = 0
                self.total_score = 0
                self.start_time = self.get_current_time()


        SCREEN.fill('#D37D98')
        SCREEN.blit(NAME_SURF, NAME_RECT)
        SCREEN.blit(CAT_STAND, CAT_RECT)

        score_message = MESSAGE_FONT.render(f'Your score: {self.total_score}', True, 'Black')
        score_message_rect = score_message.get_rect(center = (WIDTH/2 , 330))

        if self.score == 0:
            SCREEN.blit(MESSAGE_SURF1, MESSAGE_RECT1)
            SCREEN.blit(MESSAGE_SURF2, MESSAGE_RECT2)
        else:
            SCREEN.blit(MESSAGE_SURF3, MESSAGE_RECT3)
            SCREEN.blit(score_message, score_message_rect)

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == obstacle_timer:
                obstacle_group.add(Paper(choice(['light', 'dark', 'light'])))


        SCREEN.blit(NIGHT_SURF,(0,0))
        SCREEN.blit(GROUND_SURF,(0,350))
        self.score = self.display_score()

        cat.draw(SCREEN)
        cat.update()

        obstacle_group.draw(SCREEN)
        obstacle_group.update()

        if self.collision():
            self.state = 'spanish'
            self.total_score += self.score

    def spanish(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.answer = self.user_text
                    irregular_conjugated = self.load_irregulars(INFINITIVES_IRREGULAR_FILE_PATH)
                    is_good_answer = self.validate_answer(self.infinitive, self.person, self.answer, irregular_conjugated)
                    if is_good_answer:
                        self.reset()
                        self.state = 'main'
                        self.start_time = self.get_current_time()
                    else:
                        self.reset()
                        self.state = 'start'
                else:
                    self.user_text += event.unicode

        if self.is_task_not_chosen(): self.draw_stuff()

        task_message = f'Write \'{self.infinitive}\' in the {self.person} person:'
        task_surf = FONT_ON_PAPER.render(task_message, True, 'Black')
        task_rect = task_surf.get_rect(midtop = (WIDTH/2,100))
        task_bg = pygame.Rect(50,100,700,30)
        input_surf = FONT_ON_PAPER.render(self.user_text, True, 'White')
        input_rect = input_surf.get_rect(midtop = (WIDTH/2,200))
        input_bg = pygame.Rect(150,200,500,30)

        SCREEN.blit(PAPER_BG_SURF, (0,0))
        pygame.draw.rect(SCREEN, 'darkblue', input_bg)
        pygame.draw.rect(SCREEN, 'lightgray', task_bg)
        SCREEN.blit(task_surf, task_rect)
        SCREEN.blit(input_surf, input_rect)

    def is_task_not_chosen(self):
        return self.infinitive == '' and self.person == ''

    def reset(self):
        self.infinitive = ''
        self.person = ''
        self.user_text = ''

    def draw_stuff(self):
        self.infinitive = choice(INFINITIVES)
        self.person = choice(['singular 1st', 'singular 2nd', 'singular 3rd',
                              'plural 1st', 'plural 2nd', 'plural 3rd'])

    def load_irregulars(self, infinitives_irregular_file_path):
        self.correct_irregulars = {}
        with open(infinitives_irregular_file_path) as file:
            for line in file:
                lst = line.split()
                self.correct_irregulars[lst[0]] = lst
        return self.correct_irregulars

    def check_regulars(self, infinitive, person, answer):
        ending = infinitive[-2:]
        word_stem = infinitive[:-2]
        checked_ar = ending == 'ar' and answer == (word_stem + GROUP_AR[person])
        checked_er_ir = (ending == 'er' or ending == 'ir') and answer == (word_stem + GROUP_ER_IR[person])
        return checked_ar or checked_er_ir

    def check_irregulars(self, infinitive, person, answer, irregular_to_conjugation):
        return answer == irregular_to_conjugation[infinitive][PERSONS[person]]

    def validate_answer(self, infinitive, person, answer, irregular_conjugated):
        is_good_answer = False
        if infinitive not in INFINITIVES_IRREGULAR:
            is_good_answer = self.check_regulars(infinitive, person, answer)
        else: is_good_answer = self.check_irregulars(infinitive, person, answer, irregular_conjugated)
        return is_good_answer
