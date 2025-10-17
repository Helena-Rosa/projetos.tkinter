import ttkbootstrap as ttk


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



        def run (self):
            self.janela_cadastro.mainloop()


    if_name_ == "_main_":


    janela_cadastro = Janaela_cadastro(ttk.Window())
    janela_cadastro.run()
