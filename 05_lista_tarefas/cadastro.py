import ttkbootstrap as ttk
import sqlite3


class Janela_cadastro():

    def _init_(self, janela_pai):



        #Criando a janela filha
        self.janela_cadastro = ttk.Toplevel(janela_pai)


        #Criando o titulo
        ttk.Label(self.janela_cadastro,
                  text="CADATRO DE USUÁRIO").pack()
        

        #Label do Nome
        ttk.Label(self.janela_cadastro,
                  text="Digite seu nome completo").pack()
        
        #Criando a caixa do texto do nome 
        caixinha_nome = ttk.Entry(self.janela_cadastro)
        caixinha_nome.pack()



       #Label do Usuario
        ttk.Label(self.janela_cadastro,
                  text="Digite seu ususario").pack()
        
        #Criando a caixa do texto do usuario 
        caixinha_usuario = ttk.Entry(self.janela_cadastro)
        caixinha_usuario.pack()




        #Label da Senha
        ttk.Label(self.janela_cadastro,
                  text="Digite sua senha").pack()
        
        #Criando a caixa do texto da senha
        caixinha_senha = ttk.Entry(self.janela_cadastro)
        caixinha_senha.pack()

        #botão
        ttk.Button(self.janela_cadastro, text= "Cadastar").pack()

        def criar_tabela_usuario():
            #Conectando ao banco de dados 
            conexao= sqlite3.connect ("./bd_lista_tarefas.sqlite")

        #criar cursor
        cursor = conexao.cursor()

        #Execultar o comando
        cursor.execute("""
                    CREATE TABLE usuario (
                        nome VARCHAR(80),
                        usuario VARCHAR (20),
                        senha VARCHAR(20)
                       );
                    """)
        
        #comito a transação
        conexao.commit()

        #encerro a conexao
        conexao.close()

    def inserir_usuario(self):
        
        #crir conexao
        conexao = sqlite3.connect ("./bd_lista_tarefa.sqlite")


    #criar cursor
    cursor = conexao.cursor()
    
    nome =  self.caixinha_nome.get()
    usuario = self.caixinha_usuario.get()
    senha = self.caixinha_senha.get()
    


        #execultar
    cursor.execute("""
                      INSERT INTO usuario
                        (nome,
                        usuario,
                        enha)
                    VALUES
                        (?,
                         ?,
                         ?);
                        """,
                        [nome, 
                         usuario, 
                         senha]
    )





    def run (self):
        self.janela_cadastro.mainloop()

    
    
if __name__ == "__main__":


    janela_cadastro = Janela_cadastro(ttk.Window())
    janela_cadastro.run()
