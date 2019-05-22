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
                    
     
        return liste_texte



    def recherche_mot_ou_database(self, texte):
        self.texte = texte

    

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


            print(i)
            try:
                print(i, propriete.string)
                recherche = create_base.recherche_en_database(self, i)
                #print(recherche)
                if recherche == []:
                    create_base.mis_en_database(self, i, str(propriete.string), nombre)
                else:
                    nouveau_nombre = int(recherche[0][3]) + nombre
                    create_base.update_presence(self, i, nouveau_nombre)
                    
            except:
                pass















