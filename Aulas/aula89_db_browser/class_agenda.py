import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, name, phone_number):
        query = 'INSERT OR IGNORE INTO agenda (name, phone_number) VALUES (:name, :phone_number)'
        self.cursor.execute(query, {'name': name, 'phone_number': phone_number})
        self.conn.commit()


    def editar(self, name, phone_number, id):
        query = 'UPDATE OR IGNORE agenda SET name=:name, phone_number=:phone_number WHERE id=:id '
        self.cursor.execute(query, {'name': name, 'phone_number': phone_number, 'id': id})
        self.conn.commit()
        


    def excluir(self, id):
        query = 'DELETE FROM agenda WHERE id=:id '
        self.cursor.execute(query, {'id': id})
        self.conn.commit()
    
    
    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        
        for linha in self.cursor.fetchall():
            print(linha)
    
    
    def seach(self, value):
        query = 'SELECT * FROM agenda WHERE name LIKE ?'
        self.cursor.execute(query, (f'%{value}%',))
        
        for linha in self.cursor.fetchall():
            print(linha)
