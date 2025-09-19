import tkinter as tk

# classe que criar a segunda pagina do login
class Logar():
    def __init__(self):
        
        # função que mostra a segunda pagina (janela)
        self.janela = tk.Tk()
        self.janela.title ("Login")
        self.janela.geometry("400x400")

 
    # função que mantei a pagina aberta 
    def run (self):
            self.janela.mainloop()