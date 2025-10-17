import tkinter as tk
import sqlite3
from class_login import Login

# classe que criar a segunda pagina do login

class Logar():
    def __init__(self):
        
        # função que mostra a segunda pagina (janela)
        self.janela = tk.Tk()
        self.janela.title ("Janela_pai")
        self.janela.geometry("500x500")


        # função para criar uma segunda janela (minha lista de tarefas)
        label_janela = tk.Label (self.janela,
                                            text= "Minha Lista de Tarefa",
                                            font=("success", 15))
        label_janela.pack()
    

        #função para criar um botão 
        frame_botao = tk.Frame()
        frame_botao.pack (pady=(25,0)) 


        #função que da "estrutura" ao botão (adicionar)
        self.adicionar = tk.Button(frame_botao,text="ADICIONAR",command=self.adicionar)
        self.adicionar.pack(side="left", padx= 20)


        #
        self.entrada = tk.Entry(frame_botao, width=50)
        self.entrada.pack(side="right")


        self.caixa = tk.Listbox(self.janela, font=("success, 12"), height=10)
        self.caixa.pack(pady=20,padx=28,fill="both", expand=True)


        frame_botao = tk.Frame(self.janela)
        frame_botao.pack(side="bottom")


        self.excluir = tk.Button(frame_botao,text="Excluir",command=self.excluir_item)
        self.excluir.pack(side="left", padx= 100)

        self.concluir = tk.Button(frame_botao,text="Concluir", command=self.botao_concluir)
        self.concluir.pack(side="left", padx= 100)

        
        #conectando o banco de dados 
        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        #criando um cursor, responsavel por comandas o bando de dados
        cursor= conexao.cursor()

        sql_para_criar_tabela = """
                                        CREATE TABLE IF NOT EXISTS tarefa (
                                        codigo integer primary key autoincrement,
                                        descricao_tarefa varchar (200),
                                        conclusao boolean
                                        );
                                """
        cursor.execute(sql_para_criar_tabela)

        #comitei as alterações
        conexao.commit()      

        #fechei a conexão
        cursor.close()  
        conexao.close()    


        #abrindo a janela de login
        Login(self.janela)    


        #Escondendo a janela da lista tarefas
        self.janela.withdraw()

        

        self.atualizar_lista()

        

    def atualizar_lista(self):
        #Atualizar a lista
        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor= conexao.cursor()

        sql_para_criar_tabela = """select codigo, descricao_tarefa from tarefa;"""
        
        cursor.execute(sql_para_criar_tabela)

        lista_de_tarefas = cursor.fetchall()

        cursor.close()  
        conexao.close()  

        #inserindo os itens na listbox
        for linha in lista_de_tarefas:
            self.caixa.insert("end",linha [1])


    def adicionar(self):
        dado = self.entrada.get()
        self.caixa.insert(tk.END,dado)

        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor= conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = f"""
                        INSERT INTO tarefa (descricao_tarefa) 
                        VALUES (?)
                     """
        
        cursor.execute(sql_insert,[dado])
        
        conexao.commit()
        cursor.close()
        conexao.close()


    def excluir_item(self):
        escolhido=self.caixa.curselection()
        self.texto = self.caixa.get(escolhido)
        self.caixa.delete(escolhido)
        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor = conexao.cursor()

        cursor.execute ("DELETE FROM tarefa WHERE descricao_tarefa = (?)", (self.texto,))
        conexao.commit()
        conexao.close()
        


    def botao_concluir (self):
        selecionado = self.caixa.curselection()
        self.caixa.itemconfig(selecionado[0], {"bg": "green"})
        
        
        #daqui para baixo é a função para jogar no banco de dados
        conclusao = selecionado[0] + 1
        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor= conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = f"""
                        UPDATE tarefa
                        SET conclusao = 1
                        WHERE codigo = ?
                     """
        
        cursor.execute(sql_insert,[conclusao])
        
        conexao.commit()
        cursor.close()
        conexao.close()
    
    

    # função que mantei a pagina aberta 
    def run (self):
        self.janela.mainloop()


if __name__ =="__main__":
    login= Logar()
    login.run()