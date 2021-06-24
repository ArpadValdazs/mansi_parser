from uniparser_erzya import ErzyaAnalyzer
import re
import os
import json
from orph_corrector import init_function

last_array = []
mode = ["nodiacritics"]
initial_string = []

# wordform.gloss = STEM+MORPH+MORPH...

preverbs = ["kon", "nāluw", "akwan", "nōx", "juw", "tāra", "sisi", "paɧ", "raviɣ", "pānttiɣ", "xot", "lap", "ēl", "ɕam", "ɕama", "lakkw", "lakkwa"]
prev_translations = ["наружу", "к.реке", "вместе", "наверх", "внутрь", "через", "назад", "к.суше", "в.клочья", "в.лепёшку", "от", "закрыть", "далеко", "насмерть", "насмерть", "врозь", "врозь"]

assertive = ["at", "ul", "wos", "woss", "ta", "ti", "xun'", "kos", "ke"]
ass_transl = ["NEG", "COND", "PROH", "OPT", "OPT", "PTCL", "PTCL2", "PTCL2", "разве", "CONC"]

sentence_array = [[], []]
def createParser(parse_mode):
    print(parse_mode)
    a = ErzyaAnalyzer(mode=parse_mode)
    return a

def call_adapter(filename, parse_mode):
    last_array.clear()
    if len(mode) > 0:
        mode.clear()
    mode.append(parse_mode)
    initial_string.clear()
    print("CALLED: \n\n1)", filename, " 2)", parse_mode)
    a = createParser(parse_mode)
    text = init_function(filename, "chern")
    # print("CORR: \n\n", text)
    response = text_splitter(text, a)
    # print("GOT: \n\n", response)
    print("KLLLLKLKLK", initial_string)
    finish = print_file(response)
    return finish

def start_analyze_2(word, a):
    # print("предложение", word)
    analyses = a.analyze_words(word)
    print(analyses)
    return analyze(analyses, a)

def analyze(analyses, a):
    morphs_array = []
    glosses_array = []
    for ana in analyses:
        prepared_glosses = []
        prepared_morphs = []
        for wordform in ana:
            print("WF\n\n\n ", wordform)
            gloss = wordform.gloss
            if '$' in gloss:
                # print("UAAA", gloss)
                elem = gloss.strip().split('$')
                result = elem[0]+"["+elem[1]+"]"
                if elem[2]:
                    i = 2
                    while i < len(elem):
                        result += elem[i]
                        i += 1
                gloss = result
            if '%' in wordform.lemma:
                redo = list(wordform.lemma.strip().split('%'))
                # print("redo ", redo)
                redo.remove(redo[0])
                second_analysis = start_analyze_2(redo, a)
                # print("SECOND: ", second_analysis)
                # print("BEFORE: ", morphs_array)
                for elem in second_analysis[0]:
                    glosses_array.append(elem)
                for elem in second_analysis[1]:
                    morphs_array.append(elem)
                # print("AFTER: ", morphs_array)
                # print("wordform IF: ", wordform)
            else:
                if "STEM" in gloss and wordform.wfGlossed:
                    gloss_stem = gloss.replace("STEM", wordform.otherData[0][1])
                # morphs_array.append(wordform.wfGlossed)
                    prepared_glosses.append(gloss_stem)
                    prepared_morphs.append(wordform.wfGlossed)
                if wordform.wfGlossed == '':
                    morphs_array.append([wordform.wf])
                    glosses_array.append([wordform.wf + "(??)"])

        if len(prepared_glosses) != 0:
            morphs_array.append(prepared_morphs)
            glosses_array.append(prepared_glosses)
        # здесь надо формировать строки с омонимией
    # print("RETURN: ", morphs_array, glosses_array)
    return [morphs_array, glosses_array]


def check_spaces(conc_string):
    new_string = []
    # print("CS: ", conc_string)
    # print(len(conc_string))
    for i in range(len(conc_string)):
        if conc_string[i-1] == "=" and i > 0:
            # print("conc: ", conc_string," ", conc_string[i-1], " i: ", i-1)
            new_string.append("")
        else:
            new_string.append(conc_string[i])
    sentence_to_print = "".join(new_string)
    # print("end: ", sentence_to_print)
    return sentence_to_print

def catch_preverbs(sentence):
    new_sentence = []
    splitted = list(sentence.strip().split(' '))
    for word in splitted:
        new_word = []
        replaced = ""
        # print("word", word)
        for i in range(len(word)):
            if word[i] == "=":
                new_sentence.append(" ")
            else:
                new_sentence.append(word[i])
        new_sentence.append(" ")
    sentence_to_print = "".join(new_sentence)
    return sentence_to_print


def print_file(array):
    print(array)
    dict2 = {combination: [{"gramm":
                                [{"compound"+str(compound):
                                      [{"omonym"+str(omonym):
                                            array[combination][0][compound][omonym]
                                        } for omonym in range(len(array[combination][0][compound]))]
                                  } for compound in range(len(array[combination][0]))],
                            "trans":
                                [{"compound" + str(compound):
                                      [{"omonym" + str(omonym):
                                            array[combination][1][compound][omonym]
                                        } for omonym in range(len(array[combination][1][compound]))]
                                  } for compound in range(len(array[combination][1]))],
                            }]
             for combination in range(len(array))}
    print(os.getcwd())
    #os.chdir("../../")
    print(os.getcwd())
    return(dict2)

def split_sentence(sentence_array, a):
    # print("String to split: ", sentence_array)
    for elem in sentence_array:
        # Emphasize string
        # print("This string: ", elem)
        new_sentence_array = catch_preverbs(elem)
        splitted = list(new_sentence_array.strip().split(' '))
        new_string = []
        # print(splitted)
        for i in range(len(splitted)):
            if "-" in splitted[i]:
                splitted[i] = splitted[i].strip().split('-')
                for j in splitted[i]:
                    new_string.append(j)
            else:
                new_string.append(splitted[i])
        # print("Splitted string: ", new_string)
        print(new_string)
        array = start_analyze_2(new_string, a)
        last_array.append(array)
    return last_array


def text_splitter(text, a):
    splitted = list(text.strip().split('.'))
    print(splitted)
    for i in splitted:
        initial_string.append(i)
    return split_sentence(splitted, a)

def sentence_adapter(word):
    parse_mode = mode[0]
    last_array.clear()
    a = createParser(parse_mode)
    print("word ", word)
    response = split_sentence([word], a)
    finish = print_file(response)
    print("response ", response)
    return finish

def saveFile(data):
    filename = data["filename"]
    print(os.getcwd())
    try:
        os.chdir('final_files')
    except FileNotFoundError:
        return "Ошибка! Путь:" + os.getcwd()
    # if os.getcwd() == "C:\\Users\\Пользователь":
        # os.chdir('MorphParser/flask_app')
    # if os.getcwd() == "C:\\":
        # os.chdir('C:/Users/Пользователь/MorphParser/flask_app')
    try:
        with open(filename+".csv", "w", encoding="utf-16") as fout:
            fout.write('№\tgramm\tgloss\tcomment\r\n')
            for i in range(len(data)-1):
                print(i)
                fout.write(str(i)+'\t')
                for row in data[str(i)]:
                    if "," in row[0]:
                        elem = row[0].replace(",", "")
                        print(elem)
                        fout.write(elem+'\t')
                    else:
                        print(row[0])
                        fout.write(row[0] + '\t')
                i += 1
                fout.write('\n')
        fout.close()
        print(os.getcwd())
        os.chdir("../")
        print(os.getcwd())
        return "ЁВТАТАНО ПОЗДОРОВТ!!!"
    except OSError:
        os.chdir("../")
        return "Люльсаӈ вāравес! Сусхати, тамле файл наме хансуӈкве ат рōви "

def find_file(data):
    # if os.getcwd() == "C:\\Users\\Пользователь":
    try:
        os.chdir('temps')
    except FileNotFoundError:
        return "Ошибка! Путь:" + os.getcwd()
    # if os.getcwd() == "C:\\":
        # os.chdir('C:/Users/Пользователь/MorphParser/flask_app')
    print("[", os.getcwd(), "] ", data["filename"])
    try:
        with open(data["filename"], "r", encoding="utf-8") as fout:

            print("[", os.getcwd(), "] ", data["filename"])
            text = fout.read()
            print(text)
            elem = text.split("<", 1)[0].partition("\n")[0].split(": ")
            mode = elem[1].split(" ")[0].lstrip()
            filename = elem[2].split("\\")[2]
            print("elem", filename, " ", mode)
            os.chdir("../")
            call_adapter(filename, mode)
            #line = fout.readline()
            #print(line.split(" "))
            return text
    except:
        os.chdir("../")
        return "Люльсаӈ вāравес! Ат рōвнэ лёӈх"

def save_temp(data):
    try:
        os.chdir('temps')
    except FileNotFoundError:
        return "Ошибка! Путь:" + os.getcwd()
    #if os.getcwd() == "C:\\Users\\Пользователь":
        #os.chdir('MorphParser/flask_app')
    #if os.getcwd() == "C:\\":
        #os.chdir('C:/Users/Пользователь/MorphParser/flask_app')
    print(os.getcwd(), data["filename"])
    try:
        with open(data["filename"], "w", encoding="utf-8") as fout:
            fout.write(data["text"])
            os.chdir("../")
            print(os.getcwd(), data["filename"])
            return "Ёмасыг вāравес!"
    except:
        os.chdir("../")
        return "Люльсаӈ вāравес! Ат рōвнэ лёӈх"

def hard_adapter(num):
    #допилить, когда человек начинает работать со старым файлом
    print("init ", initial_string)
    last_array.clear()
    print("initthis ", initial_string[int(num["number"])])
    parse_mode = mode[0]
    print("mode ", mode)
    a = createParser(parse_mode)
    result = split_sentence([initial_string[int(num["number"])]], a)
    response = print_file(result)
    print("response", response)
    return response



