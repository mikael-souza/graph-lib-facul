from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import glob

janela = Tk()
janela.title('Mikael Test')

image_list = []


def selected_folder():
    janela.grid = None
    path = filedialog.askdirectory()
    return path


for filename in glob.glob(rf'{selected_folder()}/*.jpg'):
    img = ImageTk.PhotoImage(Image.open(filename).resize((400, 260), Image.ANTIALIAS))
    image_list.append(img)

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=1, columnspan=2)


def forward(num_imagem):
    global my_label
    global btn_avancar
    global btn_voltar

    my_label.grid_forget()
    my_label = Label(image=image_list[num_imagem - 1])
    btn_avancar = Button(janela, text=">>", command=lambda: forward(num_imagem + 1))
    btn_voltar = Button(janela, text="<<", command=lambda: back(num_imagem - 1))

    if num_imagem == len(image_list):
        btn_avancar = Button(janela, text=">>", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    btn_voltar.grid(row=0, column=0)
    btn_avancar.grid(row=0, column=3)


def back(image_number):
    global my_label
    global btn_avancar
    global btn_voltar

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    btn_avancar = Button(janela, text=">>", command=lambda: forward(image_number + 1))
    btn_voltar = Button(janela, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        btn_voltar = Button(janela, text="<<", state=DISABLED)

    my_label.grid(row=0, column=1, columnspan=2)
    btn_voltar.grid(row=0, column=0)
    btn_avancar.grid(row=0, column=3)


btn_voltar = Button(janela, text="<<", command=back, state=DISABLED)
btn_avancar = Button(janela, text=">>", command=lambda: forward(2))
btn_select = Button(janela, text="Selecionar pasta", command=lambda: selected_folder())

btn_voltar.grid(row=0, column=0)
btn_avancar.grid(row=0, column=3)
btn_select.grid(row=1, column=1, columnspan=2)

janela.mainloop()
