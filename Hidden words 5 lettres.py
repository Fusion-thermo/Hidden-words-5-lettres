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
gris=(204,204,204)
vert=(134,190,153)
jaune=(244,202,122)
zone=1

#main
compteur=0
mouse = Controller()
sleep(2)
while compteur<2:
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
            sleep(0.2)
            #mouse.click(Button.left)
            #sleep(0.2)
        mouse.position = espace
        #sleep(0.2)
        #mouse.click(Button.left)
        #sleep(0.2)
        #vérification des couleurs
        im = ImageGrab.grab(bbox =(x0-zone,y0+(tentative-1)*80-zone,x0+5*80+zone,y0+(tentative-1)*80+zone))
        im.show()
        px=im.load()
        nombre_corrects=0
        print(1)
        for i in range(5):
            couleur=px[i*80,0]
            print(couleur)
            if couleur==gris:
                non.append(mot[i])
            elif couleur==vert:
                nombre_corrects+=1
                bonne_position[i]=mot[i]
            elif couleur==jaune:
                mauvaise_position[i]=mot[i]
            else:
                print("erreur")
        fini=True
        if nombre_corrects==5:
            fini=True
            break
        #trier les mots possibles
        for mot in liste_mots_actuelle:
            passer=False
            for lettre in non:
                if lettre in mot:
                    liste_mots_actuelle.remove(mot)
                    passer=True
                    break
            if passer:
                continue
            for indice in bonne_position.keys():
                if mot[indice] != bonne_position[indice]:
                    liste_mots_actuelle.remove(mot)
                    passer=True
                    break
            if passer:
                continue
            for indice in mauvaise_position.keys():
                if mot[indice] == mauvaise_position[indice]:
                    liste_mots_actuelle.remove(mot)
                    passer=True
                    break
                if mot.count(lettre) < [i for i in bonne_position.values()].count(lettre) + [i for i in bonne_position.values()].count(lettre):
                    liste_mots_actuelle.remove(mot)
                    passer=True
                    break





    
