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
    VALUES ("00-01", 0, 2, 4, 0, 2, 0, 0, 0, False, False, False),
            ("02-03", 1, 0, 6, 0, 0, 0, 0, 0, False, False, False),
            ("04-05", 1, 3, 5, 0, 3, 0, 0, 0, False, False, False),
            ("06-07", 1, 0, 0, 0, 0, 2, 2, 0, False, False, False),
            ("08", 1, 0, 0, 0, 0, 1, 1, 0, False, True, False),
            ("09", 1, 1, 0, 0, 1, 0, 0, 0, False, False, False),
            ("10", 1, 0, 1, 0, 0, 0, 0, 0, False, False, False),
            ("11-12", 2, 1, 1, 2, 1, 1, 1, 0, False, True, False),
            ("13", 2, 2, 3, 0, 3, 1, 1, 0, False, False, False),
            ("14", 2, 1, 0, 0, 1, 1, 1, 0, False, True, False),
            ("15", 2, 0, 5, 2, 0, 5, 3, 0, False, True, False),
            ("16", 2, 10, 5, 0, 1, 0, 0, 11, False, False, False),
            ("17", 2, 0, 6, 1, 3, 3, 3, 0, False, False, True),
            ("18", 2, 1, 7, 3, 1, 1, 1, 4, False, True, False),
            ("19", 2, 1, 3, 1, 0, 1, 2, 0, True, True, False),
            ("e00", 2, 0, 0, 0, 0, 0, 0, 0, False, False, False),
            ("e01", 2, 1, 0, 1, 0, 0, 0, 5, False, True, False),
            ("e02", 2, 0, 0, 0, 0, 0, 0, 10, True, True, False);
    """)
#["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]

c.execute("""
    INSERT INTO categorie
    VALUES (1, "Glitchless"),
           (2, "OOB"),
           (3, "Inbounds");
""")

c.execute("""
    INSERT INTO speedrun
    VALUES
    (1, "00-01", "2m02s790ms", "SiDiouS", "https://youtu.be/RWnuM6Q7Abs"),
    (1, "02-03", "1m06s750ms", "SiDiouS", "https://youtu.be/l3HC1YUo914?t=72"),
    (1, "04-05", "0m59s655ms", "SiDiouS", "https://youtu.be/vFwvG8GJZMU"),
    (1, "06-07", "0m43s260ms", "SiDiouS", "https://youtu.be/Haq-ADBYl18"),
    (1, "08", "0m22s200ms", "SiDiouS", "https://youtu.be/vaIABzlP4VQ"),
    (1, "09", "0m22s155ms", "SiDiouS", "https://youtu.be/9pjq1JmIWzs"),
    (1, "10", "0m27s990ms", "SiDiouS", "https://youtu.be/_aupAFFtWmY"),
    (1, "11-12", "0m46s140ms", "SiDiouS", "https://youtu.be/xlUrQkH593U"),
    (1, "13", "0m21s360ms", "SiDiouS", "https://youtu.be/Juy3_0Y-yUs"),
    (1, "14", "0m18s285ms", "SiDiouS", "https://youtu.be/ulzdxtACjxc"),
    (1, "15", "0m29s715ms", "SiDiouS", "https://youtu.be/pn_9fcuErEg"),
    (1, "16", "0m42s345ms", "SiDiouS", "https://youtu.be/vSdMCojohlI"),
    (1, "17", "1m00s405ms", "SiDiouS", "https://youtu.be/dkQwu9KNFUI"),
    (1, "18", "0m48s855ms", "SiDiouS", "https://youtu.be/7kqyAmQL3oA"),
    (1, "19", "0m31s590ms", "SiDiouS", "https://youtu.be/VbDt9Ov2HWs"),
    (1, "e00", "0m22s560ms", "SiDiouS", "https://youtu.be/26KFcYrwpdE"),
    (1, "e01", "0m29s745ms", "SiDiouS", "https://youtu.be/GIzXyCVDoyQ"),
    (1, "e02", "1m54s435ms", "SiDiouS", "https://youtu.be/ii9HTuKNnXU"),
    (1, "complet", "14m29s205ms", "SiDiouS", "https://youtu.be/l3HC1YUo914"),
    (2, "00-01", "1m09s795ms", "Floorb", "PDV"),
    (2, "02-03", "0m48s525ms", "Sarahspeedrun", "https://youtu.be/uKSVm2Cd_Og"),
    (2, "04-05", "0m35s835ms", "Sarahspeedrun", "https://youtu.be/4qvCzH_XWK8"),
    (2, "06-07", "0m18s435ms", "SiDiouS", "https://youtu.be/IXqg---dIoI"),
    (2, "08", "0m12s310ms", "Floorb", "https://youtu.be/KZ1QPxooIbk"),
    (2, "09", "0m20s505ms", "SiDiouS", "https://youtu.be/-yrz7kUzIII"),
    (2, "10", "0m15s690ms", "SiDiouS", "https://youtu.be/83dSIXz1-wE"),
    (2, "11-12", "0m18s135ms", "SiDiouS", "https://youtu.be/p-zfbACb60g"),
    (2, "13", "0m17s220ms", "SiDiouS", "https://youtu.be/x6AL-r6XPiY"),
    (2, "14", "0m15s930ms", "RealCreative", "https://youtu.be/0BtzqNZdnaM"),
    (2, "15", "0m17s805ms", "SiDiouS", "https://youtu.be/E4icW41bZUk"),
    (2, "16", "0m18s345ms", "SiDiouS", "https://youtu.be/jrmQCXuF9Pw"),
    (2, "17", "0m28s470ms", "SiDiouS", "https://youtu.be/g-spBg7KbvA"),
    (2, "18", "0m29s265ms", "SiDiouS", "https://youtu.be/7FGWUV9VsUo"),
    (2, "19", "0m03s885ms", "RealCreative", "https://youtu.be/WUGnb3LG5zU"),
    (2, "e00", "0m02s550ms", "SiDiouS", "https://youtu.be/KFDCKMffrCg"),
    (2, "e01", "0m05s580ms", "SiDiouS", "https://youtu.be/Vt3tPC7YySs"),
    (2, "e02", "0m31s980ms", "SiDiouS", "https://youtu.be/4edlRvC9af0"),
    (2, "complet", "05m50s340ms", "Sarahspeedrun", "https://youtu.be/SCrfnfMe9F4"),
    (3, "00-01", "01m09s795ms", "Floorb", "PDV"),
    (3, "02-03", "01m02s115ms", "Floorb", "https://youtu.be/C4vHHrnntV8"),
    (3, "04-05", "00m56s670ms", "SiDiouS", "https://youtu.be/tvWRp3pBXDw"),
    (3, "06-07", "00m40s185ms", "SiDiouS", "https://youtu.be/pyJkqMIZhjw"),
    (3, "08", "0m17s310ms", "Floorb", "https://youtu.be/KZ1QPxooIbk"),
    (3, "09", "0m20s505ms", "SiDiouS", "https://youtu.be/-yrz7kUzIII"),
    (3, "10", "0m21s690ms", "RealCreative", "https://youtu.be/us6_sWNbF4Y"),
    (3, "11-12", "0m26s035ms", "SiDiouS", "https://youtu.be/JCoC-3S02mY"),
    (3, "13", "0m20s490ms", "SiDiouS", "https://youtu.be/yXkBHRFOKX8"),
    (3, "14", "0m17s325ms", "Reassagressta", "https://youtu.be/kGMNVSX3QfU"),
    (3, "15", "0m26s460ms", "SiDiouS", "https://youtu.be/ZxAlyQklz7k"),
    (3, "16", "0m20s805ms", "SiDiouS", "https://youtu.be/ynsEUyYV-PA"),
    (3, "17", "0m28s470ms", "SiDiouS", "https://youtu.be/aNIvLScbt5Q"),
    (3, "18", "0m29s265ms", "SiDiouS", "https://youtu.be/GLZSEn7S3lY"),
    (3, "19", "0m03s885ms", "RealCreative", "https://youtu.be/Qu2WXceCjlw"),
    (3, "e00", "0m02s550ms", "SiDiouS", "https://youtu.be/qkSvlAif3EA"),
    (3, "e01", "0m05s580ms", "SiDiouS", "https://youtu.be/Yv3iHeG3sE4"),
    (3, "e02", "0m31s980ms", "SiDiouS", "https://youtu.be/BKEaW49B250"),
    (3, "complet", "8m16s395ms", "Sarahspeedrun", "https://youtu.be/iYWWp5iQr1E");
""")

#Validation
connexion.commit()


#Déconnexion
connexion.close()