# CRUD - CREATE, READ, UPDATE, DELETE
# Działanie	        Instrukcja SQL	    HTTP	             DDS
# Create	        INSERT	            PUT / POST	        write
# Read (Retrieve)	SELECT	            GET	                read / take
# Update	        UPDATE	            POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	            DELETE	            dispose

# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print('Baza danych została podłączona')


except sqlite3.Error as e:
    print("Bład podłączania do bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
