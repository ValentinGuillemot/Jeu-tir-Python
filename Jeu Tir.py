
from tkinter import*
import random
#*********************************************
def deplacer(event) :
    global vise
    coorb = can.coords(canon_central)
    coora = can.coords(canon_gauche)
    coorc = can.coords(canon_droit)
    l = len(tir)
    lc = can.coords(tir[l-1])
    if event.keysym == 'a' :
        if vise > 1 :
            vise += -1
        else :
            vise = 3
    if event.keysym == 'z' :
        if vise < 3 :
            vise += 1
        else :
            vise = 1
    if vise == 2 :
        signe_b = c.create_rectangle(205, 5, 250, 25, fill = 'green')
        signe_a = c.create_rectangle(55, 5, 100, 25, fill = 'gray')
        signe_c = c.create_rectangle(355, 5, 400, 25, fill = 'gray')
        if event.keysym == 'Left' and coorb[0] > 170 :
            can.move(canon_central, -5, 0)
        if event.keysym == 'Right' and coorb[2] < 325 :
            can.move(canon_central, 5, 0)
        if lc[1] < 250 :
            if event.keysym == 'space' and lc[1] < 250 :
                tir.append(can.create_rectangle(coorb[0]+10, 460, coorb[2]-10, 480, fill = 'yellow', outline = 'white'))
    if vise == 1 :
        signe_b = c.create_rectangle(205, 5, 250, 25, fill = 'gray')
        signe_a = c.create_rectangle(55, 5, 100, 25, fill = 'green')
        signe_c = c.create_rectangle(355, 5, 400, 25, fill = 'gray')
        if event.keysym == 'Left' and coora[0] > 5 :
            can.move(canon_gauche, -5, 0)
        if event.keysym == 'Right' and coora[2] < 160 :
            can.move(canon_gauche, 5, 0)
        if lc[1] < 250 :
            if event.keysym == 'space' and lc[1] < 250 :
                tir.append(can.create_rectangle(coora[0]+10, 460, coora[2]-10, 480, fill = 'yellow', outline = 'white'))
    if vise == 3 :
        signe_b = c.create_rectangle(205, 5, 250, 25, fill = 'gray')
        signe_a = c.create_rectangle(55, 5, 100, 25, fill = 'gray')
        signe_c = c.create_rectangle(355, 5, 400, 25, fill = 'green')
        if event.keysym == 'Left' and coorc[0] > 340 :
            can.move(canon_droit, -5, 0)
        if event.keysym == 'Right' and coorc[2] < 495 :
            can.move(canon_droit, 5, 0)
        if lc[1] < 250 :
            if event.keysym == 'space' and lc[1] < 250 :
                tir.append(can.create_rectangle(coorc[0]+10, 460, coorc[2]-10, 480, fill = 'yellow', outline = 'white'))

def jeu() :
    global tir, cible, partie
    bouton.config(state = DISABLED, text = 'En jeu...')
    a = 0
    l = len(tir)
    while a < l :
        can.move(tir[a], 0, -20)
        a += 1
    compteur = 0
    while compteur < 50 :
        impact(cibles[compteur])
        compteur += 1
    final = scorep + scoren
    if final == 50 and partie == True :
        print("Fin du jeu")
        partie = False
    can.after(60, jeu)


def impact(cible) :
    global tir, scorep, scoren
    can.move(cible, 0, 3)
    if cible != 0 :
        place_t = can.coords(cible)
    c = len(tir)
    l = c
    d = len(place_t)
    if c > 1 and d == 4 :
        if place_t[1] > 520 :
            barre.create_rectangle(490-10*scoren, -1, 500-10*scoren, 21, fill = 'firebrick2', outline = 'firebrick2')
            scoren += 1
            can.delete(cible)
        compteur_tir = 1
        while compteur_tir < l :
            cor = can.coords(tir[compteur_tir])
            if place_t[1] <= cor[1] and cor[1] <= place_t[3] :
                if place_t[0] <= cor[0]+5 and cor[0]+5 <= place_t[2] :
                    can.delete(cible)
                    can.move(tir[compteur_tir], 500, -100)
                    barre.create_rectangle(10*scorep, -1, 10*scorep+10, 21, fill = 'yellow', outline = 'yellow')
                    scorep += 1
            compteur_tir += 1

    


#*********************************************
vise = 2
partie = True

fenetre = Tk()
fenetre.geometry("500x650+150+30")
fenetre.title("Canon test")
fenetre.bind('<KeyPress>', deplacer)

can = Canvas(fenetre, width = 500, height = 520, bg = 'cornflower blue')
can.pack(side = TOP)
canon_central = can.create_rectangle(235, 470, 265, 520, fill = 'pink', outline = 'violet red')
can.create_rectangle(163, 500, 169, 525, fill = 'white', outline = 'cornflower blue')
canon_gauche = can.create_rectangle(85, 470, 115, 520, fill = 'pink', outline = 'violet red')
can.create_rectangle(329, 500, 336, 525, fill = 'white', outline = 'cornflower blue')
canon_droit = can.create_rectangle(385, 470, 415, 520, fill = 'pink', outline = 'violet red')
tir = []
tir.append(can.create_rectangle(245, -470, 255, -450, fill = 'yellow', outline = 'white'))
cibles = []
cible = can.create_oval(230, -35, 255, -10, fill = 'firebrick2')
cibles.append(cible)
compteur = 0
while compteur < 50 :
    y = random.randint(1, 3)
    if y == 1 :
        x = random.randint(5, 100)
    if y == 2 :
        x = random.randint(170, 265)
    if y == 3 :
        x = random.randint(340, 410)
    cibles.append(can.create_oval(x, compteur*-50-25, x+25, compteur*-50, fill = 'firebrick2'))
    compteur += 1
cible_b = can.create_oval(70, -50, 95, -25, fill = 'firebrick2')
cibles.append(cible_b)

c = Canvas(fenetre, width = 450, height = 30, bg = 'white')
c.pack(side = TOP)
signe_b = c.create_rectangle(205, 5, 250, 25, fill = 'green')
signe_a = c.create_rectangle(55, 5, 100, 25, fill = 'gray')
signe_c = c.create_rectangle(355, 5, 400, 25, fill = 'gray')


bouton = Button(fenetre, text = 'Commencer', command = jeu)
bouton.pack(side = TOP, pady = 10)
barre = Canvas(fenetre, width = 500, height = 20, bg = 'cornflower blue')
barre.pack(side = TOP)
scorep = 0
scoren = 0

fenetre.mainloop
