from tkinter import *
import tkinter.messagebox
import sqlite3

login = Tk()
login.geometry('720x480')
login.title("Login")


def user_verify():

    conexao = sqlite3.connect("dev-base.db")
    cursor = conexao.cursor()

    sqlite_select_query = """SELECT cpf,senha from Usuario"""
    cursor.execute(sqlite_select_query)
    users = cursor.fetchall()

    for user in users:
        print(user[0], user[1])
        if str(user[0]) == cpf.get() and str(user[1]) == password.get():
            from visualizar import visualizar
            visualizar
        else:
            tkinter.messagebox.showwarning(title='Falha na Autenticação:', message='Usuário ou Senha incorreta!')


Label(login, text="CPF          :").grid(row=0)
Label(login, text="Password :").grid(row=1)

cpf = Entry(login)
password = Entry(login)

cpf.grid(row=0, column=1)
password.grid(row=1, column=1)

btn_quit = Button(login, text='Sair', command=login.quit).grid(row=5, column=2, sticky=tkinter.W, pady=4)
btn_verify = Button(login, text='Exibir Dados', command=lambda: user_verify()).grid(row=5, column=1, sticky=tkinter.W, pady=4)

login.mainloop()
