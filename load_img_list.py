import os
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import tkinter
import glob

root = Tk()
root.title('Selecionar arquivos: ')
root.geometry('720x480')

def walk_dir(root_dir, extension):
    file_list = []
    towalk = [root_dir]
    while towalk:
        root_dir = towalk.pop()
        for path in os.listdir(root_dir):
            full_path = os.path.join(root_dir, path).lower()
            if os.path.isfile(full_path) and full_path.endswith(extension):
                file_list.append((path.lower(), root_dir))
    return file_list

def get_list(event):
    global listbox1
    try:
        global selpath
        sel = listbox1.curselection()
        selpath = [file_list[int(x)] for x in sel]
    except:
        info_label.config(text="Please select a file on the list")

def add_file():
    global file_num
    global root_dir
    global btn_avancar
    global btn_voltar
    global btn_select

    try:
        root.destroy()
        
        janela = Tk()
        janela.title('Galeria')
        janela.geometry('720x480')

        image_list = []

        my_label = Label(image=None)

        # def selected_folder():

        for path_tuple in selpath:
            # listbox2.insert(END, path_tuple[0])
            fullpath_list.append(path_tuple)

            img = ImageTk.PhotoImage(Image.open(root_dir+'/'+path_tuple[0]).resize((662, 440), Image.ANTIALIAS))
            image_list.append(img)

        my_label.configure(image=image_list[0])
        my_label.image = image_list[0]
        my_label.grid(row=0, column=1, columnspan=2)
        


        def selected_folder():
            path = filedialog.askdirectory()
            for path_tuple in selpath:
            # listbox2.insert(END, path_tuple[0])
                fullpath_list.append(path_tuple)

                img = ImageTk.PhotoImage(Image.open(root_dir+'/'+path_tuple[0]).resize((662, 440), Image.ANTIALIAS))
                image_list.append(img)
            print(image_list)

            
            my_label.configure(image=image_list[0])
            my_label.image = image_list[0]
            my_label.grid(row=0, column=1, columnspan=2)
            btn_select.grid(row=1, column=1, columnspan=2)
            btn_voltar.grid(row=0, column=0)
            btn_avancar.grid(row=0, column=3)



        def forward(num_imagem):
            global my_label
            global btn_avancar
            global btn_voltar
            global btn_select

            my_label = Label(image=None)

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

            my_label = Label(image=None)

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

        

    except NameError:
        if file_num <=0:
            root_dir = root_dir
            print(root_dir)
        else:
            tkinter.messagebox.showwarning(title='Aviso', message='Por favor, selecione ao menos um arquivo da lista!')


imgs = [] 
listbox1 = Listbox(root, width=80, height=6, selectmode=EXTENDED)
listbox1.grid(row=0, column=0)


listbox2 = Listbox(root, width=80, height=6)

yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL)
yscroll.grid(row=0, column=1, sticky=N+S+W)
listbox1.configure(yscrollcommand=yscroll.set)

add_button = Button(root, text='Carregar imagens', command=add_file)
add_button.grid(row=2, column=0, pady=5, sticky=W)

info_label = Label(fg='red')
info_label.grid(row=3, column=0, pady=5, sticky=W)

fullpath_list = []

root_dir = filedialog.askdirectory()
extension = ['.png','.jpg']
file_list = []
for ext in extension:
    file_list = file_list + walk_dir(root_dir, ext)

file_list.sort()

for file in file_list:
    listbox1.insert(END, file[0])
    
file_num = len(file_list)
if  file_num > 0:
    info = "%s" % (root_dir)
else:
    info = "%s" % (root_dir)
    tkinter.messagebox.showwarning(title='Aviso', message="Não há arquivos de imagens em %s" % (root_dir))
    pass

info_label.config(text=info)

listbox1.bind('<ButtonRelease-1>', get_list)


root.mainloop()

