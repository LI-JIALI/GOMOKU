
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
#tkinter,messagebox fournit un assortiment de fenêtres de dialogue pour des tâches simples

BLACK = True    #Ici on juge qui jouera aux échecs en premier
END = False     #Ici on juge si le jeu est terminé


longueur = 15     #L'Échiquier de taille 15x15

echiquier = [[0 for i in range(0,longueur+1)] for j in range(0,longueur+1)] #Nous sauvegardons l'échiquier dans un tableau à deux dimensions
decalage = [(1, 0), (0, 1), (1, 1), (1, -1)]  #La direction du décalage

root = tkinter.Tk()  #Créer un cadre
root.geometry('530x510') #Définir la taille
root.title("GOMOKU")    #Définir le titre
top = Canvas(root,height = 500,width = 500,bg='#D5B092')  #Définir les propriétés de la fenêtre

def gagnant(): 
    #Afficher les info des gagnantes
    #Cette fonction est appelée par verifieGagnant, vérifiez l'état d'échec NOIR à ce moment afin de savoir le gagnant
    global END  
    msg = "LE NOIR GAGNE!" if BLACK else "LE BLANC GAGNE!"  #Afficher les informations gagnantes
    tkinter.messagebox.showinfo("LE JEU EST TERMINÉ",msg) #La boîte de dialogue apparaît

def verifieMatchNul(): #Vérifiez si les deux ont fait partie nulle
    for x in range(1,longueur+1): 
        for y in range(1,longueur+1):
            if echiquier[x][y] == 0:   #S'il y a des places qui n'a pas été placée, le plateau n'est pas plein
                return False    #Renvoie False, les deux n'ont pas fait de partie nulle

    #D'ici，les deux ont fait partie nulle
    tkinter.messagebox.showinfo("LE JEU EST TERMINÉ",msg) #La boîte de dialogue apparaît
    global END
    END = True
    return True 

def resCompteDirection( point_x,point_y,valeur, x_decalage, y_decalage):    #Voir la pièce d'échecs qui vient d'être jouée qui connectée dans une certaine direction
    compter = 1   
    for etaoe in range(1, 5):    # Vérifie quatre unités dans le sens positif du décalage actuel
        x = point_x + etaoe * x_decalage  # Calcule la valeur de x 
        y = point_y + etaoe * y_decalage  # Calcule la valeur de y
        if 0 < x <= longueur and 0 < y <= longueur and echiquier[x][y] == valeur:  #Vérifiez s'il est hors frontière et si les échecs sont de la même couleur         
            compter += 1  #Si oui, compte +1
        else:
            break   #Si la pièce d'échecs est hors frontières ou si la couleur est différente, sautez de la boucle

    for etaoe in range(1, 5): # Vérifiez quatre unités dans la direction opposée du décalage actuel
        x = point_x - etaoe * x_decalage 
        y = point_y - etaoe * y_decalage
        if 0 < x <= longueur and 0 < y <= longueur and echiquier[x][y] == valeur:
            compter += 1
        else:
            break

    return compter >= 5  #Vérifie si 5 pièces sont connectées dans une ligne, puis retourne une valeur booléenne

def verifieGagne(valeur,point_x,point_y): 
    for dir in decalage:  
        if resCompteDirection(point_x,point_y, valeur, dir[0], dir[1]):
           #Si la condition If est remplie, le jeu est terminé
            gagnant()    

def echec (evenement): # Cette fonction est liée par tkinter et transmet les événements utilisateur à cette fonction
    #30 pixels par grille
    evenement.x = evenement.x//30+1 if (evenement.x %30 > 15) else evenement.x//30
    evenement.y = evenement.y//30+1 if (evenement.y %30 > 15) else evenement.y//30

    evenement.x  = min(evenement.x,longueur)
    evenement.x  = max(1,evenement.x)
    evenement.y  = min(evenement.y,longueur)
    evenement.y  = max(1,evenement.y)


    gauche = evenement.x * 30 - 13
    droit = evenement.x * 30 + 13
    haut = evenement.y * 30 - 13
    bas = evenement.y * 30 + 13

    global BLACK    #Variable globale, utilisées pour vérifier qui joue aux échecs
    global echiquier   
    if (END == False) : 
        if echiquier[evenement.x][evenement.y] == 0:   #Ce point est vide et peut être placé
            couleur = 'BLACK' if BLACK else 'WHITE'   #Définir la couleur d'échec
            echec_valeur = 1 if BLACK else 2    #Définissez la valeur de l'échec dans le tableau à deux dimensions

            top.create_oval(gauche,haut,droit,bas,fill = couleur,tag ='echec')   #Dessiner des pièces d'échecs
            echiquier[evenement.x][evenement.y] = echec_valeur #Enregistrer dans un tableau à deux dimensions
            verifieMatchNul()    #Vérifiez si les deux ont fait partie nulle
            verifieGagne(echec_valeur,evenement.x,evenement.y)  #Vérifiez si cette pièce est connectée aux 4 pièces environnantes

            BLACK = False if BLACK else True  


def main():
    
    top.pack(expand=YES, fill=BOTH) #Exécuter les propriétés de la fenêtre
    top.bind("<Button-1>",echec)    #Liant la fonction echec, un événement bouton-1 (clic gauche de la souris) se produit, indiquant que l'utilisateur est dans la position

    for cnt in range(1,longueur+1):   
        top.create_line(30,cnt*30,450,cnt*30,width = 2) #Tracez des lignes horizontales
        top.create_line(cnt*30,30,cnt*30,450,width = 2) #Tracez des lignes verticale
        #30 est l'intervalle entre deux points, chaque ligne / colonne a 15 points 450 = 30 * 15
        #create_line (coordonnée x du premier point, coordonnée y du premier point, coordonnée x du deuxième point, coordonnée y du deuxième point)

    root.mainloop() #Exécuter toute la fonction

if __name__ == "__main__":
    main() #Appel la fonction main
