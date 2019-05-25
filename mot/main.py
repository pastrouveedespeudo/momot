from catch_mot import texte





if __name__ == '__main__':

    texte = texte()
    le_texte = texte.lecture(r'C:\Users\jeanbaptiste\Desktop\cluster\mot\texte\triste')

    texte.nombre_ponctuation(le_texte)
    texte_mot = texte.traitement_liste(le_texte)

    verbe = texte.recherche_mot_ou_database(texte_mot)
    texte.traitement_verbe(verbe)

    ponctuation = texte.nombre_ponctuation(le_texte)
    texte.traitement_ponctuation(ponctuation)
