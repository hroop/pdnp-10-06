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

    insert = '''
    INSERT INTO hardware (id,name,price) VALUES (1, 'Apple',6999);
    '''
    insert_samsung = '''
        INSERT INTO hardware (id,name,price) VALUES (2, 'Samsung',6999);
        '''
    # create - insert
    # c.execute(insert)
    # conn.commit()
    # create - insert
    # c.execute(insert_samsung)
    # conn.commit()

    # read - select
    select = """
    SELECT * FROM hardware;
    """
    for row in c.execute(select):
        print(row)  # (1, 'Apple', 6999.0)

    # update
    update = """
    UPDATE hardware SET price=8999 WHERE id=1;
    """
    c.execute(update)
    conn.commit()

    # delete
    delete = """
    DELETE FROM hardware WHERE id=1;
    """
    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Bład podłączania do bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
