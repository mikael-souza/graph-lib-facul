import tkinter
from tkinter import *
from PIL import ImageTk,Image
import glob
from viewer import Viewer

janela = Tk()
janela.title('Titulo da janela')
janela.geometry("1280x800")
janela.resizable(width=False, height=False)

image_list = []

for filename in glob.glob(r'C:\Users\NTB-G01\OneDrive - Etec Centro Paula Souza\imagens\*.PNG'):
    imgs = ImageTk.PhotoImage(Image.open(filename))
    image_list.append(imgs)

for img in range(0, len(image_list)):
    if img <= 2:
        Viewer(image_list[img], Label(janela, image=image_list[img]), Label(image=image_list[img], width=420, height=260).grid(row=0, column=img+1))

    if 3 <= img <= 5:
        Viewer(image_list[img], Label(janela, image=image_list[img]), Label(image=image_list[img], width=420, height=260).grid(row=1, column=img-2))

    if 6 <= img <= 8:
        Viewer(image_list[img], Label(janela, image=image_list[img]), Label(image=image_list[img], width=420, height=260).grid(row=2, column=img-5))


def forward(numero_imagem):
    global my_label
    global btn_avancar
    global btn_voltar

    my_label.grid_forget()
    my_label = Label(image=image_list[numero_imagem - 1])
    button_forward = Button(janela, text=">>", command=lambda: forward(numero_imagem + 1))
    button_back = Button(janela, text="<<", command=lambda: back(numero_imagem - 1))

    if numero_imagem == len(image_list):
        button_forward = Button(janela, text=">>", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=3)


def back(image_number):
    global my_label
    global btn_avancar
    global btn_voltar

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(janela, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(janela, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(janela, text="<<", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=3)


btn_voltar = Button(janela, text="<<", command=back, state=DISABLED)
btn_avancar = Button(janela, text=">>", command=lambda: forward(2))

btn_voltar.grid(row=1, column=0)
btn_avancar.grid(row=1, column=4)


janela.mainloop()
