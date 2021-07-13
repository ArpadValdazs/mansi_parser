import os

# Надо взять по одному их, и разбросать по разным концам массива

def show_texts(name, serverURL):
    print("1: ", os.getcwd())
    print("2: ", serverURL)
    if os.getcwd() == serverURL:
        os.chdir('database/' + name + '/texts')
    else:
        os.chdir('texts')
    # if os.getcwd() == serverURL + '/database':
    #     os.chdir(name + '/texts')
    # if os.getcwd() == serverURL + '/database' + name + '/texts':
    #     print(os.getcwd())
    #     os.chdir("../")
    #     os.chdir('texts')
    # else:
    # os.chdir('database/' + name + '/texts')
    #print("2", os.getcwd())
    dirlist = os.listdir()
    #print("LOL1 ", dirlist)
    os.chdir("../")
    #print("LOL2 ", dirlist)
    return (dirlist)


def show_temp(name, serverURL):
    print("3: ", os.getcwd())
    print("4: ", serverURL)
    if os.getcwd() == serverURL:
        os.chdir('database/' + name + '/temp')
    else:
        os.chdir('temp')
    print("U: ", os.getcwd())
    dirlist = os.listdir()
    print(os.listdir())
    os.chdir("../")
    return (dirlist)