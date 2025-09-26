import tkinter as tk

# classe que criar a segunda pagina do login
class Logar():
    def __init__(self):
        
        # função que mostra a segunda pagina (janela)
        self.janela = tk.Tk()
        self.janela.title ("Login")
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

        self.cocluir = tk.Button(frame_botao,text="Concluir", command=self.botao_concluir)
        self.cocluir.pack(side="left", padx= 100)



    def adicionar(self):
        dado = self.entrada.get()
        self.caixa.insert(tk.END,dado)

    def excluir_item(self):
        escolhido=self.caixa.curselection()
        self.caixa.delete(escolhido)


    def botao_concluir (self):
        selecionado = self.caixa.curselection()
        self.caixa.itemconfig(selecionado[0], {"bg": "green"})
         

    # função que mantei a pagina aberta 
        def run (self):
            self.janela.mainloop()


if __name__ =="__main__":
    login= Logar()
    login.run()