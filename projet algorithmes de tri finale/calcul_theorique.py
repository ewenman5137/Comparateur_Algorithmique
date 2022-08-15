#calcul théorique des différente fonctions
from random import randint
from time import time
from math import log
def liste_alea(top,nombre):
    """
    Retourne une liste comportant "nombre" entiers de  compris entre 0 et "top"
    le choix se fait aléatoirement.
    Un même entier peut apparaître plusieurs fois.
    """
    return [randint(0,top) for _ in range(nombre)]

def tri_par_max(liste):
    """
    Tri de la liste en recherchant d'abord la valeur maximale et en la plaçant
    en fin de liste. Puis on recommence avec la liste restante en recherchant
     la valeur maximale de toutes les valeurs sauf la dernière. On continue
    jusqu'à obtenir toute la liste triée.
    Cette fonction retourne la même liste triée.
    """

    for fin in range(len(liste) - 1 ,0 ,-1 ):
        val_max =liste[0]
        ind_max = 0
        for ind in range(1,fin + 1):
            if liste[ind] > val_max:
                val_max = liste[ind]
                ind_max = ind
        liste[ind_max] , liste[fin] = liste[fin] , liste[ind_max]
    return liste

def tri_a_bulle(liste):
    """
    Tri de la liste en utilisant la méthode du tri à bulle.
    On compare 2 entiers consécutifs en partant de la gauche.
    Si les valeurs sont dans le mauvaise ordre, on les permute,
    on ne fait rien dans le cas contraire.
    Après un 1er passage la valeur maximale est à sa place à droite.
    On recommence en s'arretant avant le dernier élément et ainsi de suite.
    Cette fonction retourne la liste triée.
    """
    for fin in range (len(liste) - 1 ,0, -1):
        for ind in range(fin):
            if liste[ind] > liste[ind + 1]:
                liste[ind] , liste[ind + 1] = liste[ind + 1] , liste[ind]
    return liste

def tri_par_insertion_1(liste):
    """
    A partir d'une sous liste triée de p éléments, construit une liste triée
    de (p+1) éléments en insérant l'élément suivant à la bonne place.
    On part d'une sous liste composée d'un seul élément et on y ajoute
    un par un les autres éléments de la liste.
    Cette fonction retourne la liste triée.
    """

    for ind_nouveau in range(1 , len(liste)):
        valeur = liste[ind_nouveau]
        for ind in range(ind_nouveau):
            if liste[ind] > valeur:
                del(liste[ind_nouveau])
                liste.insert(ind,valeur)
    return liste

def point_insertion(liste,ind_nouveau):
    """
    Cette fonction détermine à quel endroit doit être insérée
    la valeur liste[ind_nouveau] dans la liste pour que soit
    conservé l'ordre. On suppose bien sûr que la liste est déjà
    triée pour les valeurs d'indice de 0 jusqu'à (ind_nouveau - 1)
    """
    valeur = liste[ind_nouveau]
    if valeur <= liste[0]:
        return 0
    if valeur >= liste[ind_nouveau-1]:
        return ind_nouveau
    ind_deb = 0
    ind_fin = ind_nouveau - 1
    while (ind_fin - ind_deb > 1):
        ind_milieu = (ind_deb + ind_fin) // 2
        val_test = liste[ind_milieu]
        if val_test == valeur:
            return ind_milieu
        if val_test > valeur:
            ind_fin = ind_milieu
        else:
            ind_deb = ind_milieu
    return ind_fin


def tri_par_insertion_4(liste):
    """
    A partir d'une sous liste triée de p éléments, construit une liste triée
    de (p+1) éléments en insérant l'élément suivant à la bonne place.
    On part d'une sous liste composée d'un seul élément et on y ajoute
    un par un les autres éléments de la liste.
    La place de l'insertion est déterminée par dichotomie
    Cette fonction retourne la liste triée.
    """

    for ind_nouveau in range(1 , len(liste)):
        ind = point_insertion(liste , ind_nouveau)
        valeur = liste[ind_nouveau]
        del(liste[ind_nouveau])
        liste.insert(ind,valeur)
    return liste

def tri_fusion(liste) :
    """
    Retourne la liste T triée par ordre croissant
    Attention contrairement aux autres algorithmes
    il ne modifie pas la liste donnée en paramètre
    """
    if len(liste) < 2 :
        return liste
    milieu = len(liste) // 2
    gauche = [ liste[ind] for ind in range(milieu) ]
    droite = [ liste[ind] for ind in range(milieu , len(liste)) ]
    return fusion(tri_fusion(gauche),tri_fusion(droite))

def fusion(gauche,droite) :
    """
    Si gauche et droite sont 2 listes triées par ordre croissant.
    retourne la liste fusionnée en conservant l'ordre croissant.
    Exemple: si gauche = [0, 1, 4, 6] et droite = [2, 3, 5, 7, 8]
    alors fusion(gauche,droite) vaut [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """

    resultat = []
    ind_gauche, ind_droite = 0, 0

    while (ind_gauche < len(gauche)) and (ind_droite < len(droite)):
        val_gauche = gauche[ind_gauche]
        val_droite = droite[ind_droite]
        if val_gauche < val_droite:
            resultat.append(val_gauche)
            ind_gauche += 1
        else:
            resultat.append(val_droite)
            ind_droite += 1

    if ind_gauche == len(gauche):
        resultat += droite[ind_droite:]
    else:
        resultat += gauche[ind_gauche:]
    return resultat

def verifie_ordre(liste):
    """
    Retourne la valeur True si la liste est triée par ordre croissant.
    Retourne False dans le cas où elle ne l'est pas.
    """
    for ind in range(len(liste) -2 ):
        if liste[ind] > liste[ind + 1]:
            return False
    return True

def chrono_tri(nombre,version):
    """
    Affiche le temps mis pour executer la version de tri donné par
    le paramètre pour le nombre donné de valeurs
    Verifie également que le tri a été correctement effectué.
    """
    liste = liste_alea(5 * nombre , nombre)
    deb = time()
    liste = version(liste)
    fin = time()
    assert len(liste) == nombre
    assert verifie_ordre(liste)

    duree = round(fin - deb,2)
    return duree

dico_temps_k = {"Tri par fusion":0,"Tri par max":0,"Tri à bulle":0,"Tri par insertion 1":0,"Tri par insertion 4":0}

def temps_theorique(version,n):
    if version == "Tri par fusion":
        if dico_temps_k["Tri par fusion"] == 0:
            k = chrono_tri(200_000,dico_fct["Tri par fusion"])/(200_000*log(200_000))
            dico_temps_k["Tri par fusion"]= k
            temps_theorique=dico_temps_k["Tri par fusion"]*n*log(n)
        else:
            temps_theorique=dico_temps_k["Tri par fusion"]*n*log(n)
    elif version == "Tri par max": 
        if dico_temps_k[version]==0:
            k = chrono_tri(10000,dico_fct[version])/10000**2
            dico_temps_k[version]= k
            temps_theorique = dico_temps_k[version]*n**2
        else:
            temps_theorique = dico_temps_k[version]*n**2
    elif version == "Tri à bulle": 
        if dico_temps_k[version]==0:
            k = chrono_tri(5000,dico_fct[version])/5000**2
            dico_temps_k[version]= k
            temps_theorique = dico_temps_k[version]*n**2
        else:
            temps_theorique = dico_temps_k[version]*n**2
    elif version == "Tri par insertion 1": 
        if dico_temps_k[version]==0:
            k = chrono_tri(10000,dico_fct[version])/10000**2
            dico_temps_k[version]= k
            temps_theorique = dico_temps_k[version]*n**2
        else:
            temps_theorique = dico_temps_k[version]*n**2
    else:
        if dico_temps_k["Tri par insertion 4"]==0:
            k = chrono_tri(50_000,dico_fct["Tri par insertion 4"])/50_000**2
            dico_temps_k["Tri par insertion 4"]= k
            temps_theorique = dico_temps_k[version]*n**2
        else:
            temps_theorique = dico_temps_k[version]*n**2
    return temps_theorique
# ======================================================================
# ZONE DE TEST
# ======================================================================
# Taille du tableau que l'on trie
dico_fct = {}
dico_fct["Tri par max"] = tri_par_max
dico_fct["Tri à bulle"] = tri_a_bulle
dico_fct["Tri par insertion 1"] = tri_par_insertion_1
dico_fct["Tri par insertion 4"] = tri_par_insertion_4
dico_fct["Tri par fusion"] = tri_fusion

A_TESTER = ["Bulle"]