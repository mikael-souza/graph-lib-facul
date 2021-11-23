from tkinter import *
import tkinter
import sqlite3

cadastro = Tk()
cadastro.geometry('720x480')
cadastro.title("Cadastro de Usuários")
# cadastro["bg"] = "white"

def cadastrar_usuario():
    try:
        conexao = sqlite3.connect("dev-base.db")
        cursor = conexao.cursor()

        sql_query = f"insert into Usuario(nome, cpf, email,  senha) values('mika', '{cpf.get()}', 'mika@mikaelsoua.com', '{senha.get()}')"

        cursor.execute(sql_query)
        conexao.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if sqlite3.connect:
            cursor.close()
            print("Conexão Fechada!")

    print("Nome: %s" % (cpf.get()))
    print("Password: %s" % (senha.get()))

Label(cadastro, text="Nome    :").grid(row=0)
Label(cadastro, text="CPF        :").grid(row=1)
Label(cadastro, text="E-mail   :").grid(row=2)
Label(cadastro, text="Usuario :").grid(row=3)
Label(cadastro, text="Senha   :").grid(row=4)

nome = Entry(cadastro)
cpf = Entry(cadastro)
email = Entry(cadastro)
usuario = Entry(cadastro)
senha = Entry(cadastro)

nome.grid(row=0, column=1)
cpf.grid(row=1, column=1)
email.grid(row=2, column=1)
usuario.grid(row=3, column=1)
senha.grid(row=4, column=1)

btn_quit = Button(cadastro, text='Sair', command=cadastro.quit).grid(row=5, column=2, sticky=tkinter.W, pady=4)
btn_create_user = Button(cadastro, text='Cadastrar', command=lambda: cadastrar_usuario()).grid(row=5, column=1, sticky=tkinter.W, pady=4)

cadastro.mainloop()
