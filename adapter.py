from uniparser_erzya import ErzyaAnalyzer
a = ErzyaAnalyzer(mode='strict')
import re


sentence = "puŋktəl xaniɕtaŋkwe."
def start_analyze(word):
        print(word)
        analyses = a.analyze_words(word)
        glosses_array = []
        morphs_array = []
        total_array = []
        #print(word)
        for ana in analyses:
                for wordform in ana:
                        array = []
                        print(wordform)
                        gloss = wordform.gloss
                        if "STEM" in gloss:
                                gloss_stem = gloss.replace("STEM", wordform.otherData[0][1])
                        glosses_array.append(wordform.wfGlossed)
                        morphs_array.append(gloss_stem)
        conc_glosses=" ".join(glosses_array)
        conc_morphs=" ".join(morphs_array)
        total_array.append([conc_glosses])
        total_array.append([conc_morphs])
        print(total_array)
        #array_to_print=" ".join(total_array)
        #print(array_to_print)
        print_dict(total_array)

def print_dict(array):
        filename_out = "glosses.csv"
        with open(filename_out, 'w', encoding='utf-16', newline='') as fout:
                fout.write('morphemes\tglosses\r\n')
                print(array[0][0])
                fout.write(array[0][0] + '\t' + array[1][0] + '\r\n')
                # morphemes_sorted = list(array.keys())
                # glosses_sorted = list(array.values())
                #for i in range(len(morphemes_sorted)):
                        #for glosse in glosses_sorted[i]:
                                #fout.write(morphemes_sorted[i] + '\t' + glosse + '\r\n')

def split_sentence(sentence):
        splitted = list(sentence.strip().split(' '))
        
        start_analyze(splitted)

split_sentence(sentence)
        
