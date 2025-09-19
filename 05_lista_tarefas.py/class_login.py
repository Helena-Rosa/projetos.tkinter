import tkinter as tk 
from tkinter import messagebox


#criando uma classe
class Login():
    def __init__(self):


#criando uma janela 
        self.janela = tk.Tk()
        self.janela.title ("Login")
        self.janela.geometry("400x400")

        usuario= label_peso = tk.Label (self.janela,
                                        text= "Usuário:",
                                        font={"success" , 25})
        usuario= label_peso.pack()



        self.campo_entrada1 = tk.Entry(self.janela, width=50)
        self.campo_entrada1.pack(pady=5)


       



        senha= label_senha = tk.Label (self.janela,
                                        text= "Senha:",
                                        font={"success" , 25})
        senha= label_senha.pack()


       


        self.campo_entrada2 = tk.Entry(self.janela, width=50)
        self.campo_entrada2.pack(pady=5)



        frame_botao = tk.Frame()
        frame_botao.pack () 

        tk.Button(frame_botao,text="LOGAR",command= self.verificacao).pack(side="left",pady= 40, padx=20 )
        tk.Button(frame_botao,text="SAIR", command=self.sair).pack(side="right", pady= 40, padx=20  )       
        

                                 
                            
    def verificacao(self):
        usuario=  self.campo_entrada1.get()
        senha = self.campo_entrada2.get()


        if usuario== "Helena Rosa" and senha == "12345":
            messagebox.showinfo("LOGIN","LOGIN EFETUADO")

        else: 
            messagebox.showerror("LOGIN", "LOGIN ERRADO")
        

       
    def sair(self): 
        sair=messagebox.askquestion("SAIR", "VOCÊ DESEJA MESMO SAIR?")


        if sair== "yes":
            exit()
             



         

    def run (self):
        self.janela.mainloop()

 

if __name__ =="__main__":
    login= Login()
    login.run()
