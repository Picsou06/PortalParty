from pygame import *
import pygame
import page
import webbrowser
import sqlite3
import os

def get_things_by_num_test(cat,salle,thinkstosearch):
    thinks=["temps","joueur","video"]
    with sqlite3.connect("Portal1.db") as connexion:
        c = connexion.cursor()
        c.execute(f"SELECT {thinks[thinkstosearch]} FROM speedrun JOIN categorie ON speedrun.categorie = categorie.num_categories WHERE speedrun.salle = ? AND categorie.nom = ?", (salle,cat))

        result = c.fetchone()

        if result:
            return result[0]
        else:
            return None

def speedrun(screen, numofsalle):
    screen_width, screen_height = screen.get_size()
    background_game = pygame.transform.scale(pygame.image.load("images/Ensemble/background.png"), (screen_width,screen_height))
    retour = pygame.transform.scale(pygame.image.load("images/Ensemble/retour.png"), (50,50))
    SallePolice = pygame.font.SysFont("bold",50)
    NumberPolice = pygame.font.SysFont("bold",40)
    mouse = pygame.mouse.get_pos()
    salle=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]
    if os.path.exists(f"images/Miniature/{salle[numofsalle]}-1.jpg"):
        Speedrun01=pygame.transform.scale(pygame.image.load(f"images/Miniature/{salle[numofsalle]}-1.jpg"), (288,180))
    else:
        Speedrun01=pygame.transform.scale(pygame.image.load(f"images/Miniature/PDV.jpg"), (288,180))
    if os.path.exists(f"images/Miniature/{salle[numofsalle]}-2.jpg"):
        Speedrun02=pygame.transform.scale(pygame.image.load(f"images/Miniature/{salle[numofsalle]}-2.jpg"), (288,180))
    else:
        Speedrun02=pygame.transform.scale(pygame.image.load(f"images/Miniature/PDV.jpg"), (288,180))
    if os.path.exists(f"images/Miniature/{salle[numofsalle]}-3.jpg"):
        Speedrun03=pygame.transform.scale(pygame.image.load(f"images/Miniature/{salle[numofsalle]}-3.jpg"), (288,180))
    else:
        Speedrun03=pygame.transform.scale(pygame.image.load(f"images/Miniature/PDV.jpg"), (288,180))
    link1=get_things_by_num_test("GlitchLess",salle[numofsalle],2)
    link2=get_things_by_num_test("In Bounds",salle[numofsalle],2)
    link3=get_things_by_num_test("Out Of bounds",salle[numofsalle],2)
    Temps1 = get_things_by_num_test("GlitchLess",salle[numofsalle],0)
    Temps2 = get_things_by_num_test("In Bounds",salle[numofsalle],0)
    Temps3 = get_things_by_num_test("Out Of bounds",salle[numofsalle],0)
    User1 = get_things_by_num_test("GlitchLess",salle[numofsalle],1)
    User2 = get_things_by_num_test("In Bounds",salle[numofsalle],1)
    User3 = get_things_by_num_test("Out Of bounds",salle[numofsalle],1)

    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= mouse[0] <= 100 and 50 <= mouse[1] <= 100:
                    page.page(screen, numofsalle)
                if 20 <= mouse[0] <= 308 and 250 <= mouse[1] <= 430:
                    webbrowser.open(link1)
                if 350 <= mouse[0] <= 638 and 250 <= mouse[1] <= 430:
                    webbrowser.open(link2)
                if 350 <= mouse[0] <= 968 and 250 <= mouse[1] <= 430:
                    webbrowser.open(link3)

        mouse = pygame.mouse.get_pos()
        screen.blit(background_game, (0, 0))
        texte_GlitchLess = NumberPolice.render("GlitchLess", 1 ,(250,250,250))
        texte_OOB = NumberPolice.render("Out Of bounds", 1 ,(250,250,250))
        texte_InBounds = NumberPolice.render("in Bounds", 1 ,(250,250,250))
        texte_player = SallePolice.render("Salle "+salle[numofsalle], 1 ,(250,250,250))
        texte_time1 = NumberPolice.render(Temps1, 1 ,(30,144,255))
        texte_time2 = NumberPolice.render(Temps2, 1 ,(30,144,255))
        texte_time3 = NumberPolice.render(Temps3, 1 ,(30,144,255))
        texte_speedrunner1 = NumberPolice.render(User1, 1 ,(30,144,255))
        texte_speedrunner2 = NumberPolice.render(User2, 1 ,(30,144,255))
        texte_speedrunner3 = NumberPolice.render(User3, 1 ,(30,144,255))
        screen.blit(retour, (50, 50))
        screen.blit(texte_player, (screen_height/2+10, 10))
        screen.blit(texte_GlitchLess, (90, 200))
        screen.blit(texte_OOB, (400, 200))
        screen.blit(texte_InBounds, (740, 200))
        screen.blit(Speedrun01, (20, 250))
        screen.blit(Speedrun02, (350, 250))
        screen.blit(Speedrun03, (680, 250))
        screen.blit(texte_time1, (70, 430))
        screen.blit(texte_time2, (400, 430))
        screen.blit(texte_time3, (730, 430))
        screen.blit(texte_speedrunner1, (105, 460))
        screen.blit(texte_speedrunner2, (415, 460))
        screen.blit(texte_speedrunner3, (735, 460))
        pygame.display.flip()