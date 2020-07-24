import sqlite3

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('scp.db')

cursor = connection.cursor()

# ------------------------------------------------------------------------------------
# Structure
# ------------------------------------------------------------------------------------

#cursor.execute("CREATE TABLE scp_item (number text, level text, description text)")

# ------------------------------------------------------------------------------------
# Inserts
# ------------------------------------------------------------------------------------

#cursor.execute("INSERT INTO  scp_item VALUES('SCP-002', 'EUCLIDEO', '...')")
#cursor.execute("INSERT INTO  scp_item VALUES('SCP-003', 'EUCLIDEO', '...')")

# scps = [('SCP-004', 'EUCLIDEO', '...'),
#        ('SCP-005', 'SEGURO', '...'),
#        ('SCP-006', 'SEGURO', '...')]
#cursor.executemany("INSERT INTO scp_item VALUES(?, ?, ?)", scps)

# ------------------------------------------------------------------------------------
# Selects
# ------------------------------------------------------------------------------------


def print_itens(items):
    print('Id\t\tNumber\t\tClass')
    print('--\t\t-----\t\t-----')
    for item in items:
        print(str(item[0]) + '\t\t' + item[1] + '\t\t' + item[2])


def display_query(sql):
    cursor.execute(sql)
    items = cursor.fetchall()
    print_itens(items)
    print("\n")


display_query("SELECT rowid, * FROM scp_item")

#cursor.execute("SELECT rowid, * FROM scp_item WHERE level = 'SEGURO'")
#items = cursor.fetchall()
# print_itens(items)

# print("\n")

#cursor.execute("SELECT rowid, * FROM scp_item WHERE level LIKE '%O'")
#items = cursor.fetchall()
# print_itens(items)

# ------------------------------------------------------------------------------------
# Updates
# ------------------------------------------------------------------------------------

#cursor.execute("UPDATE scp_item SET level = 'EUCLIDEO' WHERE number = 'SCP-006' ")
#display_query("SELECT rowid, * FROM scp_item")

# ------------------------------------------------------------------------------------
# Delete
# ------------------------------------------------------------------------------------

#cursor.execute("DELETE FROM scp_item WHERE number = 'SCP-006'")
# connection.commit()
#display_query("SELECT rowid, * FROM scp_item")

connection.commit()
connection.close()
