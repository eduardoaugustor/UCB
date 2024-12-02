import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tela de Login')
        
        # Configuração da janela
        self.root.geometry('300x200')
        self.root.resizable(False, False)
        
        # Label e Entry para Usuário
        self.label_user = tk.Label(root, text='Usuário:')
        self.label_user.pack(pady=10)
        self.entry_user = tk.Entry(root)
        self.entry_user.pack(pady=5)

        # Label e Entry para Senha
        self.label_password = tk.Label(root, text='Senha:')
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show='*')
        self.entry_password.pack(pady=5)

        # Botão de Login
        self.btn_login = tk.Button(root, text='Login', command=self.check_login)
        self.btn_login.pack(pady=20)
        
    def check_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()
        
        # Verificação simples de usuário e senha (exemplo)
        if user == 'admin' and password == 'admin':
            messagebox.showinfo('Login', 'Login realizado com sucesso!')
        else:
            messagebox.showerror('Erro', 'Usuário ou senha incorretos.')

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
