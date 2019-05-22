import mysql.connector

class create_base:
    def database(self):
        
        self.connexion = mysql.connector.connect(host='127.0.0.1',
                                                 user='root',
                                                 password='TioTioTio333')

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE MOT""")
        self.connexion.commit()
