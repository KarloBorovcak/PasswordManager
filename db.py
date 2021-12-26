import psycopg2


class DataBase:
    DB_NAME = "passwordmanager"
    DB_USER = "karlo"

    def __init__(self):
        self.conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER)
        self.cur = self.conn.cursor()

    def add_account(self, username, password, site):
        pass

    def get_account(self):
        pass


# conn.commit()

# cur.close()

# conn.close()
