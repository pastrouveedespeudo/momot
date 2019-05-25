import os
import requests
import urllib.request
from bs4 import *

from database import *



class texte:

    
    def lecture(self, path):
        os.chdir(path)
        liste = os.listdir()



        liste1 = []

        for i in liste:
            with open(i, 'r') as file:
                liste1.append(file.read())

     
        return liste1


    def traitement_liste(self, liste):
        self.liste = liste

        liste_texte = []

        for i in self.liste:
            if i[-4:] == '.txt':
                pass
            else:
                mot = ''
                for j in i:
                    if j == '.' or j== ',' or\
                       j == '!' or j== '?' or\
                       j == '-' or j== ')' or\
                       j == ';' or j== '(' or\
                       j == '"' or j== "'":
                        pass
                       
                    elif j == ' ':
                        liste_texte.append(mot.lower())
                        mot = ''
                    else:
                        mot += j
   
        return liste_texte




    def recherche_mot_ou_database(self, texte):
        self.texte = texte

        liste_verbe = []

        ranger = set(self.texte)

        dico = {}
        for i in ranger:
            dico[i] = 0

        for i in self.texte:
            for cle, valeur in dico.items():
                if i == cle:
                    dico[i] += 1
       
        for i in ranger:
            
            path = "https://www.larousse.fr/dictionnaires/francais/{}".format(i)
          
            r = requests.get(path)

            page = r.content
            soup = BeautifulSoup(page, "html.parser")
            propriete = soup.find("p", {'class':'CatgramDefinition'})

            nombre = 0
            for cle, valeur in dico.items():
                if cle == i:
                    nombre += valeur


            try:
                print(i, propriete.string)
                if propriete.string == 'None' or propriete.string == None:
                    liste_verbe.append(i)
                recherche = create_base.recherche_en_database(self, i)
                if recherche == []:
                    create_base.mis_en_database(self, i, str(propriete.string), nombre)
                else:
                    nouveau_nombre = int(recherche[0][3]) + nombre
                    create_base.update_presence(self, i, nouveau_nombre)
                    
            except:
                pass


        return liste_verbe



    def traitement_verbe(self, liste):
        self.liste = liste

        dico = {}
        liste1 = set(self.liste)

        for i in liste1:
            dico[i] = 0

        for i in self.liste:
            for cle, valeur in dico.items():
                if i == cle:
                    dico[i] += 1

        for cle, valeur in dico.items():
            create_base.insertion_verbe(self, cle, valeur)



    def nombre_ponctuation(self, liste):
        self.liste = liste

        liste_ponctuation = []

        for i in self.liste:
            for j in i:
                if j == '.' or j== ',' or\
                   j == '!' or j== '?' or\
                   j == '-' or j== ')' or\
                   j == ';' or j== '(' or\
                   j == '"' or j== "'":
                    liste_ponctuation.append(j)

        return liste_ponctuation


    def traitement_ponctuation(self, liste):
        self.liste = liste

        dico = {}
        liste1 = set(self.liste)
        for i in liste1:
            dico[i] = 0


        for i in self.liste:
            for cle, valeur in dico.items():
                if i == cle:
                    dico[cle] += 1


        for cle, valeur in dico.items():
            if cle == ',':
                fonction = 'exprime une pause'
                create_base.insertion_ponctu(self, cle, fonction, valeur)

            elif cle == '!':
                fonction = 'exprime une exitation, haussement de voix'
                create_base.insertion_ponctu(self, cle, fonction, valeur)

            elif cle == '.':
                fonction = 'exprime une fin didée'
                create_base.insertion_ponctu(self, cle, fonction, valeur)

            elif cle == '?':
                fonction = 'exprime un étonnement'
                create_base.insertion_ponctu(self, cle, fonction, valeur)

            else:
                create_base.insertion_ponctu(self, cle, '', valeur)

            
                


























        












































