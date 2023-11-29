BDD Portal 1

    salle_test {

    __num_test__ : TEXT
    phase_portal_gun : INT
    nb_cubes : INT
    nb_bouton : INT
    nb_orbe : INT
    nb_plateformes_mobile : INT
    nb_tourelle : INT 
    nb_cameras : INT
    acide_mortel : BOOLEAN
    gateau : BOOLEAN
    #dialogue : INT
    }

    speedrun{

    __#categorie__: INT
    __salle__: TEXT
    temps: FLOAT
    joueur: TEXT
    video: TEXT
    }

    categorie{

    __num_categories__: INT
    nom: TEXT
    }
    exemple: (1: WR_glitchless, WR_OoB, WR_no_SLA, WR_inbounds)

    dialogues{
    __num_dialogues__: INT
    dialogue: TEXT
    }

    liste_dialogues{
        #__num_salle__  TEXT
        #__num_dialogues__

    }


    IDEE

    defis {

    __num_salle__ : TEXT
    WR_moins_portail : INT
    WR_moins_pas : INT

    }

    salle_avancee {

    __num_salle__ : TEXT
    presente : BOOLEAN

    }