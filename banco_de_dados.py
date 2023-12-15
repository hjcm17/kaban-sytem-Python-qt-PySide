import sqlite3


class KanbanDB():
    def __init__(self, name = "kanban.db"): # se nenhum argumento for passado o banco terá o nome definido
        
        self.name = name
    
    def conexao(self):
        self.conexao_kanban_db = sqlite3.connect(self.name)
    
    def encerrar_conexao(self):
        try:
            self.conexao_kanban_db.close()
        except:
            pass
    def criar_tabela_usuarios(self):
        try:
            cursor = self.conexao_kanban_db.cursor()
            cursor.execute("""
                           
                CREATE TABLE IF NOT EXISTS usuarios (
                           
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           usuario TEXT UNIQUE NOT NULL,
                           senha TEXT NOT NULL
                           
                );
                           
            """)
        
        except AttributeError:
            print("conexão falhou. faça a conexão")

    def criacao_usuario(self, nome, usuario, senha):
        
        try:
            cursor = self.conexao_kanban_db.cursor()
            cursor.execute("""

                INSERT INTO users(nome, usuario, senha) VALUES(?,?,?)




            """, (nome, usuario, senha))
            self.conexao_kanban_db.commit()
        
        except AttributeError:
            print("conexão falhou. faça a conexão")
    
    def validacao_usuario(self, usuario, senha):

        try:
            cursor = self.conexao_kanban_db.cursor()
            cursor.execute("""

                SELECT * FROM usuarios;

            """)
        for i in cursor.fetchall():
            if i[2].upper() == usuario.upper() and i[3] == senha:
                pass
            else:
                continue
        return "sem acesso"
        
        except:
            pass


if __name__ == "__main__":
    db = KanbanDB()
    db.conexao()
    db.criar_tabela_usuarios()
    db.encerrar_conexao()
