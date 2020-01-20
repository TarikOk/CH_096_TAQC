import uuid
import pyodbc as pyodbc


class Connection:

    def __init__(self):
        self.server = '34.65.101.58'
        self.database = 'EventsExpress'
        self.username = 'SA'
        self.password = '11D3v0ps'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.conn = pyodbc.connect('DRIVER=' + self.driver +
                                   ';SERVER=' + self.server +
                                   ';PORT=1433;DATABASE=' + self.database +
                                   ';UID=' + self.username +
                                   ';PWD=' + self.password)
        self.cursor = self.conn.cursor()

    def delete_user_with_email(self, name):
        self.cursor.execute("Delete from Users where Email like ?", name)
        self.cursor.commit()

    def delete_category_with_name(self, name):
        self.cursor.execute("Delete from Categories where Name like ?", name)
        self.cursor.commit()

    def edit_category_with_name(self, name, set):
        self.cursor.execute("Update Categories set Name = ? where Name like ?", (set, name))
        self.cursor.commit()

    def create_category_with_name(self, name):
        guid = uuid.uuid4()
        self.cursor.execute("INSERT INTO Categories(Id, Name) VALUES (?,?);", (guid, name))
        self.cursor.commit()

    def get_id_using_name(self, name):
        self.cursor.execute("select Id from Categories where Name = ?", name)
        return str(self.cursor.fetchone()[0])

    def confirm_useremail_on_register(self, email):
        self.cursor.execute("UPDATE Users SET EmailConfirmed = 1 WHERE Email like ?", email)
        self.cursor.commit()

    def close(self):
        self.conn.close()
