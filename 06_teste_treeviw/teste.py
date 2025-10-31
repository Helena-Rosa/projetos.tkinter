import ttkbootstrap as ttk

jenela = ttk.Window(themename="darkly")

treeview = ttk.Treeview(jenela)
treeview.pack()

treeview["columns"]=("nome", "idade", "cidade")
treeview["show"] = "headings"

treeview.heading("nome", text= "Nome Completo")
treeview.heading("idade", text= "Idade")
treeview.heading("cidade", text="Cidade")

treeview.column("nome", width=200)

treeview.insert("", "end", values= ["Godofredo Silva", "28", "São Paulo"])
treeview.insert("", "end", values= ["Maria Oliveira", "34", "Rio de Janeiro"])
treeview.insert("", "end", values= ["Ana Paula", "23", "Belo Horizonte"])
treeview.insert("", "end", values= ["João Souza", "45", "Curutiba"])

ttk.Button(janela, text="imprimir valores", command=lambda: print(treeview.item()))