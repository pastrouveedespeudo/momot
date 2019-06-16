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

        liste_ponctuation = [".", ",", ";","!","?",":", "'", '"', "-"]


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

 
        dico = sorted(dico.items(), key=lambda t: t[1])
        return dico


    def pourcent(self, dico):

        self.dico = dico

        total = 0
        for i in self.dico:
            total += i[1]


        liste = []
        for i in self.dico:
            if i[1] <= 10:
                pass
            else:
                calcul = (i[1]*100) / total
                liste.append([i[0], calcul])
             
                

   
        return liste 


class comparatif:

    def comparaison(self, text1, text2, text2_base):
        self.text1 = text1
        self.text2 = text2


        compa = [i[0] for i in self.text1 for j in self.text2 if i[0] == j[0]]
        compa1 = [i for i in self.text2 for j in self.text1 if i[0] == j[0]]
        compa2 = [i for i in self.text1 for j in self.text2 if i[0] == j[0]]


        c = 0
        for i in compa1:
            print(i[0], "est présent à :", i[1], "et dans le fichier source :", compa2[c][1])
            c+=1
            
        print("\n\n")
        
        print(len(text2_base))
        print(len(self.text2))
        
        


        


if __name__ == "__main__":


    TEXTE_A_COMPARER = "joie.txt"
    
    lecture = lecture()
    nettoyage = nettoyage()
    nombre = nombre()
    comparatif = comparatif()
        
    
    texte = lecture.lecture("textes_triste.txt")
    texte_nettoye1 = nettoyage.mise_en_mot(texte)
    texte_nettoye2 = nettoyage.ponctuation(texte_nettoye1)
    texte_nettoye3 = nettoyage.apostrophe(texte_nettoye2)
    texte_final = nombre.comptage(texte_nettoye3)
    text_final1 = nombre.pourcent(texte_final)


    texte = lecture.lecture(TEXTE_A_COMPARER)
    texte_nettoye1 = nettoyage.mise_en_mot(texte)
    texte_nettoye2 = nettoyage.ponctuation(texte_nettoye1)
    texte_nettoye3 = nettoyage.apostrophe(texte_nettoye2)
    texte_final = nombre.comptage(texte_nettoye3)
    text_final2 = nombre.pourcent(texte_final)


    comparatif.comparaison(text_final1, text_final2, texte_final)



    #on peut rajouter texte triste amour, ado, sucide, mort ect.... la c un mixte
    #mtn avec mot joie si ca match ca marche pas trop


