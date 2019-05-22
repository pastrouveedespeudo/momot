from catch_mot import Texte





if __name__ == '__main__':

    texte = Texte()
    le_texte = texte.lecture(r'C:\Users\jeanbaptiste\Desktop\cluster\texte\triste')
    texte_rangé = texte.traitement_liste(le_texte)
    texte.mot_liste(texte_rangé)
