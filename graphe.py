import copy

# ===========================================================================================================================================

# 1.1.1. Définir une fonction pref qui étant donné un mot u passé en paramètre renvoie la
# liste des préfixes de u.
def pref(u):
    prefixes = [u[:i] for i in range(len(u) + 1)]
    return prefixes

# 1.1.2. Définir une fonction suf qui étant donné un mot u passé en paramètre renvoie la
# liste des suffixes de u.
def suf(u):
    suffixes = [u[i:] for i in range(len(u) + 1)]
    return suffixes
    # on peut utiliser [::-1] sur suffixes pour renverser la liste et renvoyer ça ['', 'u', 'ou', 'cou', 'ucou', 'oucou', 'coucou']


# 1.1.3. Définir une fonction fact qui étant donné un mot u passé en paramètre renvoie la
# liste sans doublons des facteurs de u.

def fact(u):
    
    factors = set()#j'utilise un ensemble pour ne pas avoir de doublons sur la concatenation sans avoir a faire de vefication
    for i in range(len(u) + 1):
        for j in range(i + 1, len(u) + 1):
            factors.add(u[i:j])
    return sorted([''] + list(factors))
    # j'ai pas reussi a mettre le mot vide donne je l'ai rajouter manuelement

# 1.1.4. Définir une fonction miroir qui étant donné un mot u passé en paramètre renvoie le
# mot miroir de u.
def miroir(u):
    return u[::-1]
    # comme j'ai dis precedement cela renverse.

# ===========================================================================================================================================

# 1.2.1. Définir une fonction concatene qui étant donnés deux langages L1 et L2 renvoie le
# produit de concaténation (sans doublons) de L1 et L2.
def concatene(L1, L2):
    concatenation = set() #j'utilise un ensemble pour ne pas avoir de doublons sur la concatenation sans avoir a faire de vefication
    for i in L1:
        for j in L2:
            concatenation.add(i+j) 
    return list(concatenation)
    # j'ai pas reussi a obtenir dans le sens presenter dans le sujet

# 1.2.2. Définir une fonction puis qui étant donnés un langage L et un entier n renvoie le
# langage L^n (sans doublons).

def puis(L, n):
    # j'ai trouver ses deux methodes qui fonctionne
    
    # un faisant appelle a concatene et qui utilise une boucle
    
    # if n == 0:
    #     return ['']
    # result = set(L)
    # for i in range(n - 1):
    #     result = concatene(L, result)
    # return sorted(list(result))

    # le deux methodes qui fonctionne en utilisant aussi concatene mais en faisant appelle a lui meme (fonction recursive) sans boucle 
    if n == 0:
        return ['']
    elif n == 1:
        return L
    else:
        return sorted(concatene(L, puis(L, n-1)))

# 1.2.3. Pourquoi ne peut-on pas faire de fonction calculant l’étoile d’un langage ?

# Selon moi on ne peux pas calculer l'etoile d'un language car sa viendrais a calculer a l'infini
# exemple
# Un language L qui contient uniquement le mot a dont L = {a} l'etoile de se language donc
# L* représenterais l'ensembnle de tous les mots qui peuvent être créés en concatenant 0, 1, 2, 3 ..... fois a
# qui incluent le mot vide epsilon donc L* = {ε, a, aa, aaa, aaaa, ...} et calculer a l'infini sans jamais s'arréter.

# 1.2.4. Définir une fonction tousmots qui étant donné un alphabet A passé en paramètre
# renvoie la liste de tous les mots de A∗ de longueur inférieure à n.
def tousmots(A, n):
    return A

# =================================================================

# 1.3.1. Définir une fonction defauto qui permet de faire la saisie d’un automate (sans doublon).

def auto(A):
    # ajout des etats inicial et ajout des etats finaux
    aut = {}
    for i in A:
        aut[i] = []
    return aut
                
# 1.3.2. Définir une fonction lirelettre qui étant donnés en paramètres une liste de transitions T, une liste d’états E et une lettre a, renvoie la liste des états dans lesquels on peut
# arriver en partant d’un état de E et en lisant la lettre a.

def lirelettre(T, E, a):
    etats_suivants = set()
    for transition in T:
        if transition[1] == lettre and transition[0] in E:
            etats_suivants.add(transition[2])
    return list(etats_suivants)

# 1.3.3. Définir une fonction liremot qui étant donnés en paramètres une liste de transitions
# T, une liste d’états E et un mot m, renvoie la liste des états dans lesquels on peut arriver
# en partant d’un état de E et en lisant le mot m.

def liremot(T, E, m):
    etats_suivants = E
    for lettre in m:
        etats_suivants = lirelettre(T, etats_suivants, lettre)
    return etats_suivants

# 1.3.4. Définir une fonction accepte qui prend en paramètres un automate et un mot m et
# renvoie True si le mot m est accepté par l’automate.

def accepte (auto, m):
    if (liremot(auto["transitions"],auto["etats"], mot) == auto["F"]):
        return True
    else:
        return False
# ===========================================================================================================================================






if __name__ == "__main__":
    auto = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 2]],
        "I": [0],
        "F": [2]
    }
    

    # remplacer coucou pour obtenir une liste des suffixes et des préfixes du mot
    
    # declaratiopn des variables
    #=============================
    mot = "coucou"
    L1=['aa','ab','ba','bb']
    L2=['a', 'b', '']
    A = ['a', 'b']
    

    # ============================
    
    print("------------------------------------------------------------")
    print("1 Mots, langages et automates...")
    print("------------------------------------------------------------")
    print("1.1 Mots")
    print("============================================================")
    print("Le mot choisis est : " + mot)
    print("============================================================")
    
    print("\nPrefixes de " + mot + ":") 
    print(pref(mot))
    print("\nSuffixes de " + mot + ":") 
    print(suf(mot))
    print("\nFacteurs de " + mot + ":")
    print(fact(mot))
    print("\nMiroir de " + mot + ":")
    print(miroir(mot))
    
    print("============================================================")
    
    print("\n\n")
    print("------------------------------------------------------------")
    print("1.2 Langages")
    print("============================================================")
    print("Les deux language choisis sont : ")
    print("L1 = " + str(L1) + " et L2 = " + str(L2) +"\n")
    print("L'alphabet utiliser est : " + str(A))
    
    print("\nConcatenation de L1 et L2 : ")
    print(concatene(L1, L2))
    
    print("\nPuis de L1: ")
    print(puis(L1, 2))
    
    print("Alphabet : A = " + str(A))
    print("\ntousmots de l'alphabet A :")
    print(tousmots(A, 3))
    
    print("============================================================")
    
    print("\n\n")
    
    print("------------------------------------------------------------")
    
    print("1.3 Automates")
    print("============================================================")
    
    print("L'automate choisis est : ")
    print(auto)
    
    lettre = 'a'
    
    print("\nLirelettre " + lettre + " dans l'automate :")
    print(lirelettre(auto["transitions"],auto["etats"], lettre))
    
    mot = 'aba'
    
    print("\nLiremot " + mot + " dans l'automate :")
    print(liremot(auto["transitions"],auto["etats"], mot))
    
    print("\nAccepte " + mot + " dans l'automate :")
    print(accepte(auto, mot))