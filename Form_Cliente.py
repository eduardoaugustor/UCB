import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    # Aqui você pode adicionar a lógica de validação e salvar os dados do cliente
    messagebox.showinfo("Informação", f"Cliente {name} cadastrado com sucesso!")

# Cria a janela principal
root = tk.Tk()
root.title("Formulário de Cliente")

# Cria os widgets do formulário
label_name = tk.Label(root, text="Nome:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_phone = tk.Label(root, text="Telefone:")
label_phone.grid(row=2, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Executa o loop principal do Tkinter
root.mainloop()
