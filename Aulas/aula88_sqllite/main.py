import sqlite3

conect = sqlite3.connect('dadabase.db')
cursor = conect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'name TEXT,'
'value REAL'
')')

# input_name = input('Name: ' )
# input_value = input('Value: ')


### INSERIR UM REGISTRO
# cursor.execute('INSERT INTO clientes (name, value) VALUES (?, ?)', (input_name, input_value))
# cursor.execute('INSERT INTO clientes (name, value) VALUES (:name, :value)', 
# {'name': input_name, 'value': input_value}
# )
# cursor.execute('INSERT INTO clientes VALUES (:id, :name, :value)', 
# {'id': None, 'name': input_name, 'value': input_value}
# )
# conect.commit()

### ALTERAR UM REGISTRO
# cursor.execute(
#     'UPDATE clientes SET name=:name WHERE id=:id',
#     {'name': 'Valjunior', 'id': 4}
# )
# conect.commit()

### EXCLUIR UM REGISTRO
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 4}
# )
# conect.commit()

set_value = input('Value: ')

cursor.execute('SELECT * FROM clientes WHERE value > :value', {'value': set_value})

for linha in cursor.fetchall():
    print(linha)


cursor.close()
conect.close()