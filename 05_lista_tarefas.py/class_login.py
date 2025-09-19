import tkinter as tk 
from tkinter import messagebox
from class_pagina import Logar


#criando uma classe
class Login():
    def __init__(self):



        #criando uma janela 
        self.janela = tk.Tk()
        self.janela.title ("Login")
        self.janela.geometry("400x400")


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
        frame_botao = tk.Frame()
        frame_botao.pack () 


        #função botão para LOGAR, comando de verificação para ver se esta certo e a posição que o botão LOGAR esta posicionado
        tk.Button(frame_botao,text="LOGAR",command= self.verificacao).pack(side="left",pady= 40, padx=20 )

        #função botão para SAIR, comando par confirmar se deseja sair mesmo e a posição que o botão SAIR esta posicionado
        tk.Button(frame_botao,text="SAIR", command=self.sair).pack(side="right", pady= 40, padx=20  )       
        

                                 
    #função para verificar se o usuario e senha estãos certos                      
    def verificacao(self):
        usuario=  self.campo_usuario.get()
        senha = self.campo_senha.get()


        #função que informa qual é o usurio correto e a senha correta e a mensagem que aparece se estiver certo
        if usuario== "Helena Rosa" and senha == "12345":
            messagebox.showinfo("LOGIN","LOGIN EFETUADO")


            # para fechar a primeira pagina 
            self.janela.destroy()

            # para chamar a classe da outra pagina
            logar= Logar()
            logar.run()


        # se o login estiver errado 
        else: 
            messagebox.showerror("LOGIN", "LOGIN ERRADO")
        

    #função que confirma se voce deseja realmente sair  
    def sair(self): 
        sair=messagebox.askquestion("SAIR", "VOCÊ DESEJA MESMO SAIR?")


        #função que confirma que voce realmente quer sair
        if sair== "yes":
            exit()
             

#função para manter a janela aberta 
    def run (self):
        self.janela.mainloop()

if __name__ =="__main__":
    login= Login()
    login.run()
