import sqlite3
import os

def launch():
    # Connexion
    if os.path.exists("./Portal1.db"):
        os.remove("./Portal1.db")
    connexion = sqlite3.connect('Portal1.db')


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
        categorie INTEGER,
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
        num_salle TEXT,
        dialogue TEXT,
        PRIMARY KEY(num_dialogues));
        """)

    # Création de la table liste_dialogues
    c.execute("""
        CREATE TABLE IF NOT EXISTS liste_dialogues(
        num_salle TEXT,
        num_dialogues INTEGER,
        PRIMARY KEY(num_salle, num_dialogues),
        FOREIGN KEY(num_salle) REFERENCES salle_test(num_test),
        FOREIGN KEY(num_dialogues) REFERENCES dialogues(num_dialogues));
        """)

    # ---- fin des instructions SQL

    # Validation
    connexion.commit()

    # Déconnexion
    connexion.close()

launch()