import sqlite3

#Connexion
connexion = sqlite3.connect('Portal1.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL

#Création de la table

# c.execute("""
#     INSERT INTO dialogues;
# """)

c.execute("""
    INSERT INTO salle_test
    VALUES ("00-01", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("02-03", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("04-05", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("06-07", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("08", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("09", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("10", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("11-12", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("13", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("14", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("15", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("16", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("13", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("14", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("15", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("16", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("17", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("18", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("19", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("e00", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("e01", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("e02", 0, 0, 0, 0, 0, 0, 0, False, False);
    """)
#["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]

c.execute("""
    INSERT INTO categorie
    VALUES (1, "Glitchless"),
        (2, "OOB"),
        (3, "NO SLA")
        (4, "Inbounds");
""")

c.execute("""
    INSERT INTO speedrun
    VALUES (1, "00-01", 14, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "02-03", 11, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "04-05", 17, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "06-07", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "08", 16, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "09", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "10", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "11-12", 14, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "13", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "14", 15, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "15", 7, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "16", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "17", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "18", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "19", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "e00", 14, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "e01", 20, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(1, "e02", 16, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "00-01", 8, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "02-03", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "04-05", 17, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "06-07", 12, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "08", 17, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "09", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "10", 12, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "11-12", 13, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "13", 3, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "14", 21, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "15", 2, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "16", 13, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "17", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "18", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "19", 15, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "e00", 21, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "e01", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(2, "e02", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "00-01", 11, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "02-03", 17, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "04-05", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "06-07", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "08", 2, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "09", 1, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "10", 2, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "11-12", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "13", 17, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "14", 14, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "15", 6, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "16", 20, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "17", 21, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "18", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "19", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "e00", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "e01", 8, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(3, "e02", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "00-01", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "02-03", 15, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "04-05", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "06-07", 20, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "08", 20, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "09", 8, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "10", 16, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "11-12", 9, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "13", 2, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "14", 18, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "15", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "16", 7, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "17", 4, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "18", 21, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "19", 1, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "e00", 2, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "e01", 20, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
(4, "e02", 10, "Picsou06", "https://www.youtube.com/watch?v=dQw4w9WgXcQ");
""")

# ---- fin des instructions SQL

#Validation
connexion.commit()


#Déconnexion
connexion.close()