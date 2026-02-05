import mysql.connector
def crea_database():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost")
    cursor = conn.cursor()

    q_crea_database = "CREATE DATABASE azienda_generation"
    cursor.execute(q_crea_database)

if __name__ == '__main__':
    crea_database()