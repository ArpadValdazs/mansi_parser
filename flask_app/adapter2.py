from uniparser_erzya import ErzyaAnalyzer
import re
import os
import json
from orph_corrector import init_function

last_array = []

# wordform.gloss = STEM+MORPH+MORPH...

preverbs = ["kon", "nāluw", "akwan", "nōx", "juw", "tāra", "sisi", "paɧ", "raviɣ", "pānttiɣ", "xot", "lap", "ēl", "ɕam", "ɕama", "lakkw", "lakkwa"]
prev_translations = ["наружу", "к.реке", "вместе", "наверх", "внутрь", "через", "назад", "к.суше", "в.клочья", "в.лепёшку", "от", "закрыть", "далеко", "насмерть", "насмерть", "врозь", "врозь"]

assertive = ["at", "ul", "wos", "woss", "ta", "ti", "xun'", "kos", "ke"]
ass_transl = ["NEG", "COND", "PROH", "OPT", "OPT", "PTCL", "PTCL2", "PTCL2", "разве", "CONC"]

sentence_array = [[], []]
def createParser(parse_mode):
    a = ErzyaAnalyzer(mode=parse_mode)
    return a

def call_adapter(filename, parse_mode):
    last_array.clear()
    print("CALLED: \n\n", filename, " ", parse_mode)
    a = createParser(parse_mode)
    text = init_function(filename, "chern")
    print("CORR: \n\n", text)
    response = text_splitter(text, a)
    print("GOT: \n\n", response)
    finish = print_file(response)
    return finish

def start_analyze_2(word, a):
    # print("предложение", word)
    analyses = a.analyze_words(word)
    return analyze(analyses, a)

def analyze(analyses, a):
    morphs_array = []
    glosses_array = []

    for ana in analyses:
        prepared_glosses = []
        prepared_morphs = []
        for wordform in ana:
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
    os.chdir("../../")
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
        array = start_analyze_2(new_string, a)
        last_array.append(array)
    return last_array


def text_splitter(text, a):
    splitted = list(text.strip().split('.'))
    return split_sentence(splitted, a)

def sentence_adapter(word):
    response = text_splitter(word, a)
    return response
