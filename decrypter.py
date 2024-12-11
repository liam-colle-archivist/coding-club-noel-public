...
decalage = ...

texte = fichier....()
fichier....()
resultat = ""
for i in ...(len(...)):
    charactere = texte[i]
    if ....isalpha():
        if charactere....():
            resultat += chr((...(charactere) + ... - 65) % ... + 65)
        ...:
            resultat += ...((...(...) + decalage - ...) % 26 + 97)
    ...:
        resultat += ...

print(...)