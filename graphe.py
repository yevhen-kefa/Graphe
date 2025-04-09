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
# Exo 2

def deterministe(automate):
    transitions = automate["transitions"]
    transitions_vue = set()
    for transition in transitions:
        origine = transition[0]
        lettre = transition[1]
        if (origine, lettre) in transitions_vue:
            return False
        transitions_vue.add((origine, lettre))
    return True

def fusionner_etats(etats):
    return tuple(sorted(set(etats)))

def etats_atteignables(etats, lettre, transitions):
    result = set()
    for etat in etats:
        for transition in transitions:
            if transition[0] == etat and transition[1] == lettre:
                result.add(transition[2])
    return fusionner_etats(result)

def deterministe(automate):
    transitions = automate["transitions"]
    seen_transitions = set()
    for transition in transitions:
        origine = transition[0]
        lettre = transition[1]
        if (origine, lettre) in seen_transitions:
            return False
        seen_transitions.add((origine, lettre))
    return True

def determinise(automate):
    if deterministe(automate):
        return automate

    alphabet = automate["alphabet"]
    transitions = automate["transitions"]
    I = automate["I"]
    F = automate["F"]

    etats_determinises = []
    transitions_determinises = []
    etats_a_explorer = [fusionner_etats(I)]

    etats_determinises.append(fusionner_etats(I))

    while etats_a_explorer:
        etat_courant = etats_a_explorer.pop(0)
        for lettre in alphabet:
            etats_destinations = etats_atteignables(etat_courant, lettre, transitions)
            if etats_destinations and etats_destinations not in etats_determinises:
                etats_determinises.append(etats_destinations)
                etats_a_explorer.append(etats_destinations)
            if etats_destinations:
                transitions_determinises.append([list(etat_courant), lettre, list(etats_destinations)])


    F_determinise = []
    for etat in etats_determinises:
        if any(sous_etat in F for sous_etat in etat):
            F_determinise.append(list(etat))

    etats_determinises = [list(etat) for etat in etats_determinises]
    I_determinise = [list(fusionner_etats(I))]

    automate_determinise = {
        "alphabet": alphabet,
        "etats": etats_determinises,
        "transitions": transitions_determinises,
        "I": I_determinise,
        "F": F_determinise
    }

    return automate_determinise


def remplacer_etat(etats, ancien, nouveau):
    return [nouveau if etat == ancien else etat for etat in etats]

def remplacer_etat_transitions(transitions, ancien, nouveau):
    nouvelles_transitions = []
    for transition in transitions:
        origine, lettre, destination = transition
        if origine == ancien:
            origine = nouveau
        if destination == ancien:
            destination = nouveau
        nouvelles_transitions.append([origine, lettre, destination])
    return nouvelles_transitions


def renommage(automate):
    alphabet = automate["alphabet"]
    etats = automate["etats"]
    transitions = automate["transitions"]
    I = automate["I"]
    F = automate["F"]


    etat_mapping = {tuple(etat): i for i, etat in enumerate(etats)}


    nouveaux_etats = list(etat_mapping.values())


    nouvelles_transitions = []
    for transition in transitions:
        origine = tuple(transition[0])
        lettre = transition[1]
        destination = tuple(transition[2])
        nouvelles_transitions.append([etat_mapping[origine], lettre, etat_mapping[destination]])


    nouveaux_I = [etat_mapping[tuple(I[0])]]
    nouveaux_F = [etat_mapping[tuple(f)] for f in F]

    automate_renomme = {
        "alphabet": alphabet,
        "etats": nouveaux_etats,
        "transitions": nouvelles_transitions,
        "I": nouveaux_I,
        "F": nouveaux_F
    }

    return automate_renomme


#-------------------Complémentation---------------------

def complet(automate):
    alphabet = automate["alphabet"]
    etats = automate["etats"]
    transitions = automate["transitions"]

    transition_dict = {(etat, lettre): False for etat in etats for lettre in alphabet}

    for transition in transitions:
        origine, lettre, _ = transition
        transition_dict[(origine, lettre)] = True

    for key in transition_dict:
        if not transition_dict[key]:
            return False

    return True


def complete(automate):
    alphabet = automate["alphabet"]
    etats = automate["etats"]
    transitions = automate["transitions"]

    transition_dict = {(etat, lettre): False for etat in etats for lettre in alphabet}

    for transition in transitions:
        origine, lettre, _ = transition
        transition_dict[(origine, lettre)] = True


    puits = max(etats) + 1
    etats.append(puits)


    for etat in etats:
        for lettre in alphabet:
            if not transition_dict.get((etat, lettre), False):
                if [etat, lettre, puits] not in transitions:
                    transitions.append([etat, lettre, puits])

    for lettre in alphabet:
        if [puits, lettre, puits] not in transitions:
            transitions.append([puits, lettre, puits])

    return {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": automate["I"],
        "F": automate["F"]
    }


def complement(auto):
    auto_complet = complete(renommage(determinise(auto)))
    etats_finaux = set(auto_complet["F"])
    etats_non_finaux = set(auto_complet["etats"]) - etats_finaux

    auto_complet["F"] = list(etats_non_finaux)

    return auto_complet






if __name__ == "__main__":
    auto = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 2]],
        "I": [0],
        "F": [2]
    }
    auto0 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2, 3],
        "transitions": [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3]],
        "I": [0],
        "F": [3]
    }

    auto1 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1],
        "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'b', 1], [1, 'a', 1]],
        "I": [0],
        "F": [1]
    }

    auto2 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1],
        "transitions": [[0, 'a', 0], [0, 'a', 1], [1, 'b', 1], [1, 'a', 1]],
        "I": [0],
        "F": [1]
    }

    auto3 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [0, 'a', 0], [1, 'b', 2], [1, 'b', 1]],
        "I": [0],
        "F": [2]
    }

    auto4 ={
        "alphabet":['a','b'],"etats": [0,1,2,],
        "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]
    }
    auto5 ={
        "alphabet":['a','b'],"etats": [0,1,2],
        "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
        "I":[0],"F":[0,1]
    }

    auto6 ={
        "alphabet":['a','b'],
        "etats": [0,1,2,3,4,5],
        "transitions": [
            [0,'a',4],[0,'b',3],[1,'a',5],
            [1,'b',5],[2,'a',5],[2,'b',2],
            [3,'a',1],[3,'b',0],[4,'a',1],
            [4,'b',2],[5,'a',2],[5,'b',5]
        ],
        "I":[0],
        "F":[0,1,2,5]
    }

    autoexo3 = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3, 4, 5],
        "transitions": [[1, 'a', 1], [1, 'a', 2], [2, 'b', 3], [2, 'a', 5], [5 , 'b', 5], [3, 'b', 3], [3, 'a', 4]],
        "I": [1],
        "F": [4, 5]
    }


    autoforprod1 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2, 3],
        "transition": [[0, 'b', 1], [0, 'a', 3], [1, 'a', 2], [1, 'b', 3], [2, 'a', 2], [2, 'b', 2]],
        "I": [0],
        "F": [2]
    }

    autoforprod2 = {
        "alphabet": ['a', 'b'],
        "etats": [4, 5, 6, 7],
        "transition": [[4, 'a', 5], [4, 'b', 4], [5, 'a', 5], [5, 'b', 6], [2, 'a', 2], [2, 'b', 2]],
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

    print("------------------------------------------------------------")
    print("2 Déterminisation.")
    print("------------------------------------------------------------")
    print('2.1')
    print("============================================================")
    
    print(deterministe(auto0))  # True
    print(deterministe(auto2))  # False
    print('\n')

    print('2.2')
    print(determinise(auto2))
    print(determinise(auto2))

    print('2.3')
    print(renommage(determinise(auto2)))
    print('============================================================')

    print ("\n\n")

    print("------------------------------------------------------------")
    print("3 Complétion.")
    print("------------------------------------------------------------")
    print('3.1')
    print("============================================================")
    print(complet(auto0))  # False
    print(complet(auto1))  # True
    print("============================================================")
    print('\n')
    print('3.2')
    print("============================================================")
    print(complete(auto0))
    print("============================================================")
    print('\n')
    print('3.3')
    print("============================================================")
  
    print(complement(auto3))
    print('============================================================')
    print ("\n\n")