import tkinter as tk 
from tkinter import messagebox

class Calculo():
    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title ("Calculadora Corporal")
        self.janela.geometry("400x400")

            
        peso= label_peso = tk.Label (self.janela,
                                        text= "Qual é o seu peso?",
                                        font={"success" , 25})
        peso= label_peso.pack()

        self.campo_entrada1 = tk.Entry(self.janela, width=50)
        self.campo_entrada1.pack(pady=5)
        

        altura= label_altura = tk.Label (self.janela,
                                        text= "Qual é a sua altura?",
                                        font={"success" , 25})
        altura= label_altura.pack()


        self.campo_entrada2 = tk.Entry(self.janela, width=50)
        self.campo_entrada2.pack(pady=5)


        self.vazio = tk.Label(text=""
                              )
    
        self.vazio.pack()

        self.vazio2 = tk.Label (text = "")
        self.vazio2.pack()


        
        tk.Button (self.janela,
                    text="Enviar",
                    command=self.funcao_botao).pack(pady=20)
        
    def funcao_botao(self):

        try:

            peso= self.campo_entrada1.get()
            altura = self.campo_entrada2.get()
            peso = int(peso)
            altura = int(altura)
            altura = (altura/100) **2
            resposta = peso/altura 
            self.vazio.configure(text = (f"{resposta: .2f}"))
        except: 
            tk.messagebox.showerror("erro","valor invalido")
            
        if resposta >=18.5 and resposta <25:
            self.vazio2.configure(text="peso ideal")
        elif resposta >=25:
            self.vazio2.configure(text="acima do peso")
        else:
            self.vazio2.configure(text="abaixo do peso")

        



    def run (self):
        self.janela.mainloop()

 

if __name__ =="__main__":
    calc = Calculo()
    calc.run()




    