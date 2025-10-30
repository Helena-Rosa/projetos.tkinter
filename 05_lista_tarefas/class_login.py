import tkinter as tk 
from tkinter import messagebox
from cadastro import Janela_cadastro
import sqlite3



#criando uma classe
class Login():
    def __init__(self, classe_pai):


        #Estou tranformando o 
        self.janela_pai = classe_pai.janela
        self.classe_pai = classe_pai

        #criando uma janela 
        self.janela = tk.Toplevel(self.janela_pai)
        self.janela.title ("Login")
        self.janela.geometry("500x500")


        #configurando para que quando feche a janela de login ele encerre o programa
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)
       
        #texto para escrever as informações de comando (usuario)
        usuario= label_usuario = tk.Label (self.janela,
                                        text= "Usuário:",
                                        font={"success" , 25})
        usuario= label_usuario.pack()



        #campo de espaço para escrever as infomaçoes pedidas (usuario) 
        self.campo_usuario = tk.Entry(self.janela, width=50)
        self.campo_usuario.pack(pady=5)



        #texto para escrever as informações de comando (senha)
        senha= label_senha = tk.Label (self.janela,
                                        text= "Senha:",
                                        font={"success" , 25})
        senha= label_senha.pack()



        #campo de espaço para escrever as informaçoes pedidas (senha)
        self.campo_senha = tk.Entry(self.janela, width=50, show= "*")
        self.campo_senha.pack(pady=5) 


        #função do botão 
        frame_botao = tk.Frame(self.janela)
        frame_botao.pack () 


        #função botão para LOGAR, comando de verificação para ver se esta certo e a posição que o botão LOGAR esta posicionado
        self.botao_teste = tk.Button(frame_botao,text="LOGAR",command= self.verificacao).pack(side="left",pady= 40, padx=20 )

        #função botão para SAIR, comando par confirmar se deseja sair mesmo e a posição que o botão SAIR esta posicionado
        tk.Button(frame_botao,text="SAIR", command=self.sair).pack(side="right", pady= 40, padx=20  )  


        tk.Button(frame_botao, text="CADASTRO", command=self.abrir_tela_cadastro).pack(side="right", pady= 40, padx=20  )  
    
    def run (self):
        self.janela.mainloop


                                 
    #função para verificar se o usuario e senha estãos certos                      
    def verificacao(self):
        usuario=  self.campo_usuario.get()
        senha = self.campo_senha.get()

        conexao= sqlite3.connect("./bd_lista_tarefa.sqlite")

        cursor= conexao.cursor()
        cursor.execute(
            """
            select nome, usuario FROM usuario
                WHERE usuario = ? and senha = ?;
            """,
            [usuario, senha])

        resultado = cursor.fetchone()

        conexao.close()


        #função que informa qual é o usurio correto e a senha correta e a mensagem que aparece se estiver certo
        if resultado:
            messagebox.showinfo("LOGIN","LOGIN EFETUADO")
            self.janela.destroy()
            self.janela_pai.deiconify()
            #estou enviando para a janela de tarefas qual o usuario que logou
            self.classe_pai.usuario_logado= usuario


            # para fechar a primeira pagina 
            self.janela.destroy()

            # para chamar a classe da outra pagina
            #logar= Logar()
            #logar.run()


        # se o login estiver errado 
        else: 
            messagebox.showerror("LOGIN", "LOGIN ERRADO")
        

    #função que confirma se voce deseja realmente sair  




    def abrir_tela_cadastro(self):
        Janela_cadastro(self.janela_pai)

        

        #função que confirma que voce realmente quer sair
    def sair(self): 
        sair=messagebox.askquestion("SAIR", "VOCÊ DESEJA MESMO SAIR?")
        if sair== "yes":
            exit()
            
   

#função para manter a janela aberta 
    def run (self):
        self.janela.mainloop()

if __name__ =="__main__":
    login= Login()
    login.run()
