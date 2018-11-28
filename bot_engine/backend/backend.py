import sqlite3

class Backend():
    def __init__(self):
        ## name von db Datei
        self.dbfile = "backend/bundesbot.db"

    def eval(self,sql,parameters=(),doprint=False):
        ## benutze eval, um sql auszufüren
        conn = sqlite3.connect(self.dbfile)
        cursor = conn.cursor()
        cursor.execute(sql,parameters)
        res = cursor.fetchall()
        conn.close()
        if doprint:
            print(str(res))
        return res

    def setup(self):
        ## backend datenbank aufsetzten
        conn = sqlite3.connect(self.dbfile)
        print(sqlite3.version)
        cursor = conn.cursor()
        print("SETTING up database")

        ## TODO einkommentieren und fertig implementieren, um db zu erstellen
        cursor.execute("DROP TABLE IF EXISTS bundesbot")
        cursor.execute('''CREATE TABLE bundesbot
                        (name text)''')

        ## TODO einkommentieren und fertig implementieren, um Beispiel daten zu erstellen
        cursor.execute(
          "INSERT INTO bundesbot VALUES ('bla')")
        res = cursor.execute("SELECT count(*) from bundesbot")
        print("DB hat "+str(res.fetchone()[0])+" Einträge")
        conn.commit()
        conn.close()

