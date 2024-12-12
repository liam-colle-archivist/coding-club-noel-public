fichier = open("./...", "r")
decalage = ...

texte = fichier....()
resultat = ""
for i in ...(len(...)):
    charactere = texte[i]
    if ....isalpha():
        if ....isupper():
            resultat += chr((...(charactere) + ... - 65) % ... + 65)
        ...:
            resultat += ...((ord(...) + decalage - ...) % 26 + 97)
    ...:
        resultat += ...

print(...)
