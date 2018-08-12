import sqlite3



class database_object():

    def __init__(self):
        self.path_to_db = 'db/predictions.db'

    def create_connection(self):
        self.conn = sqlite3.connect(self.path_to_db)

    def create_table(self):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS predictions(
            time TEXT,
            name TEXT,
            email TEXT,
            fileLocation TEXT,
            outcome TEXT
        );""")
        self.conn.commit()
        self.conn.close()

    def add_prediction_to_db(self, name, email,filename):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("INSERT INTO predictions(time,name,email,fileLocation,outcome) VALUES(CURRENT_TIMESTAMP, '" + name + "','" + email + "','" + filename + "','Not Yet Classified');")
        self.conn.commit()
        self.conn.close()

    def get_all_entries(self):
        self.create_connection()
        c = self.conn.cursor()
        cur = c.execute("SELECT * FROM predictions")
        Results = [dict(Time=row[0],
                    Name=row[1],
                    Email=row[2],
                    FileName=row[3],
                    Outcome=row[4]) for row in cur.fetchall()]
        self.conn.close()
        return Results

    def set_new_outcome(self, newfilename, time):
        self.create_connection()
        c = self.conn.cursor()
        print("UPDATE predictions SET outcome ='" + newfilename + "' WHERE time ='" + time + "');")
        c.execute("UPDATE predictions SET outcome ='" + newfilename + "' WHERE time ='" + time + "';")
        self.conn.commit()
        self.conn.close()