import sqlite3
import update_db
import create_db
import os

def getcollumname(name):
    connection = sqlite3.connect('Portal1.db')
    c = connection.cursor()

    c.execute(f"PRAGMA table_info({name})")

    result = [column[1] for column in c.fetchall()]

    return result

def listetable():
    tempdico={}
    connexion = sqlite3.connect('Portal1.db')
    c = connexion.cursor()

    c.execute("""select name from sqlite_master  where type = \"table\"""")
    result = c.fetchall()

    print(result)
    temp=1
    for i in result:
        tempdico[i[0]]=f"[{temp}] Modifier la table {i[0]}"
        temp=temp+1
    return tempdico

def actionaddontable(name):
    listecollum = getcollumname(name)
    
    # En supposant que vous voulez demander à l'utilisateur d'entrer des valeurs pour chaque colonne
    values = []
    for col in listecollum:
        value = input(f"Entrez la valeur pour {col} : ")
        values.append(value)

    # Créer la requête SQL pour insérer la nouvelle ligne
    query = f"INSERT INTO {name} ({', '.join(listecollum)}) VALUES ({', '.join(['?']*len(listecollum))})"
    
    # Exécuter la requête avec les valeurs fournies
    connection = sqlite3.connect('Portal1.db')
    c = connection.cursor()
    c.execute(query, tuple(values))
     # Validation
    connection.commit()

    # Déconnexion
    connection.close()
    return "Donnée ajouté!"


def affichagetable(name):
    listecollum = getcollumname(name)
    response = actionlistontable(name)

    # Imprimer les noms de colonnes
    header = "\t".join(listecollum)
    print(header)

    # Imprimer les données ligne par ligne
    for row in response:
        row_values = "\t".join(str(row[col]) for col in listecollum)
        print(row_values)

def actionremoveontable(name):
    listecollum = getcollumname(name)
    response = actionlistontable(name)

    # Imprimer les noms de colonnes
    header = "\t".join(listecollum)
    print(header)

    # Imprimer les données ligne par ligne
    for row in response:
        row_values = "\t".join(str(row[col]) for col in listecollum)
        print(row_values)
    print("[#] Annuler")

    # Demander à l'utilisateur quelle ligne supprimer
    thing_to_remove = input("Entrez le premier élément de la ligne que vous souhaitez supprimer : ")

    if thing_to_remove!="#":
        # Supprimer la ligne sélectionnée
        connection = sqlite3.connect('Portal1.db')
        c = connection.cursor()

        # Obtenez la valeur de la clé primaire (ajustez cela en fonction de votre schéma)

        c.execute(f"DELETE FROM {name} WHERE {listecollum[0]}=?", (thing_to_remove,))
        connection.commit()
        connection.close()

        print("Ligne supprimée avec succès.")


def actionlistontable(name):
    response=[]
    listecollum = getcollumname(name)
    tempdico = {}
    connexion = sqlite3.connect('Portal1.db')
    c = connexion.cursor()

    c.execute(f"""select * from {name}""")
    result = c.fetchall()

    for i in range(len(result)):
        tempdico = {}
        for j in range(len(result[i])):
            tempdico[listecollum[j]] = result[i][j]
        response.append(tempdico)
    return response

def actiontable(name):
    print("[1] Ajouter un élément")
    print("[2] Supprimer un élément")
    print("[3] Lister les éléments")
    print("[#] Quitter")
    choix=input("Choix: ")
    if choix=="#":
        exit()
    if choix=="1":
        print(actionaddontable(name))
    if choix=="2":
        print(actionremoveontable(name))
    if choix=="3":
        affichagetable(name)
            

while True:
    print("Que souhaitez vous faire: ")
    print("[1] Modifier une table")
    print("[2] Réinitialiser la BDD")
    print("[#] Quitter")
    choix=input("Choix: ")
    if choix=="#":
        exit()
    elif choix=="2":
        os.remove("Portal1.db")
        create_db.launch()
        update_db.launch()
    elif choix=="1":
        dicotable=listetable()
        listoftable=[]
        print(dicotable)
        for i in dicotable:
            print(dicotable[i])
            listoftable.append(i)
        print("[#] Quitter")
        choix=input("Choix: ")
        if choix=="#":
            exit()
        actiontable(listoftable[int(choix)-1])