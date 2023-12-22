<<<<<<< HEAD
from random import *
from csv import *
import sqlite3
import os
import requests
import wave
from urllib.parse import urlparse, parse_qs
from os.path import isfile, join
def speedrun():
    n=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]
    for i in range(1,5):
        for j in range(len(n)):
            print(f"({i}, \"{n[j]}\", {randint(1,22)}, \"Picsou06\", \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"),")

def salle_test():
    reader = DictReader(open("stats Portal.csv", "r"))

    for row in reader:
        t=row['salle;phase_portal_gun;nb_cubes;nb_cam;nb_boutons;nb_interupteurs;nb_platformes;nb_orbe;nb_tourelles;gateau ;acide_mortel;compagnion']
        temp=t.split(sep=";")
        print(f"(\"{temp[0]}\", {temp[1]}, {temp[2]}, {temp[3]}, {temp[4]}, {temp[5]}, {temp[6]}, {temp[7]}, {temp[8]}, {temp[9]}, {temp[10]}, {temp[11]}),")

def extraire_id_video(link):
    url = urlparse(link)
    if url.netloc == 'youtu.be':
        return url.path[1:]
    elif url.netloc in ('www.youtube.com', 'youtube.com'):
        query = parse_qs(url.query)
        if 'v' in query:
            return query['v'][0]
    return None

def telecharger_miniature(url, destination):
    dossier_destination = os.path.dirname(destination)
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    print(f"Téléchargement de la miniature à l'emplacement : {destination}")

    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)

def recuperer_miniatures():
    conn = sqlite3.connect('Portal1.db')
    cursor = conn.cursor()

    cursor.execute("SELECT salle, categorie, video FROM speedrun")
    resultats = cursor.fetchall()

    for salle, categorie, lien in resultats:
        video_id = extraire_id_video(lien)

        if video_id:
            nom_fichier = f"{salle}-{categorie}.jpg"
            chemin_complet = os.path.join('/images/MiniatureTest/', nom_fichier)

            url_miniature = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

            print(f"Téléchargement de la miniature pour {salle}-{categorie}: {url_miniature}")

            telecharger_miniature(url_miniature, chemin_complet)
        else:
            print(f"Erreur lors de l'extraction de l'ID de la vidéo pour {salle}-{categorie}")
    conn.close()



def EasterEggTourelleSound(typeofeaster):
    fichiers = [f for f in os.listdir("Son\Tourelle") if isfile(join("Son/Tourelle", f))]
    for i in range(len(fichiers)):
        print(f"({i}, {typeofeaster}, \"Son\\\Tourelle\\\{fichiers[i]}\"),")

def ListDialoguesSound():
    fichiers = [f for f in os.listdir("Dialogues")]
    return fichiers

def parcourir_dossier(dossier):
    i = 0
    for racine, sous_dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            chemin_complet = os.path.join(racine, fichier)

            if fichier.endswith('.wav'):
                nom_sous_dossier = os.path.relpath(racine, dossier)
                chemin_complet = chemin_complet.replace("\\", "\\\\")
                print(f"({i}, \"{nom_sous_dossier}\", \"{chemin_complet}\"),")
                i = i + 1

parcourir_dossier("Dialogues")
=======
from random import *
from csv import *
import sqlite3
import os
import requests
import wave
from urllib.parse import urlparse, parse_qs
from os.path import isfile, join
def speedrun():
    n=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]
    for i in range(1,5):
        for j in range(len(n)):
            print(f"({i}, \"{n[j]}\", {randint(1,22)}, \"Picsou06\", \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"),")

def salle_test():
    reader = DictReader(open("stats Portal.csv", "r"))

    for row in reader:
        t=row['salle;phase_portal_gun;nb_cubes;nb_cam;nb_boutons;nb_interupteurs;nb_platformes;nb_orbe;nb_tourelles;gateau ;acide_mortel;compagnion']
        temp=t.split(sep=";")
        print(f"(\"{temp[0]}\", {temp[1]}, {temp[2]}, {temp[3]}, {temp[4]}, {temp[5]}, {temp[6]}, {temp[7]}, {temp[8]}, {temp[9]}, {temp[10]}, {temp[11]}),")

def extraire_id_video(link):
    url = urlparse(link)
    if url.netloc == 'youtu.be':
        return url.path[1:]
    elif url.netloc in ('www.youtube.com', 'youtube.com'):
        query = parse_qs(url.query)
        if 'v' in query:
            return query['v'][0]
    return None

def telecharger_miniature(url, destination):
    dossier_destination = os.path.dirname(destination)
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    print(f"Téléchargement de la miniature à l'emplacement : {destination}")

    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)

def recuperer_miniatures():
    conn = sqlite3.connect('Portal1.db')
    cursor = conn.cursor()

    cursor.execute("SELECT salle, categorie, video FROM speedrun")
    resultats = cursor.fetchall()

    for salle, categorie, lien in resultats:
        video_id = extraire_id_video(lien)

        if video_id:
            nom_fichier = f"{salle}-{categorie}.jpg"
            chemin_complet = os.path.join('/images/MiniatureTest/', nom_fichier)

            url_miniature = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

            print(f"Téléchargement de la miniature pour {salle}-{categorie}: {url_miniature}")

            telecharger_miniature(url_miniature, chemin_complet)
        else:
            print(f"Erreur lors de l'extraction de l'ID de la vidéo pour {salle}-{categorie}")
    conn.close()



def EasterEggTourelleSound(typeofeaster):
    fichiers = [f for f in os.listdir("Son/Tourelle") if isfile(join("Son/Tourelle", f))]
    for i in range(len(fichiers)):
        print(f"({i}, {typeofeaster}, \"Son/Tourelle{fichiers[j]}\"),")

def ListDialoguesSound():
    fichiers = [f for f in os.listdir("Dialogues")]
    return fichiers

def parcourir_dossier(dossier):
    i=0
    for racine, sous_dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            chemin_complet = os.path.join(racine, fichier)

            if fichier.endswith('.wav'):
                nom_sous_dossier = os.path.relpath(racine, dossier)
                print(f"({i}, \"{nom_sous_dossier}\", \"{chemin_complet}\"),")
                i=i+1

print(parcourir_dossier("Dialogues/"))
>>>>>>> cb064ecff469fff212ad9b98453402c2bf5e4bde
