import sqlite3
import os
import os

def launch():
    # Connexion
    if os.path.exists("./Portal1.db"):
        os.remove("./Portal1.db")
    connexion = sqlite3.connect('Portal1.db')

def launch():
    # Connexion
    if os.path.exists("./Portal1.db"):
        os.remove("./Portal1.db")
    connexion = sqlite3.connect('Portal1.db')


    # Récupération d'un curseur
    c = connexion.cursor()
    # Récupération d'un curseur
    c = connexion.cursor()

    # Création de la table salle_test
    c.execute("""
        CREATE TABLE IF NOT EXISTS salle_test(
        num_test TEXT,
        phase_portal_gun INTEGER,
        nb_cubes INTEGER,
        nb_camera INTEGER,
        nb_bouton INTEGER,
        nb_interrupteur INTEGER,
        nb_plateformes_mobile INTEGER,
        nb_orbe INTEGER,
        nb_tourelle INTEGER,
        gateau BOOLEAN,
        acide_mortel BOOLEAN,
        compagnion BOOLEAN,
        PRIMARY KEY(num_test));
        """)

    # Création de la table speedrun
    c.execute("""
        CREATE TABLE IF NOT EXISTS speedrun(
        categorie INTEGER REFERENCES categorie (num_categories),
        salle TEXT,
        temps FLOAT,
        joueur TEXT,
        video TEXT,
        PRIMARY KEY(categorie, salle));
        """)

    # Création de la table categorie
    c.execute("""
        CREATE TABLE IF NOT EXISTS categorie(
        num_categories INTEGER,
        nom TEXT,
        PRIMARY KEY(num_categories));
        """)

    # Création de la table dialogues
    c.execute("""
        CREATE TABLE IF NOT EXISTS dialogues(
        num_dialogues INTEGER,
        name_salle TEXT,
        whereisit TEXT,
        PRIMARY KEY(num_dialogues,name_salle));
        """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS EasterEgg(
        number INTEGER,
        typeofeaster TEXT,
        whereisit TEXT,
        PRIMARY KEY(number, typeofeaster));
        """)
    # ---- fin des instructions SQL

    # Validation
    connexion.commit()

    # Déconnexion
    connexion.close()

launch()