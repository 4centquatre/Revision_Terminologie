import streamlit as st
from random import randint

dico = {
    0: ["A-, AN-", "Absence de", "Anorexie / Aphonie", "Absence d'appétit / Perte importante de la voix"],
    1: ["Anti-", "Contre (s'oppose à)", "Antalgique", "Molécule qui lutte contre la douleur"],
    2: ["Brady-", "Lent", "Bradypnée", "Respiration lente"],
    3: ["Dys-", "Difficulté", "Dyslexie", "Difficulté à lire, à reconnaître le langage écrit"],
    4: ["Endo-", "À l'intérieur", "Endomètre", "Paroi interne de l'utérus"],
    5: ["Intra-", "À l'intérieur", "Intraveineuse", "À l'intérieur d'une veine"],
    6: ["Eu-", "Normal", "Eupépsie", "Digestion normale"],
    7: ["Exo-", "À l'extérieur", "Exocrine", "Qui est sécrété hors d'une cavité du corps"],
    8: ["Extra-", "À l'extérieur", "Extracellulaire", "Situé à l'extérieur d'une cellule"],
    9: ["Hémi-", "Moitié", "Hémiplégie", "Paralysie de la moitié gauche ou droite du corps"],
    10: ["Hyper-", "Excès", "Hyperglycémie", "Taux de glucose dans le sang supérieur aux valeurs normales"],
    11: ["Hypo-", "Diminution, manque", "Hypoxie", "Diminution de la quantité d'oxygène apportée aux tissus"],
    12: ["Macro-", "Grand", "Macroscopique", "Que l'on peut observer à l'œil nu"],
    13: ["Micro-", "Petit", "Micro-organisme", "Organisme vivant invisible à l'œil nu"],
    14: ["Néo-", "Nouveau", "Néothérapie", "Nouveau traitement"],
    15: ["Oligo-", "Peu", "Oligurie", "Production anormalement faible d'urine"],
    16: ["Poly-", "Beaucoup, plusieurs", "Polydipsie", "Soif excessive"],
    17: ["Tachy-", "Rapide", "Tachycardie", "Accélération du rythme cardiaque"],

    18: ["-algie", "Douleur", "Dorsalgie", "Douleur au niveau du dos"],
    19: ["-centèse", "Ponction", "Amniocentèse", "Ponction et prélèvement de liquide amniotique"],
    20: ["-cide", "Qui tue", "Bactéricide", "Qui tue des bactéries"],
    21: ["-cyte", "Cellule", "Myocyte", "Cellule musculaire"],
    22: ["-ectasie", "Dilatation", "Bronchectasie", "Dilatation des bronches"],
    23: ["-ectomie", "Ablation", "Appendicectomie", "Ablation de l'appendice"],
    24: ["-émie", "Sang", "Glycémie", "Taux de glucose dans le sang"],
    25: ["-gène", "Qui entraîne / provoque", "Pathogène", "Qui provoque une maladie"],
    26: ["-genèse", "Formation", "Spermatogenèse", "Processus de formation des spermatozoïdes"],
    27: ["-gramme", "Résultat écrit", "ECG", "Tracé représentant l'activité électrique du cœur"],
    28: ["-graphie", "Enregistrement", "Radiographie", "Enregistrement par rayons X"],
    29: ["-ite", "Inflammation", "Arthrite", "Inflammation d'une articulation"],
    30: ["-logie", "Étude de", "Cardiologie", "Étude de l'appareil cardiovasculaire"],
    31: ["-logue", "Spécialiste de", "Pneumologue", "Spécialiste des poumons"],
    32: ["-lyse", "Destruction", "Hydrolyse", "Destruction par l'eau"],
    33: ["-mégalie", "Très grand", "Hépatomégalie", "Augmentation de la taille du foie"],
    34: ["-ome", "Tumeur", "Ostéome", "Tumeur osseuse"],
    35: ["-ose", "Pathologie non inflammatoire", "Arthrose", "Destruction irréversible du cartilage articulaire"],
    36: ["-pathie", "Maladie", "Myopathie", "Maladie touchant les muscles"],
    37: ["-pénie", "Diminution", "Leucopénie", "Diminution du nombre de globules blancs"],
    38: ["-plastie", "Réparer, corriger", "Otospastie", "Correction chirurgicale du pavillon de l'oreille"],
    39: ["-plégie", "Paralysie", "Tétraplégie", "Paralysie des quatre membres"],
    40: ["-rragie", "Écoulement de sang", "Hémorragie", "Écoulement de sang hors d'un vaisseau"],
    41: ["-rrhée", "Écoulement non sanguin", "Rhinorrhée", "Écoulement de liquide par le nez"],
    42: ["-scopie", "Examen visuel", "Laryngoscopie", "Examen visuel du larynx"],
    43: ["-thérapie", "Traitement", "Radiothérapie", "Traitement utilisant des rayons"],
    44: ["-tomie", "Incision", "Cardiotomie", "Incision chirurgicale du cœur"],
    45: ["-urie", "Urine", "Hématurie", "Présence de sang dans les urines"],

    46: ["cyt(o)-", "Cellule"],
    47: ["hist(o)-", "Tissu"],

    48: ["arthr(o)-", "Articulation"],
    49: ["cérébr(o)-", "Cerveau"],
    50: ["cervic(o)-", "Cou / col"],
    51: ["chondr(o)-", "Cartilage"],
    52: ["cost(o)-", "Côte"],
    53: ["cox(o)-", "Hanche"],
    54: ["gon(o)-", "Genou"],
    55: ["médull(o)- / myél(o)-", "Moelle"],
    56: ["my(o)-", "Muscle"],
    57: ["neur(o)- / névr(o)-", "Nerf"],
    58: ["osté(o)-", "Os"],
    59: ["rachi- / rachid(o)-", "Rachis (colonne vertébrale)"],
    60: ["tendin(o)-", "Tendon"],
    61: ["thorac(o)-", "Thorax"],

    62: ["adip(o)-", "Graisse"],
    63: ["appendic(o)-", "Appendice"],
    64: ["bucc(o)- / stomat(o)-", "Bouche"],
    65: ["chol(e)-", "Bile"],
    66: ["cholécyst(o)-", "Vésicule biliaire"],
    67: ["col(o)-", "Côlon"],
    68: ["duodén(o)-", "Duodénum"],
    69: ["entér(o)-", "Intestin"],
    70: ["gastr(o)-", "Estomac"],
    71: ["hépat(o)-", "Foie"],
    72: ["jéjun(o)-", "Jéjunum"],

    73: ["ilé(o)-", "Iléon"],
    74: ["odont(o)-", "Dent"],
    75: ["œsophag(o)-", "Œsophage"],
    76: ["pharyng(o)-", "Pharynx"],
    77: ["rect(o)-", "Rectum"],

    78: ["angi(o)- / vas(o)- / vascul(o)-", "Vaisseau"],
    79: ["artéri(o)-", "Artère"],
    80: ["athér(o)-", "Dépôt de graisse"],
    81: ["bar(o)-", "Pression"],
    82: ["cardi(o)-", "Cœur"],
    83: ["coronar(o)-", "Coronaire"],
    84: ["hém(o)-", "Sang"],
    85: ["ox(o)-", "Oxygène"],
    86: ["nécr(o)-", "Mort"],
    87: ["phléb(o)-", "Veine"],
    88: ["thromb(o)-", "Caillot"],
    89: ["valvul(o)-", "Valvule"],

    90: ["bronch(o)-", "Bronche"],
    91: ["laryng(o)-", "Larynx"],
    92: ["nas(o)- / rhin(o)-", "Nez"],
    93: ["-pnée / spir(o)-", "Respiration"],
    94: ["pneum(o)- / pulm(o)-", "Poumon"],
    95: ["traché(o)-", "Trachée"],

    96: ["glyc(o)-", "Glucose"],
    97: ["glycogén(o)-", "Glycogène"],
    98: ["insulin(o)-", "Insuline"],
    99: ["néphr(o)-", "Rein"],
    100: ["ur(o)-", "Urine"],
    101: ["étranger", "Étranger"],

    102: ["leuc(o)-", "Blanc"],
    103: ["lymph(o)-", "Lymphe"],
    104: ["phag(o)-", "Manger"],
    105: ["pyr(o)-", "Feu (fièvre)"],
    106: ["sér(o)-", "Sérum"],
    107: ["splén(o)-", "Rate"],
    108: ["thym(o)-", "Thymus"],
    
    110: ["andr(o)-", "Homme"],
    111: ["cervic(o)-", "Cou - col"],
    112: ["gynéc(o)-", "Femme"],
    113: ["hystér(o)-", "Utérus"],
    114: ["mamm(o)-", "Sein"],
    115: ["mén(o)-", "Mois, règles"],
    116: ["métr(o)-", "Utérus"],
    117: ["orchid(o)-", "Testicules"],
    118: ["ovari(o)-", "Ovaire"],
    119: ["prostat(o)-", "Prostate"],
    120: ["salping(o)-", "Trompe"],

    121: ["sperm(o)-", "Sperme - semence"],
    122: ["sthén(o)-", "Force, énergie"],
    123: ["térat(o)-", "Malformation - monstre"],
    124: ["vagin(o)-", "Vagin"],

    125: ["cancer(o)-", "Cancer"],
    126: ["carcin(o)-", "Cancer"],
    127: ["cary(o)-", "Noyau"],
    128: ["chimi(o)-", "Chimie"],
    129: ["iatr(o)-", "Troubles (provoqués par un traitement)"],
    130: ["nuclé(o)-", "Noyau"],
    131: ["radi(o)-", "Rayon"],
    132: ["tumor(o)-", "Tumeur"],
    109: ["-trophie", "Développement"],
}

if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = {}
if "current" not in st.session_state:
    st.session_state.current = None
if "step" not in st.session_state:
    st.session_state.step = "question"
if "end" not in st.session_state:
    st.session_state.end = {}

st.title("Quiz Terminologie")

if st.session_state.step == "question":
    st.session_state.reponse = ""
    if len(st.session_state.questions.keys()) >= len(dico.keys()):
        st.session_state.step = "fin"
        #st.rerun()
    indice = randint(0, len(dico) - 1)
    while indice in st.session_state.questions.keys():
        indice = randint(0, len(dico) - 1)
    st.session_state.current = indice
    st.session_state.step = "reponse"
    #st.rerun()

if st.session_state.step == "reponse":
    indice = st.session_state.current
    indice2 = randint(0,len(dico[indice])-1)
    question = dico[indice][indice2]
    st.session_state.questions[indice] = question
    st.write("Question : "+question)
    reponse = st.text_input("Écris ta réponse (ou 'stop' pour arrêter)", key="reponse_input")

    if st.button("Valider"):
        if reponse.lower() == "stop":
            st.session_state.step = "fin"
        else:
            st.session_state.step = "feedback"
            st.session_state.reponse = reponse
        #st.rerun()

if st.session_state.step == "feedback":
    indice = st.session_state.current
    chaine = ""
    for car in dico[indice]:
        chaine += car + " "
    st.write("La réponse était : "+chaine)
    vrai_faux = st.radio("Tu as eu :", ["Vrai", "Faux"], horizontal=True)

    if st.button("Continuer"):
        if vrai_faux == "Vrai":
            st.session_state.score += 1
        elif vrai_faux == "Faux":
            st.session_state.end[indice] = dico[indice]
        st.session_state.step = "question"
        #st.rerun()

# Étape finale
if st.session_state.step == "fin":
    st.write("C'est fini ! Ton score est de : "+str(st.session_state.score)+"/"+str(len(st.session_state.questions.keys())-1)+ " Bravo mon coeur t'es trop forte !")
    if len(st.session_state.end.keys())>1:
        st.write("Tes reponses fausses etaient : ")
    elif len(st.session_state.end.keys()) == 1:
        st.write("Ta reponse fausse etait : ")
    else:
        st.write("Tu n'as eu aucune reponse fausse bravo !")
    for tab in st.session_state.end.values():
        chaine = ""
        for item in tab:
            chaine = chaine + str(item) + " "
        st.write(chaine)
    if st.button("refaire"):
        st.rerun()
