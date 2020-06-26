from tkinter import *
from tkinter import ttk
from random import randint

root = Tk() # Notre Window
player = {"level": 10, "score": 0, 'NbLine': 0}

cheight = 700 # Hauteur de notre window
cwidth = 500 # Largeur de notre window 
root.title("Game Mike") # Title de la window
root.resizable(False, False) # Impossible de resize

canvas = Canvas(root, width = cwidth, height = cheight) # Création d'une canvas <body>
canvas.pack()

# 1 - 10 => 2
# 11 - 15 => 3
# 16 - 18 => 4
# 19 - 20 => 5
# Tout les 10 line level++

def generateBlock():
    global canvas, cheight, cwidth
    # Zone de depart de nos block
    positionDepartX = randint(0, 9)*35 # Random sur la longeur
    positionFinalX = positionDepartX + 35
    positionDepartY = 0
    positionFinalY = 35

    # Couleur de nos blocks    
    couleur = ["red", "green", "blue", "gray"]
    color = couleur[randint(0, 3)] # Choix de la couleur

    # Création d'un block dans la canvas
    forme = canvas.create_rectangle(positionDepartX,positionDepartY, positionFinalX,positionFinalY, fill=color, tags='block')

    for x in range(cheight): # Boucle permettant le défilement

        # Recuparation des coord. du block
        myForme = canvas.coords(forme)
        # Chercher un block en dessous
        prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3]) 
        if len(prevForme) > 1: # Si un block est bien en dessous
            break

        # Check si le block se trouve tout en bas
        if myForme[1] > (cheight-positionFinalY):
            print(myForme)
            break
        
        canvas.move(forme, 0, 1) #Deplacement du block


        def leftKey(event): # Click clavier gauche
            # Chercher un block sur la gauche
            prevForme = canvas.find_overlapping(myForme[0]-1,myForme[1],myForme[2]-1,myForme[3]) 
            if myForme[0] > 0 and len(prevForme) == 1: # Check si le block
               canvas.move(forme,-35, 0 ) 

        def rightKey(event): # Click clavier droit
            # Chercher un block sur la droit
            prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]+1,myForme[3])
            if myForme[0] < 315 and len(prevForme) == 1:
               canvas.move(forme,35, 0 )
        
        def downKey(event):
            if myForme[1] < 665:
                prevForme = canvas.find_overlapping(myForme[0]+1,myForme[1],myForme[2]-1,myForme[3]+25) 
                
                if (myForme[1] + 25) > 665 and len(prevForme) == 1:
                    canvas.move(forme,0, 665 - myForme[1] )
                elif len(prevForme) == 1:
                    canvas.move(forme,0, 25 )

            
        root.bind('<Left>', leftKey)
        root.bind('<Right>', rightKey)
        root.bind('<Down>', downKey)

        root.update()

    # Ligne probleme
    prevFormes = canvas.find_overlapping(0,666,315,700)
    print(prevFormes)
    if len(prevFormes) > 10:
        for theFormes in prevFormes:
            canvas.delete(theFormes)
        canvas.move('block', 0, 35)
    generateBlock()
    
def createdWindows():
    global canvas, cheight

    canvas.create_rectangle(350, 0, 500, cheight, fill= 'black')
    scoreText = canvas.create_text(390, 20, text="Score User: ", fill='white')
    scoreValeurText = canvas.create_text(465, 20, text="0pts", fill='white', font='bold')
    levelText = canvas.create_text(390, 50, text="Level User: ", fill='white')
    levelValeurText = canvas.create_text(465, 50, text="0", fill='white', font='bold') 
    generateBlock()

# canvas.itemconfig(levelValeurText, text = str(player['level']))

createdWindows()
root.mainloop()













