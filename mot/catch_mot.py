import os

class texte:

    def lecture(self, path):

        self.path = path
        
        os.chdir(self.path)
        liste = os.listdir()
        for i in liste:

            with open(i, 'r') as file:
                liste.append(file.read())

            return liste
            
        
    def traitement_liste(self, liste):
        self.liste = liste

        liste_texte = []

        for i in liste:
            if i[-4:] == '.txt':
                pass
            else:
                mot = ''
                for j in i:
                    if j == ' ':
                        liste_texte.append(mot)
                        mot = ''
                    else:
                        mot += j
                    
        print(liste_texte)
        return liste_texte



























