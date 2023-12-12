import sqlite3
import create_db

#Connexion
create_db.launch()
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
           ("04-05", 0, 0, 0, 0, 0, 0, 0, False, True),
           ("06-07", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("08", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("09", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("10", 0, 0, 0, 0, 0, 0, 0, False, False),
           ("11-12", 0, 0, 0, 0, 0, 0, 0, False, False),
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
           (3, "Inbounds"),
           (4, "Inbounds NO SLA");
""")

c.execute("""
    INSERT INTO speedrun
    VALUES (1, "00-01", 2m02s790ms, "SiDiouS", "https://youtu.be/RWnuM6Q7Abs"),
(1, "02-03", 1m06s750ms, "SiDiouS", "https://youtu.be/l3HC1YUo914?t=72"),
(1, "04-05", 0m59s655ms, "SiDiouS", "https://youtu.be/vFwvG8GJZMU"),
(1, "06-07", 0m43s260ms, "SiDiouS", "https://youtu.be/Haq-ADBYl18"),
(1, "08", 0m22s200ms, "SiDiouS", "https://youtu.be/vaIABzlP4VQ"),
(1, "09", 0m22s155ms, "SiDiouS", "https://youtu.be/9pjq1JmIWzs"),
(1, "10", 0m27s990ms, "SiDiouS", "https://youtu.be/_aupAFFtWmY"),
(1, "11-12", 0m46s140ms, "SiDiouS", "https://youtu.be/xlUrQkH593U"),
(1, "13", 0m21s360ms, "SiDiouS", "https://youtu.be/Juy3_0Y-yUs"),
(1, "14", 0m18s285ms, "SiDiouS", "https://youtu.be/ulzdxtACjxc"),
(1, "15", 0m29s715ms, "SiDiouS", "https://youtu.be/pn_9fcuErEg"),
(1, "16", 0m42s345ms, "SiDiouS", "https://youtu.be/vSdMCojohlI"),
(1, "17", 1m00s405ms, "SiDiouS", "https://youtu.be/dkQwu9KNFUI"),
(1, "18", 0m48s855ms, "SiDiouS", "https://youtu.be/7kqyAmQL3oA"),
(1, "19", 0m31s590ms, "SiDiouS", "https://youtu.be/VbDt9Ov2HWs"),
(1, "e00", 0m22s560ms, "SiDiouS", "https://youtu.be/26KFcYrwpdE"),
(1, "e01", 0m29s745ms, "SiDiouS", "https://youtu.be/GIzXyCVDoyQ"),
(1, "e02", 1m54s435ms, "SiDiouS", "https://youtu.be/ii9HTuKNnXU"),
(1, "complet", 14m29s205ms, "SiDiouS", "https://youtu.be/l3HC1YUo914"),
(2, "00-01", 1m09s795ms, "Floorb", "PDV"),
(2, "02-03", 0m48s525ms, "Sarahspeedrun", "https://youtu.be/uKSVm2Cd_Og"),
(2, "04-05", 0m35s835ms, "Sarahspeedrun", "https://youtu.be/4qvCzH_XWK8"),
(2, "06-07", 0m18s435ms, "SiDiouS", "https://youtu.be/IXqg---dIoI"),
(2, "08", 0m12s310ms, "Floorb", "https://youtu.be/KZ1QPxooIbk"),
(2, "09", 0m20s505ms, "SiDiouS", "https://youtu.be/-yrz7kUzIII"),
(2, "10", 0m15s690ms, "SiDiouS", "https://youtu.be/83dSIXz1-wE"),
(2, "11-12", 0m18s135ms, "SiDiouS", "https://youtu.be/p-zfbACb60g"),
(2, "13", 0m17s220ms, "SiDiouS", "https://youtu.be/x6AL-r6XPiY"),
(2, "14", 0m15s930ms, "RealCreative", "https://youtu.be/0BtzqNZdnaM"),
(2, "15", 0m17s805ms, "SiDiouS", "https://youtu.be/E4icW41bZUk"),
(2, "16", 0m18s345ms, "SiDiouS", "https://youtu.be/jrmQCXuF9Pw"),
(2, "17", 0m28s470ms, "SiDiouS", "https://youtu.be/g-spBg7KbvA"),
(2, "18", 0m29s265ms, "SiDiouS", "https://youtu.be/7FGWUV9VsUo"),
(2, "19", 0m03s885ms, "RealCreative", "https://youtu.be/WUGnb3LG5zU"),
(2, "e00", 0m02s550ms, "SiDiouS", "https://youtu.be/KFDCKMffrCg"),
(2, "e01", 0m05s580ms, "SiDiouS", "https://youtu.be/Vt3tPC7YySs"),
(2, "e02", 0m31s980ms, "SiDiouS", "https://youtu.be/4edlRvC9af0"),
(2, "complet", 05m50s340ms, "Sarahspeedrun", "https://youtu.be/SCrfnfMe9F4"),
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