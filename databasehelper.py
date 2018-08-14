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

    def create_model_table(self):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS model(
            time TEXT,
            name TEXT,
            valacc REAL,
            valloss REAL,
            acc REAL,
            loss REAL,
            training_curve_path TEXT,
            training_structure_path TEXT
        );""")
        self.conn.commit()
        self.conn.close()

    def save_model_data(self,name,valacc,valloss,acc,loss,training_curve_path,training_structure_path):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("INSERT INTO model(time,name,valacc,valloss,acc,loss,training_curve_path,training_structure_path) VALUES(CURRENT_TIMESTAMP,'" + str(name) + "'," + str(valacc) + "," + str(valloss) + "," + str(acc) + "," + str(loss) + ",'" + training_curve_path + "','" + training_structure_path + "');")
        self.conn.commit()
        self.conn.close()

    def retrieve_models(self):
        self.create_connection()
        c = self.conn.cursor()
        cur = c.execute("SELECT * FROM model;")

        Results = [dict(Time=row[0],
                    Name=row[1],
                    ValAcc=str(round(row[2]*100,2)),
                    ValLoss=str(round(row[3]*100,2)),
                    Acc=str(round(row[4]*100,2)),
                    Loss=str(round(row[5]*100,2)),
                    Curve=row[6],
                    Structure=row[7]) for row in cur.fetchall()]

        self.conn.close()
        return Results
