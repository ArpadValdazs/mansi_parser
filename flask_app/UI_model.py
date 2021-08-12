import os

# Надо взять по одному их, и разбросать по разным концам массива

def show_info(name, serverURL):
    names = []
    print("1: ", os.getcwd())
    print("2: ", serverURL)
    if os.getcwd() == serverURL:
        os.chdir('database/' + name + '/texts')
    else:
        os.chdir('texts')

    names.append(os.listdir())
    print("1", names)
    os.chdir("../temp")
    names.append(os.listdir())
    os.chdir("../")
    print("2", names)
    return names
