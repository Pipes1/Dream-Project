#!/bin/python3
import random
import pygame, sys
path = 'D:/poopsex.txt'
poopy_file = open(path, 'w')
# Setup Python ----------------------------------------------- #


# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1000, 1000), 0, 32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        finalbossdamage = int

        loopage = int

        turnswitcher = 0

        loopage = 0

        bossdamage = int

        defense = int

        code = int

        damage = int

        attack = int

        dotheybesure = int

        version = "alpha indev V0.3"

        turn = str

        turn == 'your turn'

        #draw_text("""Whenever a choice appea
        #rs type the resp
        #onse you want in all lowercase letters""", font, (255, 255, 255), screen, 400, 500)
        #print('WARNING! The Are You Sure System Is WIP So DO NOT USE IT!')

        bosshealth = int

        playerhealth = int

        items = int(input("Do You Have Any Codes For Items? If Not Type 1"))
        if items == 1:
            persinput = int(input("""What Difficulty? 1, lmao not even a game,
            2, easy, 3, medium, 4, hard"""))
        else:
            persinput = int(input("""What Difficulty? 1, lmao not even
            a game, 2, easy, 3, medium, 4, hard"""))
        def user(persinput):
            if persinput == 1:
                dotheybesure = int(input("""Are You Sure You Want The Game To Not Ev
                en Be Fun? Type 5 If Not, 1 If Sure"""))
            elif persinput == 2:
                dotheybesure = int(input("""Are You Sure You Want
                Easy? Type 5 If Not, 2 If Sure"""))
            elif persinput == 3:
                dotheybesure = int(input("""Are You Sure You Want
                Medium? Type 5 If Not, 3 If Sure"""))
            elif persinput == 4:
                dotheybesure = int(input("""Are You Sure You Want Ha
                rd? Type 5 If Not, 4 If Sure"""))
            return dotheybesure
        dotheybesure = user(persinput)
        if dotheybesure == 1:
            print("""Welcome To Bethesda's Game Engine In A Nutshell!
            The Current Version Is", version, " There is No Story Yet But Im On It!""")
            if items == 29032:
                playerhealth = 0
            elif items == 80085:
                print("""No God Has Bounds Upon You, You Have Been Transcende
                d To The Sheer Power Level Of A
                God. Your Power Has No Bounds. You Roam The Realms With All Creatures,
                Mortal And Immortal In Sheer Terror
                Of Even Just The Concept Of You.""")
                playerhealth = 99999999999999999999999999999999999
                9999999999999999999999
                9999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999
            else:
                playerhealth = 100000000000
            while loopage == 0:
                if (turnswitcher % 2) == 0:
                    turn == "Your Turn"
                bosshealth = 1
                print('Remaining Health Is', playerhealth, '''
                Remaining Boss Health Is ''', bosshealth, '''
                It Is ''' , turn, 'You can attack')
                loopage = loopage+1
        while loopage == 1:
            attack = int(input("Would You Like To Attack? 1 For Yes, 2 For No."))
            if items == 1:
                damage = random.randint(0, 16)
                if attack == 1:
                    if damage > 0:
                        print('You Dealt' , damage, 'Damage')
                        bosshealth = bosshealth-damage
                        loopage = loopage+1
            elif items == 84493:
                damage = random.randint(0, 18)
                if attack == 1:
                    if damage > 0:
                        print('You Dealt' , damage, 'Damage')
                        bosshealth = bosshealth-damage
                        loopage = loopage+1
        while loopage == 2:
            if bosshealth <= 0:
                lmaoitem = random.choice(['Dirt', 'Stick', '''Dissapoin
                tment''', 'Depression', 'Chicken Nugget'])
                if lmaoitem == "Dirt":
                    code = 10554
                elif lmaoitem == "Stick":
                    code = 84493
                elif lmaoitem == "Dissapointment":
                    code = 34879
                elif lmaoitem == "Depression":
                    code = 29032
                elif lmaoitem == "Chicken Nugget":
                    code = 80085
                    print("Congratulations! You Did Absolutely Nothing Challenging!")
                    print('You Got,' , lmaoitem, '!')
                    print('''Use This Code And Restart The
                    Game To Use Your Item''' , code, '!')
                    loopage = loopage+1
                elif damage <= 0:
                    print('''You Missed, You Malformed, Battered,
                    And Deep Fried Greasy Chunk Of Chicken Scraps.''')
                while (turnswitcher % 2) == 0:
                    turn = "Boss' Turn"
                    print('Remaining Health Is', playerhealth, '''
                    Remaining Boss Health Is ''', bosshealth, ''' It Is
                    ''' , turn, 'You can defend')
                    defend = input("Would You Like To Defend? 1 For Yes, 2 For No.")
                    bossdamage = random.randint(1, 30)
                    if defend == 1:
                        defense = random.randint(1, 20)
                        if bossdamage-defense <= 0:
                            bossdamage = 0
                        elif bossdamage-defense >= 0:
                            finalbossdamage = bossdamage-defense
                            playerhealth = playerhealth-finalbossdamage
                    elif playerhealth <= 0:
                        loopage = 1
                        if items == 29032:
                            print("""Why Would You Think It's A Good
                            Idea To Use An Item Named Depression?""")
                        else:
                            print("How Did You Even Manage To Die On This Difficulty?")
        dotheybesure = user(persinput)
        if dotheybesure == 2:
            print("Welcome To The Game! The Current Version Is", version, """ There
            is No Story Yet But Im On It!""")
            if items == 29032:
                playerhealth = 0
            elif items == 80085:
                print("""No God Has Bounds Upon You, You Have Been Transcended To The
                Sheer Power Level Of
                A God. You
                r Power Has No Bounds. You Roam The Realms With All Creatures,
                Mortal And Imm
                ortal In Sheer Terror Of
                Even Just The Concept Of You.""")
                playerhealth = 999999999999999999999999999999999999999999999999999
                99999999999999999999
                999999999999999999999999999999999999999999999999999999999999999999999
            else:
                playerhealth = 100000000000
        while loopage == 0:
            if (turnswitcher % 2) == 0:
                turn == "Your Turn"
            bosshealth = 1
            print('Remaining Health Is', playerhealth, ''' Remaining Boss
            Health Is ''', bosshealth, ' It Is', turn, 'You can attack')
            loopage = loopage+1
        while loopage == 1:
            attack = int(input("Would You Like To Attack? 1 For Yes, 2 For No."))
            if items == 1:
                damage = random.randint(0, 16)
                if attack == 1:
                    if damage > 0:
                        print('You Dealt' , damage, 'Damage')
                        bosshealth = bosshealth-damage
                        loopage = loopage+1
            elif items == 84493:
                damage = random.randint(0, 18)
                if attack == 1:
                    if damage > 0:
                        print('You Dealt' , damage, 'Damage')
                        bosshealth = bosshealth-damage
                        loopage = loopage+1
        while loopage == 2:
            if bosshealth <= 0:
                easyitem = random.choice(["Bronze Sword", "Cooler Stick", """Old Bow
                And Arrow""", "Even Cooler Stick", """Strange Vintage
                Collector's Chicken Nugget"""])
                print("Congratulations! You Did Absolutely Nothing Challenging!")
                print('You Got,' , easyitem, '!')
                loopage = loopage+1
            elif damage <= 0:
                print('''You Missed, You Malformed, Battered,
                And Deep Fried Greasy Chunk Of Chicken Scraps.''')
            while (turnswitcher % 2) == 0:
                turn = "Boss' Turn"
                print('Remaining Health Is', playerhealth, ''' Remaining Boss
                Health Is ''', bosshealth, ' It Is', turn, 'You can defend')
                defend = input("Would You Like To Defend? 1 For Yes, 2 For No.")
                bossdamage = random.randint(1, 5)
                if defend == 1:
                    defense = random.randint(1, 20)
                    if bossdamage-defense <= 0:
                        bossdamage = 0
        while playerhealth <= 0:
            loopage = 1
            if items == 29032:
                print("""Why Would You Think It's A Good
                Idea To Use An Item Named Depression?""")
            else:
                print("Its Kinda Sad You Died But... On Easy?")
click = False

def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text("Bethesda's Game Engine In A Nutshell", font, (255, 255, 255), screen, 400, 50)

        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(400, 100, 200, 50)
        button_2 = pygame.Rect(400, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        draw_text('music', font, (255, 255, 255), screen, 400, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()
