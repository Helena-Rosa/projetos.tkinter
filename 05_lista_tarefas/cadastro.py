import ttkbootstrap as ttk
import sqlite3
import tkinter
import tkinter.messagebox


class Janela_cadastro():

    def __init__(self, janela_pai):



        #Criando a janela filha
        self.janela_cadastro = ttk.Toplevel(janela_pai)
    


        #Criando o titulo
        ttk.Label(self.janela_cadastro,
                  text="CADATRO DE USUÁRIO").pack()
        

        #Label do Nome
        ttk.Label(self.janela_cadastro,
                  text="Digite seu nome completo").pack()
        
        #Criando a caixa do texto do nome 
        self.caixinha_nome = ttk.Entry(self.janela_cadastro)
        self.caixinha_nome.pack()


       #Label do Usuario
        ttk.Label(self.janela_cadastro,
                  text="Digite seu ususario").pack()
        
        #Criando a caixa do texto do usuario 
        self.caixinha_usuario = ttk.Entry(self.janela_cadastro)
        self.caixinha_usuario.pack()



        #Label da Senha
        ttk.Label(self.janela_cadastro,
                  text="Digite sua senha").pack()
        
        #Criando a caixa do texto da senha
        self.caixinha_senha = ttk.Entry(self.janela_cadastro)
        self.caixinha_senha.pack()

        #botão
        ttk.Button(self.janela_cadastro, text= "Cadastar", command=self.inserir_usuario).pack()

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):
        #Conectando ao banco de dados 
        conexao= sqlite3.connect ("./bd_lista_tarefa.sqlite")

        #criar cursor
        cursor = conexao.cursor()

        #Execultar o comando
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuario (
                        nome VARCHAR(80),
                        usuario VARCHAR(20) primary key,
                        senha VARCHAR(20)
                    );
                    """)
        
        
        #comito a transação
        conexao.commit()

        #encerro a conexao
        conexao.close()

    def inserir_usuario(self):
        try:
        
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
                                senha)
                            VALUES
                                (?,
                                ?,
                                ?);
                                """,
                                [nome, 
                                usuario, 
                                senha]
            )

            conexao.commit()
            conexao.close()

            tkinter.messagebox.showinfo ("Cadastro Efetuado!")

        except:    
            tkinter.messagebox.showerror("Cadastro", "Erro de Cadastro")
    
   


    def run (self):
        self.janela_cadastro.mainloop()

    
    
if __name__ == "__main__":


    janela_cadastro = Janela_cadastro(ttk.Window())
    janela_cadastro.run()
