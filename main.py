#### Fonction secondaire
"""Fonction qui permet de connaitre si une séquence de lettres est un palindrome ou non
p: chaîne de caractères
"""
def ispalindrome(p):
    """on crée une table (traducteur)  
    afin de modifier les caracères originaux en ce que l'on souhaite
    et supprimer les caractères spéciaux
"""
    p=p.lower() #remets toutes les lettres en minuscule
    traducteur=p.maketrans("éèêëôùûaàç","eeeeouûaac"," ,'/?!.:-_")
    p=p.translate(traducteur)
    if p==p[::-1]:
        return True
    return False
#### Fonction principale


def main():
    "fonction main qui permet de vérifier le code secondaire à travers différents exemples"
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
