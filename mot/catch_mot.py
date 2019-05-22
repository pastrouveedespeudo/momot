import os

class Texte:

    def lecture(self, path):

        self.path = path

        liste_des_textes = []
        
        os.chdir(self.path)
        liste = os.listdir()
        for i in liste:
            liste1 = []
            with open(i, 'r') as file:
                liste1.append(file.read())
            
            liste_des_textes.append(liste1)
            
        return liste_des_textes
            
        
    def traitement_liste(self, liste):
        self.liste = liste

        liste_texte = []

        for i in self.liste:
            mot = ''
            for j in i:
                for k in j:
                    if k == ' ':
                        liste_texte.append(mot)
                        mot = ''
                    else:
                        mot += k

        return liste_texte


    def mot_liste(self, liste):
        self.liste = liste

        dico = {}
        
        ranger = set(self.liste)

        for i in ranger:
            dico[i] = 0
            
        for i in self.liste:
            for cle, valeur in dico.items():
                if i == cle:
                    dico[i] += 1

        print(dico)
    
    

    def nombre_verbe():
        pass


























