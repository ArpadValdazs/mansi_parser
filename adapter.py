from uniparser_erzya import ErzyaAnalyzer

a = ErzyaAnalyzer(mode='strict')
import re

text = "puŋktəl āɣmxarəŋ akwtoriɣ āŋkwal. akwtorəɣ kon-wārijanīn. utkweɣ utnən kwaləs āpərlaŋkwe. akwmatērtən akwmatnakt аlśəŋ wārijaɣum"
last_array = []
#надо добавить аквтопы, а также разобраться с элементами агглютинации в мансийском

def start_analyze(word):
    print("предложение", word)
    analyses = a.analyze_words(word)
    glosses_array = []
    morphs_array = []
    sentence_array = []
    no_dot_gramm_str = ""
    glosses_str = ""
    for ana in analyses:
        for wordform in ana:
            if '%' in wordform.lemma:
                new_wordform = catch_much_stems(wordform)
                splitted_gramm = wordform.wfGlossed.split("-")
                splitted_glosses = wordform.gloss.split("-")
                no_dot_gramm = [new_wordform[0][0:-1:1]]
                glosses = [new_wordform[1]]
                i = 1
                while i < len(splitted_gramm):
                    no_dot_gramm.append(splitted_gramm[i])
                    i = i + 1
                i = 1
                while i < len(splitted_glosses):
                    glosses.append(splitted_glosses[i])
                    i = i + 1
                no_dot_gramm_str = "-".join(no_dot_gramm)
                glosses_str = "-".join(glosses)
                wordform.wfGlossed = new_wordform[0]
                wordform.wfGlossed.split("-")
                #morphs_array.append(no_dot_gramm_str)
                if wordform == ana[0]:
                    morphs_array.append(glosses_str)
                    glosses_array.append(no_dot_gramm_str)
                else:
                    morphs_array.append("/" + glosses_str + "/")
            array = []
            prev_value = ""
            gloss = wordform.gloss
            # ВЫДЕЛИТЬ В ОТДЕЛЬНУЮ ФУНКЦИЮ
            if wordform.wf == "kon":
                wordform.wfGlossed = wordform.wf.replace("kon", "kon=")
                prev_value = "наружу="
            if wordform.wf == "akwan":
                wordform.wfGlossed = wordform.wf.replace("akwan", "akwan=")
                prev_value = "вместе="
            if wordform.wf == "nox":
                wordform.wfGlossed = wordform.wf.replace("nox", "nox=")
                prev_value = "наверх="
            if wordform.wf == "juw":
                wordform.wfGlossed = wordform.wf.replace("juw", "juw=")
                prev_value = "внутрь="
            if wordform.wf == "tāra":
                wordform.wfGlossed = wordform.wf.replace("tāra", "tāra=")
                prev_value = "через="
            if wordform.wf == "sisi":
                wordform.wfGlossed = wordform.wf.replace("sisi", "sisi=")
                prev_value = "назад="
            if wordform.wf == "paɧ":
                wordform.wfGlossed = wordform.wf.replace("paɧ", "paɧ=")
                prev_value = "к.суше="
            if wordform.wf == "raviɣ":
                wordform.wfGlossed = wordform.wf.replace("raviɣ", "raviɣ=")
                prev_value = "в.клочья="
            if wordform.wf == "pānttiɣ":
                wordform.wfGlossed = wordform.wf.replace("pānttiɣ", "pānttiɣ=")
                prev_value = "в.лепёшку"
            if wordform.wf == "xot":
                wordform.wfGlossed = wordform.wf.replace("xot", "xot=")
                prev_value = "от"
            if wordform.wf == "lap":
                wordform.wfGlossed = wordform.wf.replace("lap", "lap=")
                prev_value = "закрыть"
            if wordform.wf == "ēl":
                wordform.wfGlossed = wordform.wf.replace("ēl", "ēl=")
                prev_value = "далеко"
            if wordform.wf == "ɕam":
                wordform.wfGlossed = wordform.wf.replace("ɕam", "ɕam=")
                prev_value = "насмерть"
            if wordform.wf == "lakkw":
                wordform.wfGlossed = wordform.wf.replace("lakkw", "lakkw=")
                prev_value = "врозь"
            if wordform.wf == "lakkwa":
                wordform.wfGlossed = wordform.wf.replace("lakkwa", "lakkwa=")
                prev_value = "врозь"
            if '%' not in wordform.lemma:
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
    #print(conc_glosses)
    prepared_glosses = check_spaces(conc_glosses)
    prepared_morphs = check_spaces(conc_morphs)
    sentence_array.append([prepared_glosses])
    sentence_array.append([prepared_morphs])
    # array_to_print=" ".join(sentence_array)
    # print(array_to_print)
    last_array.append(sentence_array)


def check_spaces(conc_string):
    new_string = []
    #print(len(conc_string))
    for i in range(len(conc_string)):
        if conc_string[i-1] == "=":
            new_string.append("")
        else:
            new_string.append(conc_string[i])
    sentence_to_print = "".join(new_string)
    #print(sentence_to_print)
    return sentence_to_print

def catch_much_stems(word):
    analysed_gramm = []
    analysed_gloss = []
    redo = list(word.lemma.strip().split('%'))
    redo.remove(redo[0])
    second_analyses = a.analyze_words(redo)
    print("ASAS: ", second_analyses)
    for i in range(len(second_analyses)):
        for wordform in second_analyses[i]:
            analysed_gramm.append(wordform.wf)
            if 'STEM' in wordform.gloss:
                analysed_gloss.append(wordform.otherData[0][1])
                print(analysed_gloss)
            print(wordform.gloss)
            cases = list(wordform.gloss.strip().split('-'))
            i = 1
            while i < len(cases):
                analysed_gloss.append(cases[i])
                i = i + 1
    split_gramm = "-".join(analysed_gramm)
    split_gloss = "-".join(analysed_gloss)
    print(split_gramm)
    print(split_gloss)
    return [split_gramm, split_gloss]




def catch_preverbs(sentence):
    new_sentence = []
    splitted = list(sentence.strip().split(' '))
    for i in splitted:
        #print(i)
        if "kon-" in i:
            word = i.replace("kon-", "kon ")
            new_sentence.append(word)
        elif "xot-" in i:
            word = i.replace("xot-", "xot ")
            new_sentence.append(word)
        elif "ēl-" in i:
            word = i.replace("ēl-", "ēl ")
            new_sentence.append(word)
        elif "nox" in i:
            word = i.replace("nox-", "nox ")
            new_sentence.append(word)
        elif "juw" in i:
            word = i.replace("juw-", "juw ")
            new_sentence.append(word)
        elif "tāra" in i:
            word = i.replace("tāra-", "tāra ")
            new_sentence.append(word)
        elif "sisi" in i:
            word = i.replace("sisi-", "sisi ")
            new_sentence.append(word)
        elif "akwan" in i:
            word = i.replace("akwan-", "akwan ")
            new_sentence.append(word)
        elif "lap" in i:
            word = i.replace("lap-", "lap ")
            new_sentence.append(word)
        elif "raviɣ" in i:
            word = i.replace("raviɣ-", "raviɣ ")
            new_sentence.append(word)
        elif "pānttiɣ" in i:
            word = i.replace("pānttiɣ-", "pānttiɣ ")
            new_sentence.append(word)
        elif "paɧ" in i:
            word = i.replace("paɧ-", "paɧ ")
            new_sentence.append(word)
        elif "naluw" in i:
            word = i.replace("naluw-", "naluw ")
            new_sentence.append(word)
        elif "ɕam" in i:
            word = i.replace("ɕam-", "ɕam ")
            new_sentence.append(word)
        elif "lakkw" in i:
            word = i.replace("lakkw-", "lakkw ")
            new_sentence.append(word)
        elif "lakkwa" in i:
            word = i.replace("lakkwa-", "lakkwa ")
            new_sentence.append(word)
        else:
            new_sentence.append(i)
    sentence_to_print = " ".join(new_sentence)
    #print("finish", sentence_to_print)
    return sentence_to_print


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
