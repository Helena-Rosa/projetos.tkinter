import ttkbootstrap as ttk 
from classe_bot_gemini import Gemini_Bot
class Janela_chat():
    def __init__(self):
        #criando a janela 
        self.janela= ttk.Window(themename="vapor",
                       title = "Dona Rosa")
        self.janela.geometry ("1000x800")

        self.label_titulo = ttk.Label(self.janela,
                                    text = "OLÁ, SEJA BEM VINDO(A)",
                                    font = "Stencil",
                                    foreground = "yellow")
        self.label_titulo.pack(pady= 10)

        
        self.label_titulo = ttk.Label(self.janela,
                                    text = "Venha Aprender a fazer o melhor Brownie do Mundo!",
                                    font ="Perpetua",
                                    foreground = "pink")
        self.label_titulo.pack(pady= 20)
        

        self.label_titulo = ttk.Label(self.janela,
                                    text = "Qual é a sua dúvida?",
                                    font ="Century",
                                    foreground = "orange")
        self.label_titulo.pack(pady= 20)


        ttk.Button (self.janela,
                    text="Enviar",
                    style="danger").pack(pady=20)
        
        label_resposta = ttk.Label (self.janela,
                                    text= "RESPOSTA",
                                    style= "success")
        label_resposta.pack(pady=(20,0))

    #crinado o objeto robo(instanciando uma class)
        self.robo = Gemini_Bot


    def responder (self):
        pergunta = self.entry_pergunta.get()
        resposta = self.robo.enviar_mensagem (pergunta)
        self.label_resposta.config(text=resposta)


    
    
    def run (self):
        self.janela.mainloop()

 

if __name__ =="__main__":
    chat = Janela_chat()
    chat.run()

    
