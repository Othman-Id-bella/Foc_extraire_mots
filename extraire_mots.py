def extraire_mots(phrase):
    mots = phrase.split()
    return mots

phrase_test = "Bonjour, comment ça va ?"
mots_extraits = extraire_mots(phrase_test)
print(f"Mots extraits de la phrase : {mots_extraits}")
