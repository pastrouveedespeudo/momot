class lecture:
    
    def lecture(self, fichier):

        self.fichier = fichier

        liste = []
        file = open(self.fichier, "r")
        liste.append(file.read())

        return liste



class nettoyage:

    def mise_en_mot(self, liste):
        self.liste = liste

        liste2 = [i.split() for i in self.liste]
        liste2 = liste2[0]
        liste2 = [i.lower() for i in liste2]

        return liste2


    def ponctuation(self, liste):

        self.liste = liste

        liste_ponctuation = [".", ",", ";","!","?",":", "'", '"']


        liste1 = []

        for i in self.liste:

            if i == "/" or i == " /" or i == "/ " or i == " / ":
                self.liste.remove(i)
            else:
                ajout1 = ""
                ajout = ""
                
                if i[-3:] == "...":
                    liste1.append(i[:-3])
                    liste1.append(i[-1:])
                    ajout1 = True

                if ajout1 != True:
                    for j in liste_ponctuation:

                        if i[-1] == j:
                            liste1.append(i[:-1])
                            liste1.append(i[-1])
                            ajout = True
                            

            if ajout != True and ajout1 != True:
                liste1.append(i)



        return liste1



    def apostrophe(self, liste):

        self.liste = liste

        liste1 = []
        for i in self.liste:

            ajout = ""
            
            for j in i:
                if j == "'":
                    index = i.index(j)
                    liste1.append(i[:index])
                    liste1.append(i[index+1:])
                    ajout = True
                    
            if ajout != True:
                liste1.append(i)

        return liste1






class nombre:
    
    def comptage(self, liste):
        self.liste = liste

        recurence = []

        liste1 = set(self.liste)

        for i in self.liste:
            compt = self.liste.count(i)
            recurence.append([i, compt])

                
        liste2 = []
        dico = {}
        for i in sorted(liste1):
            dico[i] = 0

        for i in recurence:
            for cle, valeur in dico.items():
                
                if i[0] == cle:
                    dico[cle] = i[1]
                    break

        print(dico)
        return dico

if __name__ == "__main__":

    fichier = "essais.txt"


    lecture = lecture()
    nettoyage = nettoyage()
    nombre = nombre()

    texte = lecture.lecture(fichier)
    texte_nettoye1 = nettoyage.mise_en_mot(texte)
    texte_nettoye2 = nettoyage.ponctuation(texte_nettoye1)
    texte_nettoye3 = nettoyage.apostrophe(texte_nettoye2)
    nombre.comptage(texte_nettoye3)












