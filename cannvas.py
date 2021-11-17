from tkinter import *
from PIL import ImageTk, Image
import glob
import os

janela = Tk()
janela.title('Mikael Test')

canvas = Canvas(janela, width=1280, height=800)
canvas.pack()

image_list = []

for filename in glob.glob(r'C:\Users\NTB-G01\OneDrive - Etec Centro Paula Souza\imagens\*.png'):
# filename = r"C:\Users\NTB-G01\OneDrive - Etec Centro Paula Souza\imagens\English.png"
    img = ImageTk.PhotoImage(Image.open(filename).resize((400, 260), Image.ANTIALIAS))
    image_list.append(img)


for imgg in image_list:
    canvas.create_image(20, 20, anchor=NW, image=imgg)
    canvas.create_image(242, 20, anchor=NW, image=imgg)
    canvas.create_image(464, 20, anchor=NW, image=imgg)
    canvas.create_image(20, 290, anchor=NW, image=imgg)
    canvas.create_image(242, 290, anchor=NW, image=imgg)
    canvas.create_image(464, 290, anchor=NW, image=imgg)
    mainloop()
