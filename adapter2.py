from uniparser_erzya import ErzyaAnalyzer

a = ErzyaAnalyzer(mode='nodiacritics')
import re
from orph_corrector import init_function

# text = "puŋktəl, kon-kwaluw āɣmxarəŋ akwtoriɣ, a? d? aa? d? dddd fff, aa, āŋkwal. akwmatnakt, аlśəŋ, wārijaɣum, wojən konal' "
# text = "mān'pol' ētpost l'āxxal totne māxum xantə-mansijskij gosudarstwennəj arxiw-koln wōwin'tālwēsət. tot rūpitan xōtpat tānanəln jil'pi tāratəm nēpakət urəl potərtasət os diskət sussəltasət. pēs porat samarowat potr jefimowič kuzn'eсow ōlum. XIX not oiɣpam tālətət os XX not palətəl kuzn'eсowət ɕēma ōləɣlam tēlat an' pussən tāra-pattuwēsət. tān pēs xurianəl os dokumentanəl arxiwət ōwəl ɕos sussəltawēsət. an' rūtanəl t'umen' os jaroslawl' ūsət ōlēɣət. tuwəl kit jil'pi nēpakəɣ tāratawesīɣ. akw nēpak o.w. buksina os mōtan o.n. gawrilowa xassīɣ, tēn nēpakaɣēn arxiwt rūpitan xōtpatn tārataŋkwe n'ōtwesīɣ. ol'ɣa wladimirowna buksina (maslowa) takwi moskwat ōlə os «nowost'i juɣrə» gazetan l'āxxalət xansə. taw «moj žizn'ennəj zakat prekrasen» nampa nēpakēt iwan mixajlowič gubkin akademik urəl potərtas. ōjka 45 tāle porat warwara bojarskaja, mān'lat nē, jot xōntxatas. tōnt nē wāt nupəl akw tāle tōwləs. tēn akwan at minasīɣ kos, os tōwnakt akwjot rūpitəm jalasasīɣ. iwan mixajlowič mā-wōj kisne māt rūpitas, warwara kartat pōsət pōsləs. tuwəl ōjka səmən ērne āɣitēntəl tēnki xalēnt piɕmat xasmīɣ. 1939 tālt gubkin āt'iməɣ jēmtəs, os jotəl sār ēkwatēn piɕmane rossijskij an arxiw-koln totəmat. tānanəl tot wal'ent'ina wasil'ewna patranowa, «nowost'i juɣrə» gazetat rūpitan ēkwa, kāsalāsane os ol'ɣa buksinan nēpak ɕōpitaŋkwe lāwəs. an' os taml'e pūməɕ jil'pi nēpak wārwes. mōt «detstwo, opal'onnoje wojnoj» nampa nēpakt ol'ɣa gawrilowa uraj ūst ōlum matumpāla xōtpat potranəl xassane. ta ūst školat xan'iɕtaxtən n'āwramət «rostok» nampa objedin'en'iat ōs potrət xansəm jalasēɣət. an' janəɣpāla xōtpat ōlum tārwitəŋ tēlanəl urəl xansəm potranəl pussən akw nēpakən ɕōpitawēsət. xantə-mansijsk ūsuw urəl «ɣorod solnсa» nampa disk wārima. «arxiwə juɣorii» №12 jil'pi žurnal os «juɣorskij kal'ejdoskop sobət'ij na 2013» kal'endar sussəltawesīɣ. tə nēpakət manos diskət pussən 2012 tāln xansəɣləm projektət ɕirəl wārwēsət. an' tə tāl tə arxiwkol «istoria isčeznuwšix derewen'» nampa mōt projekt ɕirəl rūpitaŋkwe patə. naləman tāl juwl'e xul'tum porat 292 mān' pāwəl okruɣ janətəl kartan xansəm ōlsət. an' 194 mān' pāwlətt māxum ōluŋkwe tup xul'tmət. mōt pāwəlkwet xotal' sōjməsət, xuml'e jēmtsət? xun' tān ōlwēsət, manər nam ōɕsət? xot'ut tot ōwəl kol ūnttəɣlas os xotə xōtpat tuw ōlməɣtālsət? pussən tə tēlat tāra-pattən māɣəs okruɣt ōlne māxum kitəɣlawet. xot'ut n'ōtuŋkwe kāsaɕi ke, akwjot rūpitaŋkwe wōwawet. taimāɣəs māxum tānki samən patum mān' pāwlanəl urəl potərtaŋkwe wērmēɣət. pēs xurit, matər dokumentət ōn'ɕēɣət ke, arxiwən ōs wos totnuwanəl. 2014 tālt arxiwt rūpitan xōtpat «pamat'i isčeznuwšix sol i derewen' xantəmansijskoɣo rajona» nēpak ɕōpitaŋkwe lāwxatsət. mān os mānki mān'ɕi māxmanuw ōlum pāwlət nēpakn ɕōpitanuwanūw ke, takem jomas ōlnūw. sāwəŋpāle tup aɕōjkanuw samən patum pēs nēpakanəlt xansəm xul'tsət .ōwlēt xum xōtpanuw repressia tālətət xottal' totəɣpawēsət. tuwəl mōtanət xōntlan māt porslawēsət. pāwlanuwt mān'ɕi ɕēmat moɕɕamasət. jotəl kolxozət kwāltapaptuwēsət. mān' pāwlət akw janəɣ pāwlən totwēsət. taɕirəl mān'ɕi pāwlanuw sujtāləɣ ta patsət. tōwnakt namanəl ērɣətt xūntləɣlāləjanūw os pēs jis mōjtətt lowin'taləjanuw: mēsəɣ pāwəl, kūrt'a pāwəl, muwənkēs,rākt'a pāwəl, sūma pāwəl, xoxaŋa pāwəl.... os pēs potər ōn'ɕeɣīn ke, nān gah­m a o @ y a n d e x . r u el'ektronnəj počtan lātəŋ xansēn. tə tēlat māɣəs swetlana wladimirowna t'ul'ina puŋktotə. mōlal ta arxiwət akwan-atəm pēs dokumentət, xurit pussən iɕxīpəŋ utən pōsluwēsət. os «el'ektronnəj arxiw juɣrə» nampa sajtən wārwēsət. nān an' matər ērne pēs nēpakət tot sunsəɣlaŋkwe wērmianīn. tə lātŋət ɕirəl kisxatēn: arhivugra. admhmao.ru manos gah­mao.ru māxum an' potranəl manos xurianəl piɕmal kētəjanən ke, adrese taml'e: 628011, xantə-mansijsk ūs, enɣel'sa ūsxulə, 14 kole. manos 8(3467) 32-97-76, 33-14-67 t'el'efonəɣ xosət zwon'itēn."
# text = "mān'pol' ētpost l'āxxal totne māxum xantə-mansijskij gosudarstwennəj arxiw-koln wōwin'tālwēsət"
# text = "minēɣum minēɣən mini minimēn mineɣīn minēɣ minēw minēɣit minēɣət"
# text = "wārilum wārilən wārite wārijaɣe wārijaɣmen wārijaɣīn wārijaɣēn wārijaɣuw wārijaɣānil wārijaɣānəl"
# text = "wārijaɣum wārijaɣīn wārijaɣe wārijaɣuw wārijanuw wārijānəl wārijanānəl wārijaɣānəl wārijanēn wārijananēn wārijane"
# text = "wāwem wāɣum wāŋkwe totwem totwesum"
# text = "wārislum wārislən wāriste wārsaɣe wārsaɣuw wārsaɣīn wārsanum wārsanīn wārsaɣmēn wārsāne wārsanānəl wārisaɣamēn"
# text = "wārnūwem wārnūwēmēn wārnūwēw wārnūwūw wārnūwtēn"
# text = "wōwin'tālwēsət sussəltawēsət wōwin'tāluŋkwe"
# text = "kon=ke=mini kon=kwāləs supiɣ=kwāləs. wārnūwēmēn=ke joxti, am wārilum ēləpal ēləpalt konipal"

text = init_function()
#text = "joxti akwtoriɣ kwāləs. totwesum aaas"
# text = "kosja sunt erɣ otər. kosja sunt otər oli. pakw posi wojkan otər akw tujɣ ekwate san wars. ekwate san wars, loŋxa worati. ekwate lawi tur tep, its tep ponne san ojkate at taŋxi. ojkatan san almajawes, puliɣ ratwes. am taj tur tep astep jorəl at janɣ masum. wor sorup n̩owəl tajim, luwum janɣmas n̩owəlum janɣmas. ojkate laws. kitit tujaɣ jemtəs. ekwate xotal̩ olne san, xansaŋ san akwaɣ ta wari. ojkate nupəl lawi: - naŋen tur tep asten pinuŋkwe, manər jomas sankwe. ojkaten almajawe, os puliɣ ratwes. ojkate laws - am tur tep as tep tajum luwum at janɣmas, n̩owəlum at janə̄ɣmas. uj n̩owəl tajim luwum janɣmas, n̩owəlum janɣmas. xurmit tujɣ ti joxtəs, jaŋk notne poraɣ ti jemtəs os. ekwate xansaŋ san os ta wari. Ja wars os sant. ojkate nupəl lawi naŋəx nake tur tep, as tep pinne manər saŋkwe! ojkate wasɣ nemat xotum wasɣ at suitɣlas. ekwate nupəl lawi naŋ kasən minimen ke minumen, ti astlaxtasit. ajaŋ xum pɣane saran xap waruŋkwe larsane wap warsət. taltxatuŋkwe patsət. taltateɣt, nē paɣ mini. n̩al̩ akw xum xontaste. tamle xum xontxatas samaɣe nit at laplɣ ta xurip xum aman etpos, aman xotal! tan ojkate apsite. tan ekwa oŋɣa nupəl lawi: - ta xapet ojkan xottal p.p.w.o xottal̩ minne man totilen. minne mān ojkan ke alawe, wasɣ ti man at sunsiln. an̩ ta minasət. ete xotal etəl ta mineɣt. ɕaraɕ kotli akw mat mina xosa minasit man wat̩a minasit ekwate ojkate nupəl lawi: xuwer (xujew) xujunkwe patsit, ojkate lawi, na maxmane nupəl lawi: nan xujen, am urejum. ekwate lawi: naŋ xujen, naŋ ropitase ə n; waɣtal patsen, am nas unlasum! ojkate lawi: - naŋ erəŋ jola ojilmatawen erəŋ xonten joxtawew. ekwate lawi: - naŋ xujen, xontmake jiŋkwe patawe nox sajkatijanum. xujuŋkwe patsət, ojkate ker supe xot ekwate lawi: ker supe xot aŋx w eln, ete-xotal ker ulaman jomas oɕsann, an̩ aŋxweln! ojkate ker ulamane aŋɣsane, ta xujas. tan xujasət, maxmane tan xujnel sis ekwaten ker kus sunte lap ta juntuws nox  ul wos masxati. Jowte kasajil supɣ. ɕorxəltawes, nox xartuŋkwe jowt nirasanete mus nox-xartnete mus sopəŋ wos tolmati. maxmane xujnanel sis ekwa ruɕ oter. usen ta minas. ruɕ oter us lunnuw ols. Juw joxtas ro usen, lawi - man joxtesuw, jajen xontɣ! takwi maxmane palt sarten minas. tan juji palet. ro xont xap juw. tan maxmane palt joxtəs maxmane xujeɣt. ro. xap tan paltlaneln jis paɣ-poxats. ekwate ojkate nupəl lawi noŋx kwalen, xontn joxtuwesuw ti alawew. ojkate nox kwalapas, roxtəp  taxtas. nox-kwalapas, ker kuse nox kos masapite, tuw at lapi, kente ekwaten lap juntime. xot ta liste. Jowte almajaste, xassumtaste. xassumtame mus, ɕorxəltim matenəl ta supəŋ ta tolmats. Jowte sakwalas, tuwl r otern pusen ta alwest. ekwa tup xul̩tas os apat xujne pəriɕ xultəs. ekwate r.o. nupəl lawi - pəriɕ os oleln, janɣmi, tan aɕe l̩oŋx jujil kinsite. ro lawi tau man̩, aɕe l̩oŋx at kínsīte, aɕe on̩ɕes man ati at waɣte. ta minasit. ppwo puŋk sowl r.otern xot nujwes, naŋk ta l̩axna ta nox- taɣatawes. Jajt ta ta l̩axəl jalum ppwo puŋ sawe naŋk tal̩axət wot untawe sira sowe wos wotawe, aŋxa sowe wos wotawe! ne ro palt olmɣtas. xumɣ ta wariste. an̩ ta oleɣ. pɣriɕ xoɕa man wat̩i ols janɣmas. ro pɣetəl, n̩awrametəl joŋxeɣt. tau katl jor, laɣəle jor, ro pɣət lawi wat waɣtaləɕ mini, tau lɣ itəŋəɕ mini. r.o. n̩awramət pəriɕ nupəl laweɣt - naŋ jor laɣələn ti āɕmen, jor kat t̩i aɕmen, aɕen puŋk sowe as kotle tumpet naŋk tal̩axt manrɣ xoni? jor ti olmen. ɕane palt joxtəs ɕane nupəl lawi: - toxa ti laweɣt - Jor ti osen, os aɕen olim porat joren xotal̩ totiɣlasen? Ꞩane lawi: - aɕen ti, r.o. ta nomsi aɕe sol̩ ti mot xotal jemti akw ti piɕ, tan jor. Joŋxuŋkwe pateɣt tau lɣ, itəŋəɕ mini, motant lɣt waɣtalaɕ mini. ro n̩awramət laweɣt. - aɕen olim porat jor ti olmən, joren xotal̩ totiɣlasen! Ꞩane palt os ti minas. Ꞩane palt joxtəs lawi - Jor ti olmen, aɕen olim porat joren xotal̩ totiɣlasen? Ꞩane lawi aɕen ti. xurmit peraman̩ ti jemtəs. ta jonɣeɣt. tau lɣaəŋəɕ mini motantlɣt, waɣtaləɕ mini. n̩awramət lawɣt- naŋ jor ti olmen, aɕen olim porat, joren xotal̩ ti totiɣlaslən? us joli palt ekwaɣ-ojkaɣ oleɣ. pəriɕ nomsi ekwaɣ ojkaɣ palt tuw jalejum. nawramət laweɣt, ertum aɕ oɕsum - aɕum alime, ɕanum lawi: aɕum oli!. p. ekwaɣ ojkaɣ kitɣlaŋkwe minas. e.o palt joxtəs kitɣli: sol̩ aman aɕ oɕsum? e.-o. laweɣ, - sol̩ aɕ oɕsən. aɕen ti r.oterna olwes. p. ten nupəlen lawi - anumen xap majeln, am juwle mineɣum, aman rot oɕsum, man ati, am at waɣlum. e.-o. laweɣ rotan jun oleɣt. man̩ nupəl majwes, ta minas. minimete elal̩ sunsi, tajtnəl tajt xosit xap juw. xap l̩apan joxtuŋkwe pats, paɣ poxtas, worn tujtxatas. xap tau torɣəl joxtəs, akw xum suiti: - paɣ poxtew, tit elmxolas paɣ miname naŋki. kinsi luw. tan poɣ-poxtasət. ta kinsuŋkwe patsanel. kissanel, xontsanel. ppwo. ta apɕite. jaɣpɣe kinsiŋkwe ti joxtəs p. jaɣpɣen, kitɣlawe: - aɕen xotal̩ totwes? p. lawi: - aɕum ruɕ oterna olime. ta ro usen minasit. ro usen joxtesət. paɣ poxtasit paɣ minuŋkwe patsət p.p.w.o.u., jowt n̩al̩ wəŋkwe kuɕi. mire nupəl lawi - maj manər mirəl warew, ti kem use, amkem paɣ  mineɣum. am jowtəl n̩oləl manər wareɣum, ti kem us. n̩an̩ tup unten mant sup waɣlum, (n̩an̩ untne mant sup) tup wiste, paɣ-ta minas paɣ minas, us akw pale tupəl witen ta rautaste (mant supetəl) uset olne mir ɕar pusen olaste witen naluw rautasaste. r.o. (mant tupəl supetəl) jūnətaste, samaɣe noren xanujasɣ, akw tox sunseɣ. ta xum-akw kot pale, akw laɣəl pale tarwitəŋ. ekwaɣ-ojkaɣ, ten tuwpoxtamɣ - mena men ul aleln! tau lawi: - am nenan at alijaɣum. Juwle minuŋkwe ti patsət. on̩ɣa liliŋ taɣəl xapen totaste. xapen totaste, liliŋ taɣəl kataɣe xap pattan ker sol̩il jol ratsaɣe. laɣəlaɣe xap pattan ker sol̩il as jol ratsaɣe. ta minmɣtasət. ta minmɣtasit ekwa xap pattat ta xuji. ta pukite xosit ta jomeɣt Jomimenəl sorumen ta patwes. tuwl witen ta lisanel. tan olne māneln ta jóxtāsət. an̩ ta oleɣt"

# надо точки срезать, если они появляются
print("text ", text, " finish")
last_array = []
# надо добавить аквтопы, а также разобраться с элементами агглютинации в мансийском
# супыг также имеет значение "осётр"
# проверить -ыг. и -й. ! проверить йинкве

# остановился на сякаралунгкве

# wordform.gloss = STEM+MORPH+MORPH...
# 1. Убрать знаки равно

preverbs = ["kon", "nāluw", "akwan", "nōx", "juw", "tāra", "sisi", "paɧ", "raviɣ", "pānttiɣ", "xot", "lap", "ēl", "ɕam", "ɕama", "lakkw", "lakkwa"]
prev_translations = ["наружу", "к.реке", "вместе", "наверх", "внутрь", "через", "назад", "к.суше", "в.клочья", "в.лепёшку", "от", "закрыть", "далеко", "насмерть", "насмерть", "врозь", "врозь"]

#надо их присобачить к коду
assertive = ["at", "ul", "wos", "woss", "ta", "ti", "xun'", "kos", "ke"]
ass_transl = ["NEG", "COND", "PROH", "OPT", "OPT", "PTCL", "PTCL2", "PTCL2", "разве", "CONC"]

sentence_array = [[], []]

def start_analyze_2(word):
    print("предложение", word)
    analyses = a.analyze_words(word)
    return analyze(analyses)

def analyze(analyses):
    morphs_array = []
    glosses_array = []

    for ana in analyses:
        prepared_glosses = []
        prepared_morphs = []
        for wordform in ana:
            gloss = wordform.gloss
            if '$' in gloss:
                print("UAAA", gloss)
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
                print("redo ", redo)
                redo.remove(redo[0])
                second_analysis = start_analyze_2(redo)
                print("SECOND: ", second_analysis)
                glosses_array.append(second_analysis[1])
                morphs_array.append(second_analysis[0])
                print("wordform IF: ", wordform)
            else:
                if "STEM" in gloss and wordform.wfGlossed:
                    gloss_stem = gloss.replace("STEM", wordform.otherData[0][1])
                # morphs_array.append(wordform.wfGlossed)
                    prepared_glosses.append(gloss_stem)
                    prepared_morphs.append(wordform.wfGlossed)
                if wordform.wfGlossed == '':
                    morphs_array.append(wordform.wf)
                    glosses_array.append(wordform.wf + "(??)")

        if len(prepared_glosses) != 0:
            morphs_array.append(prepared_morphs)
            glosses_array.append(prepared_glosses)
        # здесь надо формировать строки с омонимией
    print("RETURN: ", morphs_array, glosses_array)
    return [morphs_array, glosses_array]


# def start_analyze(word):
#     print("предложение", word)
#     analyses = a.analyze_words(word)
#     morphs_array = []
#     glosses_array = []
#     sentence_array = []
#     word_check = []
#     print(analyses)
#     for ana in analyses:
#         for wordform in ana:
#             word_check = wordform
#             # For words of many stems
#             if '%' in wordform.lemma:
#                 if '%' in wordform.lemma:
#                     second_analysis = start_analyze(wordform)
#                     print("SECOND: ", second_analysis)
#                 new_wordform = catch_much_stems(wordform)
#                 # Split on parts
#                 splitted_gramm = wordform.wfGlossed.split("-")
#                 splitted_glosses = wordform.gloss.split("-")
#                 # String preparation
#                 no_dot_gramm = [new_wordform[0]]
#                 glosses = [new_wordform[1]]
#                 i = 1
#                 while i < len(splitted_gramm):
#                     no_dot_gramm.append(splitted_gramm[i])
#                     i = i + 1
#                 i = 1
#                 while i < len(splitted_glosses):
#                     glosses.append(splitted_glosses[i])
#                     i = i + 1
#                 no_dot_gramm_str = "-".join(no_dot_gramm)
#                 glosses_str = "-".join(glosses)
#                 wordform.wfGlossed = new_wordform[0]
#                 wordform.wfGlossed.split("-")
#                 if wordform == ana[0]:
#                     glosses_array.append(glosses_str)
#                     morphs_array.append(no_dot_gramm_str)
#                 else:
#                     glosses_array.append("/" + glosses_str + "/")
#             if '$' in wordform.gloss:
#                 print("UAAA", wordform.gloss)
#                 elem = wordform.gloss.strip().split('$')
#                 result = elem[0]+"["+elem[1]+"]"
#                 if elem[2]:
#                     i = 2
#                     while i < len(elem):
#                         result += elem[i]
#                         i += 1
#                 wordform.gloss = result
#             array = []
#             prev_value = ""
#             gloss = wordform.gloss
#             # ВЫДЕЛИТЬ В ОТДЕЛЬНУЮ ФУНКЦИЮ
#             for i in range(len(preverbs)):
#                 if wordform.wf == preverbs[i]:
#                     wordform.wfGlossed = wordform.wf.replace(preverbs[i], preverbs[i])
#                     prev_value = prev_translations[i]
#             if '%' not in wordform.lemma:  # если нет процента в лемме
#                 if "STEM" in gloss and wordform.wfGlossed:
#                     for i in range(len(analyses)):
#                         if analyses[i] == ana:
#                             print("GAY!", ana)
#                     if prev_value:  # если преверб записался
#                         gloss_stem = gloss.replace("STEM", prev_value)    # меняем STEM на значение преверба
#                         glosses_array.append(gloss_stem)  # и добавляем в массив глоссу
#                     elif wordform == ana[0] and wordform.wfGlossed and prev_value == "":  # если преверб записался
#                         gloss_stem = gloss.replace("STEM", wordform.otherData[0][1])  # записываем перевод
#                         glosses_array.append(gloss_stem)  # добавляем его в список глосс
#                     else:
#                         gloss_stem = gloss.replace("STEM", "/" + wordform.otherData[0][1] + "/")  # записываем перевод для остальных случаев
#                         glosses_array.append(gloss_stem)  # добавляем его в список глосс
#                 elif wordform.wfGlossed:
#                     glosses_array.append(wordform.gloss)
#                 if wordform == ana[0] and wordform.wfGlossed:
#                     morphs_array.append(wordform.wfGlossed)
#                 if wordform.wfGlossed == '':
#                     if "," in wordform.wf:
#                         wordform.wf = wordform.wf.replace(",", "")
#                         wordform.wf = wordform.wf.replace(",", "")
#                     morphs_array.append(wordform.wf)
#                     glosses_array.append(wordform.wf+"(??)")
#     conc_glosses = " ".join(morphs_array)
#     conc_morphs = " ".join(glosses_array)
#     #print(conc_glosses)
#     prepared_glosses = check_spaces(conc_glosses)
#     prepared_morphs = check_spaces(conc_morphs)
#     sentence_array.append([prepared_glosses])
#     sentence_array.append([prepared_morphs])
#     # array_to_print=" ".join(sentence_array)
#     # print(array_to_print)
#     print(prepared_glosses)
#     print(prepared_morphs)
#     last_array.append(sentence_array)


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
    print("end: ", sentence_to_print)
    return sentence_to_print

# def catch_much_stems(word):
#     analysed_gramm = []  # аналог morphs_array
#     analysed_gloss = []  # аналог glosses_array
#     third_analysis = []
#     redo = list(word.lemma.strip().split('%'))
#     print("redo ", redo)
#     redo.remove(redo[0])
#     second_analyses = a.analyze_words(redo)
#     print("Second alanysis: ", second_analyses)
#     for i in range(len(second_analyses)):
#         for wordform in second_analyses[i]:
#            # if '%' in wordform.lemma:
#            #     third_analysis = catch_much_stems(wordform)
#            #     print(third_analysis)
#             analysed_gramm.append(wordform.wfGlossed)
#             if 'STEM' in wordform.gloss:
#                 analysed_gloss.append(wordform.otherData[0][1])
#                 print(analysed_gloss)
#             print(wordform.gloss)
#             cases = list(wordform.gloss.strip().split('-'))
#             i = 1
#             while i < len(cases):
#                 analysed_gloss.append(cases[i])
#                 i = i + 1
#     split_gramm = "-".join(analysed_gramm)
#     split_gloss = "-".join(analysed_gloss)
#     print("1: ", split_gramm, "2: ", split_gloss)
#     return [split_gramm, split_gloss]
#     #if third_analysis == []:
#     #    return [split_gramm, split_gloss]
#     #else:
#     #    return [third_analysis[0], third_analysis[1]]
#
#
def catch_preverbs(sentence):
    new_sentence = []
    splitted = list(sentence.strip().split(' '))
    for word in splitted:
        new_word = []
        replaced = ""
        print("word", word)
        for i in range(len(word)):
            if word[i] == "=":
                new_sentence.append(" ")
            else:
                new_sentence.append(word[i])
        new_sentence.append(" ")
    sentence_to_print = "".join(new_sentence)
    print("sentence: ", sentence_to_print)
    #     for i in range(len(preverbs)):
    #         if preverbs[i]+"-" in word:
    #             word = word.replace(preverbs[i]+"-", preverbs[i]+" ")
    #             new_sentence.append(word)
    #             replaced = "done"
    #         elif "=" + preverbs[i] + "=" in word:
    #             word = word.replace("=" + preverbs[i] + "=", " " + preverbs[i] + " ")
    #             new_sentence.append(word)
    #             replaced = "done"
    #         elif preverbs[i] + "=" in word:
    #             print("Word:", word[0] + word[1], "Prev: ", preverbs[i][0] + preverbs[i][1], "word: ", word)
    #             word = word.replace(preverbs[i] + "=", preverbs[i] + " ")
    #             new_sentence.append(word)
    #             replaced = "done"
    #     if replaced == "":
    #         new_sentence.append(word)
    # sentence_to_print = " ".join(new_sentence)
    #print("finish", sentence_to_print)
    return sentence_to_print


def print_dict(array):
    print(array)
    filename_out = "glosses.csv"
    with open(filename_out, 'w', encoding='utf-16', newline='') as fout:
        fout.write('morphemes\tglosses\r\n')
        for elem in range(len(array)):
            fout.write(array[elem][0][0] + '\t' + array[elem][1][0] + '\r\n')


def split_sentence(sentence_array):
    print("String to split: ", sentence_array)
    for elem in sentence_array:
        # Emphasize string
        print("This string: ", elem)
        new_sentence_array = catch_preverbs(elem)
        splitted = list(new_sentence_array.strip().split(' '))
        new_string = []
        print(splitted)
        for i in range(len(splitted)):
            if "-" in splitted[i]:
                splitted[i] = splitted[i].strip().split('-')
                for j in splitted[i]:
                    new_string.append(j)
            else:
                new_string.append(splitted[i])
        print("Splitted string: ", new_string)
        array = start_analyze_2(new_string)
        last_array.append(array)
    print_dict(last_array)


def text_splitter(text):
    splitted = list(text.strip().split('.'))
    split_sentence(splitted)


text_splitter(text)
