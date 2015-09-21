# Functions file

def keyboard_input():
    """Entrée interactive des valeurs"""
    print("Entrez les valeurs de la serie statatistique,")
    print("r/remove pour suprimer la dernière valeur")
    print("ou q/quit pour quitter")
    serie = []
    while True:
        i = input(">")
        i = i.lower()
        if (i == 'q' or i == 'quit'):
            break
        if (i == 'r' or i == 'remove'):
            try:
                serie.pop()
            except IndexError:
                print("Erreur: liste vide")
        else:
            try:
                i = float(i)
            except ValueError:
                print("Erreur: merci d'entrez un nombre")
            else:
                serie.append()                    
    return serie


def user_choice(intro, *posibilites):
    print(intro)
    for index, value in enumerate(posibilites):
        print("{0}) {1}".format((index + 1), value))
    while True:
        choice = input(">")
        try:
            choice = int(choice)
            if (choice > len(posibilites) or choice < 1):
                raise IndexError
        except ValueError:
            print("Erreur: merci d'entrez un nombre")
        except IndexError:
            print("Erreur: merci de faire un choix valable")
        else:
            return choice
