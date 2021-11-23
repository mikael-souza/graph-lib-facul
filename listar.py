import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import glob
from tkinter import filedialog as fd

janela = Tk()
janela.title('Galeria')
janela.geometry('720x480')


image_list = []

my_label = Label(image=None)
my_label.grid(row=0, column=1, columnspan=2)


def load_images():
    image_list = []
    root_dir = filedialog.askdirectory()

    for filename in glob.glob(str(root_dir)+'/*.png'):
        img = ImageTk.PhotoImage(Image.open(filename).resize((662, 440), Image.ANTIALIAS))
        image_list.append(img)
        print(image_list[0])

    my_label.grid_forget()
    my_label.configure(image=image_list[0])
    my_label.image = image_list[0]
    my_label.grid(row=0, column=1, columnspan=2)

    if len(image_list) > 1:
        btn_avancar = Button(janela, text=">>", command=lambda: forward(2))
        btn_avancar.grid(row=0, column=3)



    def forward(num_imagem):
        global my_label
        global btn_avancar
        global btn_voltar

        my_label.grid_forget()
        my_label = Label(image=str(image_list[num_imagem - 1]))
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



    btn_voltar = Button(janela, text="<<", command= back, state=DISABLED)
    btn_avancar = Button(janela, text=">>", command= forward(2), state=DISABLED)
    # btn_avancar = Button(janela, text=">>", command=lambda: forward(2))
    btn_select = Button(janela, text="Selecionar pasta", command=lambda: load_images())

    btn_voltar.grid(row=0, column=0)
    btn_avancar.grid(row=0, column=3)
    btn_select.grid(row=1, column=1, columnspan=2)


btn_select = Button(janela, text="Selecionar pasta", command=lambda: load_images())
btn_select.grid(row=1, column=1, columnspan=2)

janela.bind("<Return>", load_images)
janela.mainloop()
