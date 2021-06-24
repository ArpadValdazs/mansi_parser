import os
import re

diacritics = ["ō", "ē", "ū", "ā", 'ī']
letters = ["o", "e", "u", "a", "i"]

chernetsov = ["ɧ", "ь", "ņ", "ꞩ", "t̩" "l̩", "ś", "h", "H", "Ņ", "Ļ", "Ś", "A", "E", "I", "K", "L", "M", "N", "O", "P", "S", "T", "U", "R", "W", "V", "v", "y", "J"]
proj_orph = ["ɣ", "ə", "n'", "ɕ", "t'" "l'", "ɕ", "x", "x", "n'", "l'", "ɕ", "a", "e", "i", "k", "l", "m", "n", "o", "p", "s", "t", "u", "r", "w", "w", "w", "u", "j"]

def corrector(text, type):
    symbols_array = []
    new_text = ""
    text = text.replace("n̩", "n'")
    text = text.replace("n̩̩", "n'")
    text = text.replace("l̩", "l'")
    text = text.replace("t̩", "t'")
    text = text.replace("k̩", "k")
    text = text.replace("Ņ", "n'")
    text = text.replace("Ļ", "l'")
    text = text.replace("Ț", "t'")
    text = text.replace("Ꞩ", "ɕ'")
    text = text.replace("\u030A", "")
    text = text.replace("\u0022", "")
    text = text.replace("=", " ")
    text = text.replace(" -", "")
    text = text.replace("- ", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    if text[-1] == ".":
        text = text[:-1]
    for i in range(len(text)):
        if type == "chern" and text[i] in chernetsov:
            for j in range(len(chernetsov)):
                if chernetsov[j] == text[i]:
                    text = text.replace(text[i], proj_orph[j])
    return text

def parser(filename_in, mode):
    data_file = []
    os.chdir("texts")
    print(os.getcwd())
    filename = os.getcwd()+"/"+filename_in
    print(filename)

    # Открыли, прочитали, получили список
    with open(filename, 'r', encoding="utf-8") as read_file:
        for line in read_file:
            data_file.append(line.strip('\n'))
    string = "\n".join(data_file)
    prepared_text = corrector(string, mode)
    os.chdir("../")
    return(prepared_text)


def init_function(filename, mode):
    text = parser(filename, mode)
    # print(text)
    return text

#text = init_function()
#print(text)

