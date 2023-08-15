from PIL import Image, ImageGrab
import numpy as np
from time import sleep,time
import pyautogui #for absolutely no apparent reason removing this breaks the program, the positioning doesn't go where it is supposed to go.
from pynput.mouse import Button, Controller

with open("C:/Users/jeanb/OneDrive/Documents/Python/Applications mobiles avec scrpy/Hidden-words-5-lettres/Mots 5 lettres triés.txt","r") as fichier:
    dico=fichier.read()
liste_mots=eval(dico)

#Plus nécessaire maintenant que la liste est triée
with open("C:/Users/jeanb/OneDrive/Documents/Python/Applications mobiles avec scrpy/Hidden-words-5-lettres/Occurences lettres.txt","r") as fichier:
    dico=fichier.read()
dico_lettres=eval(dico)
""" 
def tri_mots(mot):
    mot=mot.lower()
    lettres=[]
    for i in mot:
        if i not in lettres :
            lettres.append(i)
    valeur=len(lettres)*1000
    for lettre in lettres:
        valeur+=dico_lettres[lettre]
    return valeur """

pos_alphabet={'a': (1016,1213), 'z': (1094,1213), 'e': (1172,1213), 'r': (1250,1213), 't': (1328,1213), 'y': (1406,1213), 'u': (1484,1213), 'i': (1562,1213), 'o': (1640,1213), 'p': 
(1716,1213), 'q': (1016,1316), 's': (1094,1316), 'd': (1172,1316), 'f': (1250,1316), 'g': (1328,1316), 'h': (1406,1316), 'j': (1484,1316), 'k': (1562,1316), 'l': (1640,1316), 
'm': (1718,1316), 'w': (1082,1426), 'x': (1197,1426), 'c': (1312,1426), 'v': (1427,1426), 'b': (1542,1426), 'n': (1657,1426)}
espace=(1375,1529)
x0,y0 = 1141,332
gris=(205,205,205)
vert=(134, 190, 153)
jaune=(244,203,123)
zone=1
delai=0.2

def bonne_couleur(mesure, reference, ecart_admissible):
    correct=True
    for i in range(3):
        if abs(mesure[i]-reference[i]) >= ecart_admissible*reference[i]:
            correct=False
    return correct
    
#main
compteur=0
mouse = Controller()
sleep(2)
while compteur<10:
    compteur+=1

    tentative=0
    fini=False
    liste_mots_actuelle=liste_mots[:]
    non=[]#gris
    bonne_position={}#vert
    mauvaise_position={}#jaune

    while not fini:
        tentative+=1
        #écriture mot le mieux classé
        mot=liste_mots_actuelle[0]
        for lettre in mot:
            mouse.position = pos_alphabet[lettre]
            sleep(delai)
            mouse.click(Button.left)
            sleep(delai)
        mouse.position = espace
        sleep(delai)
        mouse.click(Button.left)
        sleep(2)
        #vérification des couleurs
        im = ImageGrab.grab(bbox =(x0-zone,y0+(tentative-1)*100-zone,x0+4*100+zone,y0+(tentative-1)*100+zone))
        #im.show()
        px=im.load()
        nombre_corrects=0
        print(tentative)
        for i in range(5):
            couleur=px[i*100,0]
            #print(couleur)
            if bonne_couleur(couleur,gris,0.05):
                non.append(mot[i])
            elif bonne_couleur(couleur,vert,0.05):
                nombre_corrects+=1
                bonne_position[i]=mot[i]
            elif bonne_couleur(couleur,jaune,0.05):
                mauvaise_position[i]=mot[i]
            else:
                print("erreur",couleur, i)
        print(non,bonne_position,mauvaise_position)
        if nombre_corrects==5 or tentative>6:
            fini=True
            break
        new_liste=[]
        #trier les mots possibles
        for mot in liste_mots_actuelle:
            passer=False
            for lettre in non:
                if lettre in mot:
                    #print("non",mot)
                    passer=True
                    break
            if passer:
                continue
            for indice in bonne_position.keys():
                if mot[indice] != bonne_position[indice]:
                    #print("oui",mot)
                    passer=True
                    break
            if passer:
                continue
            for indice in mauvaise_position.keys():
                if mot[indice] == mauvaise_position[indice]:
                    #print("nsp",mot)
                    passer=True
                    break
                if mot.count(lettre) < [i for i in bonne_position.values()].count(lettre) + [i for i in bonne_position.values()].count(lettre):
                    #print("nsp",mot)
                    passer=True
                    break
            if passer:
                continue
            new_liste.append(mot)
        liste_mots_actuelle=new_liste[:]
        print(liste_mots_actuelle[:10],len(liste_mots_actuelle))
    #premier clic pour lorsqu'on gagne deuxième pour lorsqu'on perd    
    sleep(4)
    mouse.position = (1512,1416)
    sleep(delai)
    mouse.click(Button.left)
    sleep(0.2)
    mouse.position = (1349,1249)
    sleep(0.2)
    mouse.click(Button.left)
    #vérifions si on a perdu ou gagné
    # x,y=1512,1416
    # zone2=3
    # im = ImageGrab.grab(bbox =(x-zone2,y-zone2,x+zone2,y+zone2))
    # im.show()
    # px=im.load()
    
    # couleur=px[zone2,zone2]
    # #print(couleur)
    # if bonne_couleur(couleur,(239,177,73),0.1):
    #     #bouton niveau suivant
    #     print(1111)
    #     sleep(4)
    #     mouse.position = (x,y)
    #     #sleep(delai)
    #     #mouse.click(Button.left)
    # else:
    #     #bouton passer
    #     sleep(5)
    #     mouse.position = (1349,1249)
    #     #sleep(delai)
    #     #mouse.click(Button.left)
    #avant le début du jeu
    sleep(1)





    
