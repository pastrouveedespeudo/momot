import psycopg2

class create_base:

    def table_triste(self):

        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE table momot_triste(
                                id serial PRIMARY KEY,
                                mot VARCHAR(100),
                                fonction VARCHAR(100),
                                presence INT);""")
        
        self.conn.commit()

    def table_verbe_triste(self):

        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE table verbe_triste(
                                id serial PRIMARY KEY,
                                verbe VARCHAR(100),
                                presence INT);""")
        
        self.conn.commit()



    def table_ponctu_triste(self):

        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE table ponctu_triste(
                                id serial PRIMARY KEY,
                                ponctu VARCHAR(100),
                                fonction VARCHAR(100),
                                presence INT);""")
        
        self.conn.commit()



    def insertion_ponctu(self, ponctu, fonction, presence):
        self.ponctu = ponctu
        self.fonction = fonction
        self.presence = presence


        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""INSERT INTO ponctu_triste
                            (ponctu, fonction, presence)
                            VALUES(%s, %s, %s)""",
                            (self.ponctu, self.fonction, self.presence))
        
        self.conn.commit()


    def insertion_verbe(self, verbe):
        self.verbe = verbe
        self.presence = presence
        
        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""INSERT INTO verbe_triste
                            (verbe, presence)
                            VALUES(%s, %s)""",
                            (self.verbe, self.presence))
        
        self.conn.commit()










    def table_joyeux(self):

        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE table momot_joyeux(
                                id serial PRIMARY KEY,
                                mot VARCHAR(100),
                                fonction VARCHAR(100),
                                presence INT);""")
        
        self.conn.commit()
        

    def recherche_en_database(self, mot_cherché):

        self.conn = psycopg2.connect(database='mot',
                                    user='postgres',
                                    host='127.0.0.1',
                                    password='tiotiotio333')
        
        self.cursor = self.conn.cursor()


        self.cursor.execute("""select *
                            from momot_triste where mot = '{}'""".format(mot_cherché))

        self.conn.commit()

        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste



    def mis_en_database(self, mot, fonction, presence):

        self.mot = mot
        self.presence = presence
        self.fonction = fonction

        self.conn = psycopg2.connect(database='mot',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()

        self.cursor.execute("""INSERT INTO momot_triste
                            (mot, fonction, presence)
                            VALUES (%s,%s,%s)
                            """, (self.mot, self.fonction, self.presence))
        self.conn.commit()


    def update_presence(self, mot, presence):

        self.mot = mot
        self.presence = presence
        
        self.conn = psycopg2.connect(database='mot',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')

        self.cursor = self.conn.cursor()

        sql = ("""UPDATE momot_triste set presence = %s
                WHERE (mot = %s);""")

        
        value = (self.presence, self.mot)
        
        self.cursor.execute(sql, value)
        self.conn.commit()



##create_base = create_base()
##
##create_base.table_triste()
##create_base.table_verbe_triste()
##create_base.table_ponctu_triste()
