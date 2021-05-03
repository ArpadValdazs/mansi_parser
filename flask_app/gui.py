from tkinter import *
from tkinter import filedialog
from adapter2 import call_adapter


def load_button():
    parse_mode = mode.get()
    filename = file_input.get()
    if filename:
        if parse_mode == 0:
            array = call_adapter(filename, "nodiacritics")
            perform_table(array)
        elif parse_mode == 1:
            call_adapter(filename, "strict")
        print(parse_mode)
    else:
        pass


def open_file():
    #  lbl5.configure(text="filepath")
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    file_input.insert(0, filepath)


def save_file():
    with open("time.csv", "w") as table:
        table.write('morphemes\tglosses\r\n')
        for elem in range(len(array)):
            table.write(array[elem][0][0] + '\t' + array[elem][1][0] + '\r\n')


window = Tk()
window["bg"] = "#FFFFFF"
window.title("Corrector")
window.geometry('1024x768')
mode = IntVar()
diacr = Radiobutton(window, text='С диакритиками (Луима)', value="1", variable=mode)
nodiacr = Radiobutton(window, text='Без диакритиков (Чернецов)', value="0", variable=mode)
diacr.grid(column=2, row=0)
nodiacr.grid(column=3, row=0)
load_btn = Button(window, text="Загрузить", command=open_file)
parse_btn = Button(window, text="ПАРСИТЬ", command=load_button, bg="red", fg="white", font="bold")
file_input = Entry(window, width=40)
file_input.grid(column=1, row=0)
load_btn.grid(column=0, row=0)
parse_btn.grid(column=4, row=0)

save_btn = Button(window, text="Сохранить как xls...", command=save_file, bg="green", fg="white", font="bold")
save_btn.grid(column=8, row=0)


def perform_table(array):
    for i in range(len(array)):
        sentence = Entry(window, width=400)
        sentence.grid(column=0, row=1 + i)
        sentence.insert(0, str(array[i][0]))
        translation = Entry(window, width=400)
        translation.grid(column=1, row=1 + i)
        translation.insert(0, str(array[i][1]))
        # lbl = Label(window, text=array[i][0], bg="#FFFFFF")
        #
        # lbl = Label(window, text=array[i][1], bg="#FFFFFF")
        # lbl.grid(column=1, row=1+i)


# lbl = Label(window, text="Sentence 1", bg="#FFFFFF")
# lbl.grid(column=0, row=1)
# lbl = Label(window, text="Sentence 2", bg="#FFFFFF")
# lbl.grid(column=0, row=2)
#
# lbl = Label(window, text="Translation 1", bg="#FFFFFF")
# lbl.grid(column=1, row=1)
# lbl = Label(window, text="Translation 2", bg="#FFFFFF")
# lbl.grid(column=1, row=2)

window.mainloop()

