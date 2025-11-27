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


        class Janela_imc():
    def __init__(self):
        self.janela = ttk.Window(themename="superhero") 
        self.janela.title("Calculadora de IMC")
        self.janela.geometry("800x400")

        # para o peso
        self.label_peso = ttk.Label(self.janela, text="Peso (kg):")
        self.label_peso.pack()
        self.entry_peso = ttk.Entry(self.janela)
        self.entry_peso.pack()
        # para a altura
        self.label_altura = ttk.Label(self.janela, text="Altura (m):")
        self.label_altura.pack()
        self.entry_altura = ttk.Entry(self.janela)
        self.entry_altura.pack()

        self.label_resultado = ttk.Label(self.janela, text="")
        self.label_resultado.pack()
        botao_calcular = ttk.Button(self.janela,text='Calcular IMC',command=self.calcular_imc)
        botao_calcular.pack()


    def calcular_imc(self):
        try:
            peso_str = self.entry_peso.get()
            altura_str = self.entry_altura.get()
            peso = float(peso_str)
            altura= float(altura_str)
            imc = peso / altura**2
        except:
            tkinter.messagebox.showerror(title="ERRO", message="Você digitou um valor inválido.")
            imc = round(imc,2)
        if imc < 18.5:
            self.label_resultado.config( text="Você está abaixo do peso")
        
        elif imc >= 18.5 and imc <= 24.9:
            self.label_resultado.config( text="Você é normoponderal")
        
        elif imc >= 25 and imc <=29.9:
            self.label_resultado.config(text="Você está na pré-obesidade")
            
        elif imc >= 30 and imc <= 34.9:
            self.label_resultado.config(text="Você está com obesidade, grau I")
            
        elif imc >=35 and imc <=39.9:
            self.label_resultado.config(text="Você está com obesidade, grau II")
        
        else:
            self.label_resultado.config(text="Você está com obesidade mórbida")
    def run(self):
        self.janela.mainloop()

    


    def run (self):
        self.janela.mainloop()

 

if __name__ =="__main__":
    calc = Calculo()
    calc.run()








    