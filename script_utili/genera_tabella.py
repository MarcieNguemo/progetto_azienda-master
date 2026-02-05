import mysql.connector
def crea_tabella():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="azienda_generation")
    cursor = conn.cursor()

    q_crea_fatture = """
    create table IF NOT EXISTS fattura(
         id_fattura INT PRIMARY KEY,
         emittente VARCHAR(80) DEFAULT "Azienda Zurich" NOT NULL,
         destinatario VARCHAR(80) NOT NULL,
         bene_servizio_venduto VARCHAR(80) NOT NULL,
         importo DOUBLE NOT NULL,
         iva double NOT NULL,
         imponibile double NOT NULL,
         data_fattura DATE
     );
"""
    cursor.execute(q_crea_fatture)

if __name__ == '__main__':
    crea_tabella()