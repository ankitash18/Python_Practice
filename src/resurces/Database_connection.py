import sqlite3

class DataBaseConnection:

    def __init__(self,host):
        self.coonnection  =None
        self.host = host
    def __enter__(self):
        self.coonnection =  sqlite3.connect(self.host)
        return self.coonnection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.coonnection.close()
        else:
            self.coonnection.commit()
            self.coonnection.close()