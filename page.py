from pygame import *
import pygame
import speedrun
import sqlite3

def SoundEasterEgg(type):
    if type=="portail":
        pygame.mixer.init()
        test = pygame.mixer.Sound("Dialogues\\19\\GLaDOS_15_part1_entry-1_fr.wav")
        test.play()
        test.set_volume(0.1)
    

def get_things_by_num_test(num_test,thinkstosearch):
    thinks=["phase_portal_gun","nb_cubes","nb_camera","nb_bouton","nb_interrupteur","nb_orbe","nb_plateformes_mobile","nb_tourelle","gateau","acide_mortel","compagnion"]
    with sqlite3.connect("Portal1.db") as connexion:
        c = connexion.cursor()

        c.execute(f"SELECT {thinks[thinkstosearch]} FROM salle_test WHERE num_test = ?", (num_test,))

        result = c.fetchone()

        if result:
            return result[0]
        else:
            return None


def page(screen, numofsalle):
    screen_width, screen_height = screen.get_size()
    background_game = pygame.transform.scale(pygame.image.load("images/Ensemble/background.png"), (screen_width,screen_height))
    fleche_droite = pygame.transform.scale(pygame.image.load("images/Ensemble/DROITE.png"), (90,90))
    fleche_gauche = pygame.transform.scale(pygame.image.load("images/Ensemble/GAUCHE.png"), (90,90))
    portailbleu = pygame.transform.scale(pygame.image.load("images/Ensemble/bleu.png"), (40,40))
    gateau = pygame.transform.scale(pygame.image.load("images/Ensemble/gateau.png"), (40,40))
    portailjaune = pygame.transform.scale(pygame.image.load("images/Ensemble/orange.png"), (40,40))
    bouton = pygame.transform.scale(pygame.image.load("images/Ensemble/bouton.png"), (160,160))
    compagnon = pygame.transform.scale(pygame.image.load("images/Ensemble/compagnon.png"), (40,40))
    cube = pygame.transform.scale(pygame.image.load("images/Ensemble/cube.png"), (120,120))
    interupteur = pygame.transform.scale(pygame.image.load("images/Ensemble/interupteur.png"), (120,120))
    orbe = pygame.transform.scale(pygame.image.load("images/Ensemble/orbe.png"), (60,60))
    camera = pygame.transform.scale(pygame.image.load("images/Ensemble/camera.png"), (120,120))
    tourelle = pygame.transform.scale(pygame.image.load("images/Ensemble/tourelle.png"), (110,160))
    speedrunbutton = pygame.transform.scale(pygame.image.load("images/Ensemble/SPEEDRUN.png"), (200,30))
    SallePolice = pygame.font.SysFont("bold",50)
    NumberPolice = pygame.font.SysFont("bold",40)
    mouse = pygame.mouse.get_pos()
    salle=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= mouse[0] <= 140 and screen_height-140 <= mouse[1] <= screen_height-50:
                    if numofsalle>0:
                        numofsalle=numofsalle-1
                elif screen_width-140 <= mouse[0] <= screen_width-50 and screen_height-140 <= mouse[1] <= screen_height-50:
                    if numofsalle<17:
                        numofsalle=numofsalle+1
                elif screen_height/2 <= mouse[0] <= screen_height/2+200 and 70 <= mouse[1] <= 120:
                    speedrun.speedrun(screen, numofsalle)
                elif phaseportail==1:
                    if screen_width-220 <= mouse[0] <= screen_width-180 and 70 <= mouse[1] <= 110:
                        print("SOUND PORTAIL BLEU")
                elif phaseportail>1:
                    if screen_width-180 <= mouse[0] <= screen_width-140 and 70 <= mouse[1] <= 110:
                        print("SOUND PORTAIL JAUNE")
                else:
                    SoundEasterEgg("portail")

        mouse = pygame.mouse.get_pos()
        phaseportail=get_things_by_num_test(salle[numofsalle],0)
        hascompagnon=get_things_by_num_test(salle[numofsalle],10)
        hasgateau=get_things_by_num_test(salle[numofsalle],8)
        nbbouton=get_things_by_num_test(salle[numofsalle],3)
        nbcube=get_things_by_num_test(salle[numofsalle],1)
        nbinterupteur=get_things_by_num_test(salle[numofsalle],4)
        nborbe=get_things_by_num_test(salle[numofsalle],5)
        nbcamera=get_things_by_num_test(salle[numofsalle],2)
        nbtourelle=get_things_by_num_test(salle[numofsalle],7)
        screen.blit(background_game, (0, 0))
        if phaseportail==1:
            screen.blit(portailbleu, (screen_width-220, 70))
        elif phaseportail>1:
            screen.blit(portailbleu, (screen_width-220, 70))
            screen.blit(portailjaune, (screen_width-180, 70))
        if hascompagnon:
            screen.blit(compagnon, (screen_width-260, 70))
        if hasgateau:
            screen.blit(gateau, (screen_width-300, 70))
        screen.blit(fleche_droite, (50, screen_height-150))
        screen.blit(fleche_gauche, (screen_width-140, screen_height-150))
        texte_player = SallePolice.render("Salle "+salle[numofsalle], 1 ,(250,250,250))
        texte_nbbouton = NumberPolice.render(str(nbbouton), 1 ,(250,250,250))
        texte_nbcube = NumberPolice.render(str(nbcube), 1 ,(250,250,250))
        texte_nbinterupteur = NumberPolice.render(str(nbinterupteur), 1 ,(250,250,250))
        texte_nborbe = NumberPolice.render(str(nborbe), 1 ,(250,250,250))
        texte_nbradio = NumberPolice.render(str(nbcamera), 1 ,(250,250,250))
        texte_nbtourelle = NumberPolice.render(str(nbtourelle), 1,(250,250,250))
        screen.blit(bouton, (110, 190))
        screen.blit(cube, (135, 360))
        screen.blit(interupteur, (135, 490))
        screen.blit(orbe, (screen_width-400, 210))
        screen.blit(camera, (screen_width-425, 320))
        screen.blit(tourelle, (screen_width-425, 480))
        screen.blit(texte_player, (screen_height/2+10, 10))
        screen.blit(speedrunbutton, (screen_height/2, 90))
        screen.blit(texte_nbbouton, (270, 250))
        screen.blit(texte_nbcube, (270, 400))
        screen.blit(texte_nbinterupteur, (270, 530))
        screen.blit(texte_nborbe, (screen_width-290, 250))
        screen.blit(texte_nbradio, (screen_width-290, 400))
        screen.blit(texte_nbtourelle, (screen_width-290, 530))



        pygame.display.flip()
