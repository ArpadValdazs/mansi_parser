import os
import re

diacritics = ["ō", "ē", "ū", "ā", 'ī']
letters = ["o", "e", "u", "a", "i"]

chernetsov = ["ɧ", "ь", "ņ", "ꞩ", "l̩", "ś", "h", "H", "Ņ", "Ļ", "Ś", "A", "E", "I", "K", "L", "M", "N", "O", "P", "S", "T", "U", "R", "W", "V", "v", "y"]
proj_orph = ["ɣ", "ə", "n'", "ɕ", "l'", "ɕ", "x", "x", "n'", "l'", "ɕ", "a", "e", "i", "k", "l", "m", "n", "o", "p", "s", "t", "u", "r", "w", "w", "w", "u"]

def corrector(text, type):
    symbols_array = []
    new_text = ""
    text = text.replace("ьɧ", "ɧ")
    text = text.replace("\u030A", "")
    text = text.replace("\u0022", "")
    text = text.replace("=", " ")
    for i in range(len(text)):
        if type == "chern" and text[i] in chernetsov:
            for j in range(len(chernetsov)):
                if chernetsov[j] == text[i]:
                    text = text.replace(text[i], proj_orph[j])

    #         text.replace(text[i], proj_orph[i])
    # for i in range(len(chernetsov)):
    #     if type == "chern" and chernetsov[i] in text:
    #         for j in range(len(text)):
    #             text.replace(text[j], proj_orph[i])
    # for j in range(len(text)):
    #     if type == "diacritics" and text[j] in diacritics:
    #         continue
    #         # symbols_array.append(letters[i])
    #     if type == "chern" and text[j] in chernetsov:
    #         for i in range(len(chernetsov)):
    #             # if chernetsov[i] == text[j]:
    #             #     symbols_array.append(proj_orph[i])
    #             # if chernetsov[i] == text[j][0] and :
    #             #     symbols_array.append(proj_orph[i])
    # print(text)
    # new_text = "".join(symbols_array)
    return text

# def parser(text):
#     in_file = "IN.txt"
#     out_file = "OUT.txt"
#     data_file = []
#     os.chdir("texts")
#     # Открыли, прочитали, получили список
#     with open(in_file, 'r') as read_file:
#         for line in read_file:
#             data_file.append(line.strip('\n'))
def init_function():
    text = corrector('Kosja sunt erьɧ otьr. Kosja sunt otьr oli. Pakv posi vojkan otьr akv tujьɧ ekvate san vars. ekvate san vars, loŋha vorati. ekvate lavi Tur tep, its tep ponne san ojkate at taŋhi. ojkatan san almajaves, puliɧ ratwes. am taj tur tep astep jorьl at janьɧ masum. vor sorup n̩ovьl tajim, luvum janьɧmas n̩ovьlum janьɧmas. ojkate lavs. kitit tujaɧ jemtьs. ekvate hotal̩ olne san, hansaŋ san akvaьɧ ta vari. ojkate nupьl lavi: - naŋen tur tep asten pinuŋkve, manьr jomas sankve. ojkaten almajave, os puliɧ ratves. ojkate lavs - am tur tep as tep tajum luvum at janьɧmas, n̩ovьlum at janь̄ɧmas. uj n̩ovьl tajim luvum janьɧmas, n̩ovьlum janьɧmas. Hurmit tujьɧ ti johtьs, jaŋk notne poraьɧ ti jemtьs os. ekvate hansaŋ san os ta vari. Ja vars os sant. Ojkate nupьl lavi naŋьh nake tur tep, as tep pinne manьr saŋkve! ojkate vasьɧ nemat hotum vasьɧ at suitьɧlas. ekvate nupьl lavi naŋ kasьn minimen ke minumen, ti astlahtasit. ajaŋ hum pьɧane saran hap varuŋkve larsane vap varsьt. Talthatuŋkve patsьt. taltateɧt, nē paɧ mini. n̩al̩ akv hum hontaste. Tamle hum honthatas samaɧe nit at laplьɧ ta hurip hum aman etpos, aman hotal! Tan ojkate apsite. Tan ekva oŋɧa nupьl lavi: - ta hapet ojkan hottal P.P.V.o hottal̩ minne man totilen. Minne mān ojkan ke alave, vasьɧ ti man at sunsiln. an̩ ta minasьt. ete hotal etьl ta mineɧt. ꞩaraꞩ kotli akv mat mina hosa minasit man vat̩a minasit ekvate=ojkate nupьl lavi: huver (hujev) hujunkve patsit, ojkate lavi, na mahmane nupьl lavi: nan hujen, am urejum. ekvate lavi: naŋ hujen, naŋ ropitase ь n; vaɧtal patsen, am nas unlasum! ojkate lavi: - naŋ erьŋ jola ojilmataven erьŋ honten johtavev. ekvate lavi: - naŋ hujen, hontmake jiŋkve patave noh=sajkatijanum. Hujuŋkve patsьt, ojkate ker supe hot ekvate lavi: ker supe hot aŋh w eln, ete-hotal ker ulaman jomas oꞩsann, an̩ aŋhweln! ojkate ker ulamane aŋɧsane, ta hujas. tan hujasьt, mahmane tan hujnel sis ekvaten ker kus sunte lap ta juntuvs noh= ul vos mashati. Jovte kasajil supьɧ. ꞩorhьltaves, noh=hartuŋkve jovt nirasanete mus noh-hartnete mus sopьŋ vos tolmati. mahmane hujnanel sis ekva ruꞩ oter. usen ta minas. Ruꞩ oter us lunnuv ols. Juv=johtas RO usen, lavi - man johtesuv, jajen hontьɧ! takvi mahmane palt sarten minas. tan juji palet. RO hont hap juv. tan mahmane palt johtьs mahmane hujeɧt. RO. hap tan paltlaneln jis paɧ-pohats. ekvate ojkate nupьl lavi noŋh=kvalen, hontn johtuvesuv ti alavev. ojkate noh=kvalapas, rohtьp= tahtas. noh-kvalapas, ker kuse noh kos masapite, tuv at lapi, kente ekvaten lap juntime. Hot ta liste. Jovte almajaste, hassumtaste. Hassumtame mus, ꞩorhьltim matenьl ta supьŋ ta tolmats. Jovte sakvalas, tuvl r otern pusen ta alvest. ekva tup hul̩tas os apat hujne pьriꞩ hultьs. ekvate r.o. nupьl lavi - Pьriꞩ os oleln, janьɧmi, tan aꞩe l̩oŋh jujil kinsite. RO lavi "Tau man̩, aꞩe l̩oŋh at kínsīte, aꞩe on̩ꞩes man ati at vaɧte. ta minasit. ppvo puŋk sovl r.otern hot nujves, naŋk ta l̩ahna ta noh- taɧataves. Jajt ta ta l̩ahьl jalum ppvo puŋ save naŋk tal̩ahьt vot untave sira sove vos votave, aŋha sove vos votave! ne RO palt olmьɧtas. Humьɧ ta variste. An̩ ta oleьɧ. Pьɧriꞩ hoꞩa man vat̩i ols janьɧmas. RO pьɧetьl, n̩avrametьl joŋheɧt. Tau katl jor, laɧьle jor, RO pьɧьt lavi vat vaɧtalьꞩ mini, tau lьɧ itьŋьꞩ mini. R.O. n̩avramьt pьriꞩ nupьl laveɧt - Naŋ jor laɧьlьn ti āꞩmen, jor kat t̩i aꞩmen, aꞩen puŋk sove as kotle tumpet naŋk tal̩aht manrьɧ honi? jor ti olmen. ꞩane palt johtьs ꞩane nupьl lavi: - Toha ti laveɧt - Jor ti osen, os aꞩen olim porat joren hotal̩ totiɧlasen? Ꞩane lavi: - Aꞩen ti, R.O. Ta nomsi aꞩe sol̩ ti mot hotal jemti akv ti piꞩ, tan jor. Joŋhuŋkve pateɧt tau lьɧ, itьŋьꞩ mini, motant lьɧt vaɧtalaꞩ mini. RO n̩avramьt laveɧt. - Aꞩen olim porat jor ti olmьn, joren hotal̩ totiɧlasen! Ꞩane palt os ti minas. Ꞩane palt johtьs lavi - Jor ti olmen, aꞩen olim porat joren hotal̩ toti̊ɧlasen? Ꞩane lavi aꞩen ti. Hurmit peraman̩ ti jemtьs. Ta jonɧeɧt. Tau lьɧaьŋьꞩ mini motantlьɧt, vaɧtalьꞩ mini. N̩avramьt lavьɧt- Naŋ jor ti olmen, aꞩen olim porat, joren hotal̩ ti totiɧlaslьn? Us joli palt ekvaьɧ-ojkaьɧ oleьɧ. Pьriꞩ nomsi ekvaьɧ ojkaьɧ palt tuv jalejum. Navramьt laveɧt, ertum aꞩ oꞩsum - aꞩum alime, ꞩanum lavi: "aꞩum oli!". P. ekvaьɧ ojkaьɧ kitьɧlaŋkve minas. e.o palt johtьs kitьɧli: Sol̩ aman aꞩ oꞩsum? E.-O. laveьɧ, - sol̩ aꞩ oꞩsьn. Aꞩen ti R.Oterna olves. P. ten nupьlen lavi - Anumen hap majeln, am juvle mineɧum, aman rot oꞩsum, man ati, am at vaɧlum. E.-O. laveьɧ "rotan jun oleɧt." Man̩ nupьl majves, ta minas. Minimete elal̩ sunsi, Tajtnьl Tajt hosit hap juv. Hap l̩apan johtuŋkve pats, paɧ pohtas, vorn tujthatas. Hap tau torɧьl johtьs, akv hum suiti: - Paɧ pohtev, tit elmholas paɧ miname naŋki. kinsi luv. Tan poɧ-pohtasьt. Ta kinsuŋkve patsanel. Kissanel, hontsanel. PPVO. ta apꞩite. jaɧpьɧe kinsiŋkve ti johtьs P. jaɧpьɧen, kitьɧlave: - Aꞩen hotal̩ totves? P. lavi: - Aꞩum ruꞩ oterna olime. Ta RO usen minasit. RO usen johtesьt. paɧ pohtasit Paɧ=minuŋkve patsьt P.P.V.O.U., jovt n̩al̩ vьŋkve kyꞩi. Mire nupьl lavi - Maj manьr mirьl varev, ti kem use, amkem paɧ= mineɧum. Am jovtьl n̩olьl manьr vareɧum, ti kem us. N̩an̩ tup unten mant sup vaɧlum, (N̩an̩ untne mant sup) Tup viste, paɧ-ta minas Paɧ minas, us akv pale tupьl viten ta rautaste (mant supetьl) uset olne mir ꞩar pusen olaste viten naluv rautasaste. R.O. (mant tupьl supetьl) jūnьtaste, samaɧe noren hanujasьɧ, akv toh sunseьɧ. Ta hum-akv kot pale, akv laɧьl pale tarvitьŋ. Ekvaьɧ-ojkaьɧ, ten tuvpohtamьɧ - Mena men ul aleln! Tau lavi: - Am nenan at alijaɧum. Juvle minuŋkve ti patsьt. On̩ɧa liliŋ taɧьl hapen totaste. Hapen totaste, liliŋ taɧьl kataɧe hap pattan ker sol̩il jol=ratsaɧe. Laɧьlaɧe hap pattan ker sol̩il as jol ratsaɧe. Ta minmьɧtasьt. Ta minmьɧtasit ekva hap pattat ta huji. Ta pukite hosit ta jomeɧt Jomimenьl sorumen ta patves. Tuvl viten ta li̊sanel. Tan olne māneln ta jóhtāsьt. An̩ ta oleɧt', "chern")
    # print(text)
    return text

#text = init_function()
#print(text)

