import psycopg2

class create_base:

    def table(self):

        self.conn = psycopg2.connect(database='bobo',
                            user='postgres',
                            host='127.0.0.1',
                            password='tiotiotio333')
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE table momot(
                                id serial PRIMARY KEY,
                                mot VARCHAR(100),
                                fonction VARCHAR(100),
                                presence INT);""")
        
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
                            from momot where mot = '{}'""".format(mot_cherché))

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

        self.cursor.execute("""INSERT INTO momot
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

        sql = ("""UPDATE momot set presence = %s
                WHERE (mot = %s);""")

        
        value = (self.presence, self.mot)
        
        self.cursor.execute(sql, value)
        self.conn.commit()



##create_base = create_base()
##create_base.table()



















