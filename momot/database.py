import psycopg2

class database:
    
    def creation_table(self):

        conn = psycopg2.connect(database='mot',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333')

        cursor = conn.cursor()
        
        cursor.execute("""create table momotv2(
                        id serial PRIMARY KEY,
                        mot varchar(100),
                        presence INT);""")

        conn.commit()



#database = database()
#database.creation_table()
