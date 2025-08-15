import tkinter as tk

#criando uma janela 
janela = tk.Tk()
janela.title ("Janela Rosa")

#Altera a cor de fundo da janela
janela.configure(bg="#FACADA")

# Define o tamanho para 800x600 e a posição inicial
janela.geometry("800x600+100+50")

#Colocando iconi na janela
janela.iconbitmap("01_Hello_World/estrela.ico")

# Impede que o usuário redimensione a janela
janela.resizable(False, False)

#Criando os widget (os componentes)
label_titulo = tk.Label(janela,
                        text = "Hello World!",
                        bg= "purple",
                        font ="Arial",
                        foreground = "yellow"  )
label_titulo.pack()


# caixa para digitar o seu nome
label_nome = tk.Label(janela,
                      text= "Digite o seu nome")

label_nome.pack()


#Botão para o programa desejar bom dia 
label_nome = tk.Label(janela,
                      text= "Bom dia" )
label_nome.pack()


#caixa de texto para a pessoa digitar seu nome 
entry_nome = tk.Entry (janela)
entry_nome.pack()

#Botão para o programa 







#Loop para manter a janela aberta
janela.mainloop()

