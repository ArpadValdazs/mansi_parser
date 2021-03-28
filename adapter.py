from uniparser_erzya import ErzyaAnalyzer

a = ErzyaAnalyzer(mode='strict')
import re

text = "puŋktəl xaniɕtaŋkwe xaniɕtaptəɣlaŋkwe qqq āt. l'oŋхnəl joxtsum kon-wārijanīn. utkweɣ kwaləs totimanəl wārijaɣum"
last_array = []


def start_analyze(word):
    analyses = a.analyze_words(word)
    glosses_array = []
    morphs_array = []
    sentence_array = []
    for ana in analyses:
        print(ana)
        for wordform in ana:
            array = []
            prev_value = ""
            gloss = wordform.gloss
            # ВЫДЕЛИТЬ В ОТДЕЛЬНУЮ ФУНКЦИЮ
            if wordform.wf == "kon":
                wordform.wfGlossed = wordform.wf.replace("kon", "kon=")
                prev_value = "наружу="
            if "STEM" in gloss and wordform.wfGlossed:
                if prev_value:
                    gloss_stem = gloss.replace("STEM", prev_value)
                    morphs_array.append(gloss_stem)
                elif wordform == ana[0] and wordform.wfGlossed and prev_value == "":
                    gloss_stem = gloss.replace("STEM", wordform.otherData[0][1])
                    morphs_array.append(gloss_stem)
                else:
                    gloss_stem = gloss.replace("STEM", "/" + wordform.otherData[0][1] + "/")
                    morphs_array.append(gloss_stem)
            elif wordform.wfGlossed:
                morphs_array.append(wordform.gloss)
            if wordform == ana[0] and wordform.wfGlossed:
                glosses_array.append(wordform.wfGlossed)
            if wordform.wfGlossed == '':
                glosses_array.append(wordform.wf)
                morphs_array.append(wordform.wf+"??")
    conc_glosses = " ".join(glosses_array)
    conc_morphs = " ".join(morphs_array)
    print(conc_glosses)
    prepared_glosses = check_spaces(conc_glosses)
    prepared_morphs = check_spaces(conc_morphs)
    sentence_array.append([prepared_glosses])
    sentence_array.append([prepared_morphs])
    # array_to_print=" ".join(sentence_array)
    # print(array_to_print)
    last_array.append(sentence_array)


def check_spaces(conc_string):
    new_string = []
    print(len(conc_string))
    for i in range(len(conc_string)):
        if conc_string[i-1] == "=":
            new_string.append("")
        else:
            new_string.append(conc_string[i])
    sentence_to_print = "".join(new_string)
    print(sentence_to_print)
    return sentence_to_print


def catch_preverbs(sentence):
    new_sentence = ''
    if "kon-" in sentence:
        new_sentence = sentence.replace("kon-", "kon ")
        print(new_sentence)
        return new_sentence
    else:
        return sentence


def print_dict(array):
    filename_out = "glosses.csv"
    with open(filename_out, 'w', encoding='utf-16', newline='') as fout:
        fout.write('morphemes\tglosses\r\n')
        for elem in range(len(array)):
                fout.write(array[elem][0][0] + '\t' + array[elem][1][0] + '\r\n')


def split_sentence(sentence_array):
    for elem in sentence_array:
        new_sentence_array = catch_preverbs(elem)
        splitted = list(new_sentence_array.strip().split(' '))
        start_analyze(splitted)
    print_dict(last_array)


def text_splitter(text):
    splitted = list(text.strip().split('.'))
    split_sentence(splitted)


text_splitter(text)
