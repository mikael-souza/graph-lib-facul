import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import glob

janela = Tk()
janela.title('Galeria')
janela.geometry('720x480')

image_list = []

my_label = Label(image=None)


def selected_folder():
    global image_list
    image_list = []
    path = filedialog.askdirectory()

    for filename in glob.glob(rf'{path}/*.png'):
        img = ImageTk.PhotoImage(Image.open(filename).resize((662, 440), Image.ANTIALIAS))
        image_list.append(img)
    print(len(image_list))

    my_label.configure(image=image_list[0])
    my_label.image = image_list[0]
    my_label.grid(row=0, column=1, columnspan=2)


def forward(num_imagem):
    global my_label
    global btn_avancar
    global btn_voltar
    global btn_select

    if image_list == image_list:
        my_label.grid_forget()

    my_label = Label(image=image_list[num_imagem - 1])
    btn_avancar = Button(janela, text=">>", command=lambda: forward(num_imagem + 1))
    btn_voltar = Button(janela, text="<<", command=lambda: back(num_imagem - 1))
    btn_select = Button(janela, text="Selecionar pasta", command=lambda: selected_folder())

    if num_imagem == len(image_list):
        btn_avancar = Button(janela, text=">>", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    btn_select.grid(row=1, column=1, columnspan=2)
    btn_voltar.grid(row=0, column=0)
    btn_avancar.grid(row=0, column=3)



def back(image_number):
    global my_label
    global btn_avancar
    global btn_voltar
    global btn_select

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    btn_avancar = Button(janela, text=">>", command=lambda: forward(image_number + 1))
    btn_voltar = Button(janela, text="<<", command=lambda: back(image_number - 1))
    btn_select = Button(janela, text="Selecionar pasta", command=lambda: selected_folder())

    if image_number == 1:
        btn_voltar = Button(janela, text="<<", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    btn_select.grid(row=1, column=1, columnspan=2)
    btn_voltar.grid(row=0, column=0)
    btn_avancar.grid(row=0, column=3)



btn_voltar = Button(janela, text="<<", command=back, state=DISABLED)
btn_avancar = Button(janela, text=">>", command=lambda: forward(2))
btn_select = Button(janela, text="Selecionar pasta", command=lambda: selected_folder())

btn_voltar.grid(row=0, column=0)
btn_avancar.grid(row=0, column=3)
btn_select.grid(row=1, column=1, columnspan=2)

janela.bind("<Return>", selected_folder)
janela.mainloop()
