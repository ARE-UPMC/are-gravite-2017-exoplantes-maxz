# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:18:31 2017

@author: 3525842
"""

from tkinter import *
from math import*

def Cercle(x,y,r,couleur):
    """ Dessine un cercle de centre (x,y) de rayon r et d'une couleur définie"""

    Canevas.create_oval(x-r, y-r, x+r, y+r, outline=couleur, fill=couleur)
def mouvement():
    global t
    t=t+0.2
    
    #mouvement de l'étoile    
    
    Canevas.coords(etoile,(xc-rs)+distancecme*sin(t),(yc-rs)+distancecme*cos(t),(xc+rs)+distancecme*sin(t),(yc+rs)+distancecme*cos(t))
    
    #mouvement de la planète  
     
    Canevas.coords(planete,(xc-rp)+distancecmp*sin(t),(yc-rp)+distancecmp*cos(t),(xc+rp)+distancecmp*sin(t),(yc+rp)+distancecmp*cos(t))
   
    
    Mafenetre.after(230,mouvement)
    
    
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("rotation d'une étoile et d'une planète autour d'un centre de masse")
global xs,ys,rs,xp,yp,rp,xc,yc,rc,R,t,a
t=0    

#coordonnées du milieu de centre de masse
xc=500
yc=500
rc=5 #son rayon
#coordonées du centre de l'étoile
xs=550
ys=550
rs=50 #son rayon
#coordonnées de la planète
xp=200
yp=200
rp=20

#Distance du centre de masse
distancecme= sqrt((xs-xc)**2+(ys-yc)**2)
distancecmp=sqrt((xp-xc)**2+(yp-yc)**2)

# Création d'un widget Canvas (zone graphique)
Largeur = 1000
Hauteur = 1000
Canevas= Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white',bd=8,relief="ridge")
Canevas.pack()
centre_de_masse=Cercle(xc,yc,rc,"black")
etoile=Canevas.create_oval(xs-rs,ys-rs,xs+rs,ys+rs,fill="yellow")
planete=Canevas.create_oval(xp-rp,yp-rp,xp+rp,yp+rp,fill="red")
mouvement()
Mafenetre.mainloop()