import sqlite3
from apps import errorhandler
class DB(object):
    def connect(self):
        try:
            self.conn = sqlite3.connect("./student.db")
            self.c = self.conn.cursor()
            self.c.execute(''' 
                CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,
                name TEXT,
                dob TEXT,
                tel TEXT,
                sex BOOLEAN,
                address CHAR(50)
            )''')
            self.c.execute('''
                CREATE TABLE IF NOT EXISTS learnresult (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                math (FLOAT),
                history (float),
                physics (float),
                average (float)
            )''')
            self.conn.commit()
        except Exception as e:
            errorhandler.writelog(str(e))
            return
            
    def liststudent(self):
        self.connect()
        self.c.execute('''            SELECT * FROM STUDENT ''')
        result = self.c.fetchall()
        self.conn.close()
        return result
        
    def addstudent(self,result):
        self.connect()
        self.c.execute('''
        INSERT INTO student (name,dob,tel,sex,address) VALUES (?,?,?,?,?)
        ''', (result['Name'],result['DOB'],result['Tel'], result['Sex'], result['Address']))
        self.conn.commit()
        self.conn.close()
        return
