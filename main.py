import CalculTheorique
import tkinter as tk
#====================================================================
#création du background
#donner les tailles de la page 
#====================================================================
couleur_bg = "#23272a"
couleur_interface = "#2c2f33"
root = tk.Tk()
root.title("fonction tri")
root.minsize(width=700,height=950)
root.config(bg=couleur_bg)

#====================================================================
#bouton pour lancer le calcul
#lance la comparaison de temps
#temps comparait en minute
#====================================================================
fenetre_du_programme = tk.LabelFrame(root,width=700,height=950,bg=couleur_bg,borderwidth=0)
fenetre_du_programme.pack()
temps_theorique = {"Tri par max":0,"Tri à bulle":0,"Tri par fusion":0,
                    "Tri par insertion 1":0,"Tri par insertion 4":0}

nom_des_fonction = ["Tri par max","Tri à bulle","Tri par fusion",
    "Tri par insertion 1","Tri par insertion 4"]

def lance_le_calcul():

    valeur_de_taille_liste = selection_valeur()
    valeur_de_taille_liste = int(valeur_de_taille_liste)
    
    
    valeur_de_taille_liste = selection_valeur()
    valeur_de_taille_liste = int(valeur_de_taille_liste)
    for i in nom_des_fonction:
        if sur_la_piste[i]==True:
            temps_theorique[i]=CalculTheorique.temps_theorique(i,valeur_de_taille_liste)
            temps_converti = converti_le_temps(temps_theorique[i])
            print("="*70,"\n","Le temps de ",i,"est de :",temps_converti[0],
                temps_converti[1],temps_converti[2],temps_converti[3])
    voiture()
    classement_temps()
# affiche le bouton principale qui lance le programme 

cadre_titre = tk.LabelFrame(fenetre_du_programme,text="ALLER",bg=couleur_interface,fg="white")
cadre_titre.place(x=250,y=0,width=100,height=50)

titre_principale = tk.Button(cadre_titre,padx=40,pady=5,command=lance_le_calcul)
titre_principale.config(text="COURSE")
titre_principale.pack()

#=====================================================================
# affiche le niveau de temps 
# fonction par fonction 
#=====================================================================

# langue pris par défault est le français 

langue_choisie = {"langue":"Français"}

uniter_traduit = {" moins de 1 ":"less than 1","":""," seconde ":" second "," secondes ":" seconds ",
" minutes ":" minutes "," heures ":" hours "," jours ":" days ",
" mois ":" month "," années ":" years ","Tri par max":"Sort by max","Tri à bulle":"Bubble sorting ","Tri par fusion":"Sort by fusion"
,"Tri par insertion 1":"Insertion sort 1","Tri par insertion 4":"Insertion sort 4"}

etat_passage = {"passage":False}
def classement_temps():
    etat_passage["passage"]=True
    cadre_classement = tk.LabelFrame(piste_de_course)
    cadre_classement.grid_propagate(False)
    cadre_classement.config(height=110,width=500,bg=couleur_bg,fg="white")
    nom_des_fonction = ["Tri par max","Tri à bulle","Tri par fusion",
    "Tri par insertion 1","Tri par insertion 4"]
    for i in nom_des_fonction:
        if sur_la_piste[i] == True:
            comparaison_des_temps(i)
            temps_converti = converti_le_temps(temps_theorique[i])
            gros_temps = temps_converti[0]
            uniter_première = temps_converti[1]
            petit_temps = temps_converti[2]
            uniter_seconde = temps_converti[3]
            nom_des_fonction = i
            phrase = tk.StringVar()
            if langue_choisie["langue"]=="Français":
                message = (f"Le temps avec la fonction {nom_des_fonction} vous prendras : {gros_temps}{uniter_première}{petit_temps}{uniter_seconde} ")
            else:
                uniter_première = uniter_traduit[uniter_première]
                uniter_seconde = uniter_traduit[uniter_seconde]
                nom_des_fonction = uniter_traduit[i]
                message = (f"The time with the fuction {nom_des_fonction} will take you : {gros_temps}{uniter_première}{petit_temps}{uniter_seconde} ")
            phrase.set(message)
            emplacement_message = tk.Label(cadre_classement,textvariable=phrase,bg=couleur_bg,fg="white")
            emplacement_message.grid(column=0,row=classement_des_temps[i])
    cadre_classement.grid(column=0,row=6,columnspan=2)

#============================================================
# prend en entrer le temps 
#puis le convertie en s / min / h / j / mois / années
#============================================================
def converti_le_temps(temps):
    if temps > 1:
        if temps > 60:
            # minute
            if temps > 3600:
                # heure
                if temps > 86400:
                    # jours
                    if temps > 2_592_000:
                        # mois 
                        if temps > 31_104_000:
                            #années
                            temps = (int(temps //31_104_000)," années ",(int(temps % 31_104_000)//2_592_000)," mois ")
                        else:
                            temps = (int(temps //2_592_000)," mois ",(int(temps%2_592_000)//86400)," jours ")
                    else:
                        temps = (int(temps//86400)," jours ",(int(temps%86400)//3600)," heures ")
                else:
                    temps = (int(temps//3600)," heures ",(int(temps%3600)//60)," minutes ")
            else:
                temps = (int(temps//60)," minutes ",int(temps%60)," secondes ")
        else:
            temps = (temps," secondes ","","")
    else:
        temps = (" moins de 1 "," seconde ","","")
    return(temps)



#=========================================================
# fonction help va guider et accompagner l'utilisateur 
# s'il le veut pour le bon fonctionnement de la procédure
#=========================================================
def langue_français():
    langue_choisie["langue"] = "Français"
    # affiche le bouton principale qui lance le programme 
    cadre_titre.config(text="Aller")
    titre_principale.config(text="Course")
    # cadre des langues
    cadre_bouton_drapeau.config(text="Langue")
    # cadre fonction de tri 
    cadre_fonction_tri.config(text="Fonction de Tri")
    # Les différentes fonction de tri
    checkbutton_0.config(text="Tri par Max")
    checkbutton_1.config(text="Tri à Bulle")
    checkbutton_2.config(text="Tri Fusion")
    checkbutton_3.config(text="Tri par insertion 1")
    checkbutton_4.config(text="Tri par insertion 4")
    # bouton pour placer les voitures sur la piste 
    en_piste.config(text="En piste")
    # Point info
    liste_fonction = ["Tri par max","Tri à bulle","Tri par fusion",
    "Tri par insertion 1","Tri par insertion 4"]
    point_info2(liste_fonction)
    cadre_information_fonction.config(text="Tu veux plus d’information ?")

    # selection du nombre de valeur inscrit dans la liste 
    cadre_nb_valeur.config(text="Entrer le nombre de valeur que vous voulez tester :")

    langue(langue_choisie["langue"])
    if etat_passage["passage"]==True:
        classement_temps()

def langue_anglais():
    langue_choisie["langue"] = "Anglais"
    # affiche le bouton principale qui lance le programme 
    cadre_titre.config(text="Start")
    # bouton qui lance le programme 
    titre_principale.config(text="Go")
    # cadre des langues
    cadre_bouton_drapeau.config(text="Language")
    # cadre fonction de tri 
    cadre_fonction_tri.config(text="Sort of fonction")
    # Les différentes fonction de tri
    checkbutton_0.config(text="Sort by Max")
    checkbutton_1.config(text="Bubble sorting")
    checkbutton_2.config(text="Sort by Fusion")
    checkbutton_3.config(text="Insertion sort 1")
    checkbutton_4.config(text="Insertion sort 4")
    # bouton pour placer les voitures sur la piste 
    en_piste.config(text="On track")
    # Point info 
    liste_fonction = ["Sort by Max","Bubble sorting","Sort by Fusion",
    "Insertion sort 1","Insertion sort 4"]
    point_info2(liste_fonction)
    cadre_information_fonction.config(text="Wanna know more ? ")

    # selection du nombre de valeur inscrit dans la liste 
    cadre_nb_valeur.config(text="Enter the number of values you want to test")
    # affichage du temps de différentes fonction
    langue(langue_choisie["langue"])
    if etat_passage["passage"]==True:
        classement_temps()


def langue(langue):
    print("bonjour vous avez choisie la langue : ", langue)
    return langue

# emplacement des langues 
cadre_bouton_drapeau = tk.LabelFrame(fenetre_du_programme,text="Langue",bg=couleur_interface,fg="white")
cadre_bouton_drapeau.place(x=580,y=10,width=120,height=60)

# drapeau français
image_drapeau_français = 'image/drapeau/drapeau_français.png'
drapeau_français = tk.PhotoImage(file=image_drapeau_français)
bouton_français = tk.Button(cadre_bouton_drapeau,command=langue_français,width=50,height=30,image=drapeau_français,bg="white")
bouton_français.grid(column=0,row=0)

# drapeau anglais
image_drapeau_anglais = 'image/drapeau/drapeau_anglais.png'
drapeau_anglais = tk.PhotoImage(file=image_drapeau_anglais)
bouton_anglais = tk.Button(cadre_bouton_drapeau,command=langue_anglais,width=50,height=30,image=drapeau_anglais,bg="white")
bouton_anglais.grid(column=1,row=0)

#====================================================================
# l'utilisateur doit choisir quelle fonction vont être comparer et utiliser
#====================================================================
sur_la_piste = {"Tri par max":False,"Tri à bulle":False,
                "Tri par fusion":False,"Tri par insertion 1":False,"Tri par insertion 4":False}
def choix_fonction():
    if expression_0.get():
        sur_la_piste["Tri par max"] = True
    if not expression_0.get():
        sur_la_piste["Tri par max"] = False
    if expression_1.get():
        sur_la_piste["Tri à bulle"] = True
    if not expression_1.get():
        sur_la_piste["Tri à bulle"] = False
    if expression_2.get():
        sur_la_piste["Tri par fusion"] = True
    if not expression_2.get():
        sur_la_piste["Tri par fusion"] = False
    if expression_3.get():
        sur_la_piste["Tri par insertion 1"] = True
    if not expression_3.get():
        sur_la_piste["Tri par insertion 1"] = False
    if expression_4.get():
        sur_la_piste["Tri par insertion 4"] = True
    if not expression_4.get():
        sur_la_piste["Tri par insertion 4"] = False



cadre_fonction_tri = tk.LabelFrame(fenetre_du_programme,text= "fonction de tri",padx=40,pady=30,
                                   bg=couleur_interface,fg='white')
cadre_fonction_tri.place(x=25,y=80,width=180,height=250)

expression_0 = tk.IntVar()
expression_1 = tk.IntVar()
expression_2 = tk.IntVar()
expression_3 = tk.IntVar()
expression_4 = tk.IntVar()

checkbutton_0 = tk.Checkbutton(cadre_fonction_tri, text="Tri par max",
                                variable=expression_0, command=choix_fonction)
checkbutton_0.place(x=-30,y=-20)
checkbutton_1 = tk.Checkbutton(cadre_fonction_tri, text="Tri à bulle",
                                variable=expression_1, command=choix_fonction)
checkbutton_1.place(x=-30,y=10)
checkbutton_2 = tk.Checkbutton(cadre_fonction_tri, text="Tri par fusion",
                                variable=expression_2, command=choix_fonction)
checkbutton_2.place(x=-30,y= 40)
checkbutton_3 = tk.Checkbutton(cadre_fonction_tri, text="Tri par insertion 1",
                                variable=expression_3, command=choix_fonction)
checkbutton_3.place(x=-30,y=70)
checkbutton_4 = tk.Checkbutton(cadre_fonction_tri, text="Tri par insertion 4",
                                variable=expression_4, command=choix_fonction)
checkbutton_4.place(x=-30,y=100)


#====================================================================
# information sur les fonctions
#====================================================================

def point_info(event):
    choix = list_info.get(list_info.curselection())
    print("point information",choix)
    text_info_fonction(choix)

cadre_information_fonction = tk.LabelFrame(fenetre_du_programme,text="Point info",
                    padx=5, pady=10,bg=couleur_interface,fg="white")
cadre_information_fonction.place(x=220,y=80,width=150,height=130)

list_info = tk.Listbox(cadre_information_fonction,height=5)

def point_info2(fonction_info):
    for item in fonction_info:
        list_info.insert(fonction_info.index(item),item)
    list_info.bind("<<ListboxSelect>>",point_info)
    list_info.grid(column=0,row=0)


#===================================================================
# affichage des informations sur les fonctions 
#===================================================================
explication = {"Tri par max":"Le tri par max est un algorithme récursif permettant de trier une liste \n en recherchant d’abord la valeur maximale.\n Puis la place en fin de liste dans l’ordre croissant.\n On continue en s’arrêtant avant la dernière valeur \n car nous savons qu’elle est la valeur minimale.\n Enfin, on retourne la même liste triée. ",
"Tri à bulle":"Le tri à Bulle est un algorithme récursif qui compare deux éléments consécutifs\n dans le mauvais ordre. Une fois la comparaison faite,\n la valeur la plus importante arrive à droite. \n Puis on ne recommence en ne prenant pas\n compte du dernier élément permuté (à droite) pour arriver à une liste triée.",
"Tri par fusion":"Le tri à fusion est un algorithme de tri qui fonctionne de façon récursive qui\n permet de comparer deux listes sans pour autant les modifier\n dans les paramètres. A la fin,\n il renvoi une liste fusionnée en conservant l’ordre croissant ",
"Tri par insertion 1":"Le tri par insertion 1 permet à partir d’une sous liste triée de p éléments,\n on construit une liste triée de (p+1) éléments en insérant l’élément\nsuivant à la bonne place. On part ensuite d’une sous liste composée d’un seul\n élément et on y ajoute un par un les autres éléments de la liste. \n Cette fonction retourne la liste triée.",
"Tri par insertion 4":"Le tri par insertion 4 est largement plus rapide que le tri par insertion 1.\n Il fonctionne aussi à partir d’une sous liste composée d’un seul élément\n et on y ajoute un par un les autres éléments de la liste.\n La place de l’insertion est déterminée par dichotomie,\n soit coupé en deux à chaque étape. \n Cette fonction retourne la liste triée ",
"Sort by Max":"Sorting by max is a recursive algorithm for sorting a list \n by first finding the maximum value.\n Then places it at the end of the list in ascending order.\n We continue by stopping before the last value \n because we know it is the minimum value.\n Finally, we return the same sorted list.",
"Bubble sorting":"Bubble sort is a recursive algorithm that compares two consecutive items\n in the wrong order. After the comparison is done,\n the most important value comes to the right. \n Then we start again, ignoring\n the last permuted element (on the right) to arrive at a sorted list.",
"Sort by Fusion":"Merge sort is a sorting algorithm that works recursively that\n compares two lists without modifying them\n in the parameters. At the end,\n it returns a merged list in ascending order",
"Insertion sort 1":"The sort by insertion 1 allows from a sorted sublist of p elements,\n we build a sorted list of (p+1) elements by inserting the next element\nin the right place. We then start from a sub-list composed of a single\n element and we add the other elements of the list one by one. \n This function returns the sorted list.",
"Insertion sort 4":"Insertion sort 4 is much faster than insertion sort 1.\n It also works from a sublist composed of a single element\n and the other elements of the list are added to it one by one. \n Place of insertion is determined by dichotomy,\n being cut in half at each step.\n This function returns the sorted list"}
def text_info_fonction(fonction_à_expliquer):
    emplacement_explication = tk.LabelFrame(fenetre_du_programme,bg=couleur_interface,fg="white")
    emplacement_explication.place(x=220,y=230,height=100,width=430)
    text=tk.StringVar()
    message1 = (explication[fonction_à_expliquer])
    text.set(message1)
    emplacement_text = tk.Label(emplacement_explication,textvariable=text,bg=couleur_interface,fg="white")
    emplacement_text.pack()

#====================================================================
# valeur de teste 
# ex: taille de liste vaut entre 1 et 9999
#====================================================================

cadre_nb_valeur = tk.LabelFrame(fenetre_du_programme, text="Entrer le nombre de valeur que vous voulez tester :",
                                padx=5,pady=15,bg=couleur_interface,fg='white')
cadre_nb_valeur.place(x=390,y=80,width=280,height=75)

def selection_valeur():
    valeur_de_taille_liste = val_select.get()
    return valeur_de_taille_liste

val_select = tk.Spinbox(cadre_nb_valeur,command=selection_valeur)
val_select.pack()


#====================================================================
# route ou l'on ajoute un voiture par fonction
#====================================================================
piste_de_course = tk.LabelFrame(fenetre_du_programme,bg=couleur_bg,bd=1)

# route
fichier_route = 'image/route/route.png' 
route = tk.PhotoImage(file=fichier_route)

# voiture max
voiture_max = 'image/voiture/voiture_max.png'
photo_max = tk.PhotoImage(file=voiture_max)
Label_max = tk.Label(piste_de_course, image=photo_max)
route_max = tk.LabelFrame(piste_de_course,width=415,height=83,bg="black",bd=0)
Label_route_max = tk.Label(piste_de_course,image=route,bd=0)

# voiture bulle
voiture_bulle = 'image/voiture/voiture_bulle.png'
photo_bulle = tk.PhotoImage(file=voiture_bulle)
Label_bulle = tk.Label(piste_de_course, image=photo_bulle)
route_bulle = tk.LabelFrame(piste_de_course,width=415,height=83,bg="pink",bd=0)
Label_route_bulle = tk.Label(piste_de_course,image=route,bd=0)

# voiture fusion
voiture_fusion = 'image/voiture/voiture_fusion.png'
photo_fusion = tk.PhotoImage(file=voiture_fusion)
Label_fusion = tk.Label(piste_de_course, image=photo_fusion)
route_fusion = tk.LabelFrame(piste_de_course,width=415,height=83,bg="orange",bd=0)
Label_route_fusion = tk.Label(piste_de_course,image=route,bd=0)

# voiture insertion_1
voiture_insertion_1 = 'image/voiture/voiture_insertion_1.png'
photo_insertion_1 = tk.PhotoImage(file=voiture_insertion_1)
Label_insertion_1 = tk.Label(piste_de_course, image=photo_insertion_1)
route_insertion_1 = tk.LabelFrame(piste_de_course,width=415,height=83,bg="blue",bd=0)
Label_route_insertion_1 = tk.Label(piste_de_course,image=route,bd=0)

# voiture insertion_4
voiture_insertion_4 = 'image/voiture/voiture_insertion_4.png'
photo_insertion_4 = tk.PhotoImage(file=voiture_insertion_4)
Label_insertion_4 = tk.Label(piste_de_course, image=photo_insertion_4)
route_insertion_4 = tk.LabelFrame(piste_de_course,width=415,height=83,bg="white",bd=0)
Label_route_insertion_4 = tk.Label(piste_de_course,image=route,bd=0)

# coupe numéro 1
fichier_coupe_1 = 'image/coupe/coupe_1.png'
coupe_1 = tk.PhotoImage(file=fichier_coupe_1)
Label_coupe_1 = tk.Label(piste_de_course,image=coupe_1)


# coupe numéro 2
fichier_coupe_2 = 'image/coupe/coupe_2.png'
coupe_2 = tk.PhotoImage(file=fichier_coupe_2)
Label_coupe_2 = tk.Label(piste_de_course,image=coupe_2)

# coupe numéro 3
fichier_coupe_3 = 'image/coupe/coupe_3.png'
coupe_3 = tk.PhotoImage(file=fichier_coupe_3)
Label_coupe_3 = tk.Label(piste_de_course,image=coupe_3)

# coupe 4 
fichier_coupe_4 = 'image/coupe/coupe_4.png'
coupe_4 = tk.PhotoImage(file=fichier_coupe_4)
Label_coupe_4 = tk.Label(piste_de_course,image=coupe_4)

fichier_coupe_5 = 'image/coupe/coupe_5.png'
coupe_5 = tk.PhotoImage(file=fichier_coupe_5)
Label_coupe_5 = tk.Label(piste_de_course,image=coupe_5)

classement_des_temps = {"Tri par max":0,"Tri à bulle":0,"Tri par fusion":0,
                    "Tri par insertion 1":0,"Tri par insertion 4":0}

# compare les temps des fonctions puis renvoie le classement


def comparaison_des_temps(fonction):
    liste_fonction_active = []
    place = 0
    for i in nom_des_fonction:
        if sur_la_piste[i] == True:
            liste_fonction_active.append(i)
    for i in liste_fonction_active:
        if temps_theorique[fonction]>=temps_theorique[i]:
            place = place + 1
    classement_des_temps[fonction] = place


def voiture():
    Label = [Label_max,Label_bulle,Label_fusion,Label_insertion_1,Label_insertion_4]
    Label_route = [Label_route_max,Label_route_bulle,Label_route_fusion,Label_route_insertion_1,Label_route_insertion_4]
    Label_coupe = [Label_coupe_1,Label_coupe_2,Label_coupe_3,Label_coupe_4,Label_coupe_5]
    x = 0
    y=4
    for i in nom_des_fonction :
        if sur_la_piste[i]==True:
            comparaison_des_temps(i)
            print(i)
            Label[x].grid(column=0,row=classement_des_temps[i])
            Label_route[x].grid(column=1,row=classement_des_temps[i])
            Label_coupe[classement_des_temps[i]-1].grid(column=2,row=classement_des_temps[i])
            print("="*70,"\n","la place de ",i," est : ",classement_des_temps[i])
        else:
            Label[x].grid_forget()
            Label_route[x].grid_forget()
            Label_coupe[y].grid_forget()
            y = y -1
        x = x + 1
    piste_de_course.place(x=25,y=340,height=538,width=630)

en_piste = tk.Button(cadre_fonction_tri,command=voiture,pady=5,padx=15,text="En piste")
en_piste.place(x=10,y=150)

langue_français()
root.mainloop()