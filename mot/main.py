from catch_mot import texte





if __name__ == '__main__':

    texte = texte()
    le_texte = texte.lecture(r'C:\Users\jeanbaptiste\Desktop\cluster\mot\texte\triste')
    texte_mot = texte.traitement_liste(le_texte)
    texte.recherche_mot_ou_database(texte_mot)
 
