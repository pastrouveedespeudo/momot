import psycopg2

#continuer denregistrer des textes
#puis dans ce fichier voir les mots qui reviennent et les fonctions qui reviennent
#traiter les verbes dans un autre fichier
#faire des courbes
#enregistrer des textes tant que c pas significatif
#quand ca le sera faut que ca fasse un truk qui dit triste ou joyeux
#faire UNE TABLE MOT JOEYUX
#et dis toi que mot == mot TRISTE

class analyse:

    def base_mot_triste(self, table):
        self.table = table


        
        self.conn = psycopg2.connect(database='mot',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')

        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""select * from {};""".format(self.table))

        self.conn.commit()

        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste


    def nombre_mot(self, liste):
        self.liste = liste


        mot = []
        dico_mot = {}
        dico_fonction = {}

        
        for i in self.liste:
            dico_fonction[i[2]] = 0
            
        for i in self.liste:
            dico_mot[i[1]] = i[3]
        
            for cle, valeur in dico_fonction.items():
                if i[2] == cle:
                    dico_fonction[cle] += 1





        return dico_mot,dico_fonction


    def recup_dico_mot(self, dico1, dico2):
        self.dico1 = dico1
        self.dico2 = dico2
        
        print(self.dico1)
        print('\n')
        print(self.dico2)



analyse = analyse()
liste = analyse.base_mot_triste('momot')
dicos = analyse.nombre_mot(liste)
analyse.recup_dico_mot(dicos[0], dicos[1])





















