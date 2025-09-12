import ttkbootstrap as tk

class Janela_principal:
    """Classe para a criação da janela principal"""

    def __init__(self):
    

        #criando uma janela 
        self.janela = tk.Window(themename="vapor")
        self.janela.title ("Janela Rosa")



        # Define o tamanho para 800x600 e a posição inicial
        self.janela.geometry("800x600+100+50")

        #Colocando iconi na janela
        self.janela.iconbitmap("01_Hello_World/estrela.ico")

        # Impede que o usuário redimensione a janela
        self.janela.resizable(False, False)

        #Criando os widget (os componentes)
        self.label_titulo = tk.Label(self.janela,
                                    text = "Hello World!",
                                font ="Arial",
                                foreground = "yellow"  )
        self.label_titulo.pack(pady=50)


        # caixa para digitar o seu nome
        self.label_nome = tk.Label(self.janela,
                            text= "Seja Bem Vindo!")

        self.label_nome.pack(pady=10)


        #Botão para o programa desejar bom dia 
        self.label_nome = tk.Label(self.janela,
                            text= "Digite seu nome:" )
        self.label_nome.pack(pady=10)


        #caixa de texto para a pessoa digitar seu nome 
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.pack(pady=10)

        #funçãomostrar  nome


        #Botão para o programa 
        self.button_bomdia = tk.Button(self.janela,
                                text="Click Aqui!",
                                command= self.desejar_bom_dia)
        self.button_bomdia.pack(pady=20)


        self.label_resultado = tk.Label(self.janela, text="")
        self.label_resultado.pack()





    def run(self):
        """Inicie a janela"""
        #manter a janela aberta
        self.janela.mainloop()



    def desejar_bom_dia(self):
        """Esta função pega o nome digitado na caixa de texto e desejar um bom dia"""
        nome=self.entry_nome.get()
        self.label_resultado.configure(text=f"Bom dia,{nome}")