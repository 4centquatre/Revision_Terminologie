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
    101: ["xén(o)", "Étranger"],

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

    133: ["Absorption", "Processus permettant le passage des nutriments de la lumière intestinale vers le sang ou la lymphe"],
    134: ["Accident vasculaire cérébral", "Toute ischémie ou hémorragie au niveau d'un vaisseau cérébral"],
    135: ["Acidose", "Augmentation du pH sanguin"],
    136: ["Allergie", "Réaction exagérée du système immunitaire à une substance étrangère"],
    137: ["Anatomie", "Science qui étudie la forme et les relations entre les organes"],
    138: ["Anémie", "Diminution de la concentration sanguine d'hémoglobine"],
    139: ["Anévrisme", "Dilatation de la paroi d'une artère"],
    140: ["Angiographie", "Examen radiographique des vaisseaux sanguins à l'aide d'un produit de contraste"],
    141: ["Angioplastie", "Intervention chirurgicale visant à réparer ou dilater un vaisseau sanguin"],
    142: ["Anoxémie", "Absence d'oxygène dans le sang"],
    143: ["Anoxie", "Absence d'oxygène au niveau d'un tissu ou d'un organe"],
    144: ["Anorexie", "Perte de l'appétit"],
    145: ["Apnée", "Arrêt temporaire de la respiration"],
    146: ["Appareil", "Ensemble d'organes assurant une fonction commune"],
    147: ["Artérite", "Inflammation des artères"],
    148: ["Articulation", "Point de jonction entre deux os"],
    149: ["Arythmie", "Trouble du rythme cardiaque"],
    150: ["Asthénie", "Affaiblissement de l'état général"],
    151: ["Athérome", "Dépôt lipidique dans la paroi des artères"],
    152: ["Athérosclérose", "Durcissement de la paroi des artères associé à un dépôt lipidique"],
    153: ["Atrophie", "Diminution du volume d'un tissu ou d'un organe"],
    154: ["Automatisme cardiaque", "Capacité du cœur à se contracter sans innervation nerveuse"],
    155: ["Axone", "Prolongement unique du neurone transmettant l'influx nerveux"],

    156: ["Biomolécule", "Molécule présente chez les êtres vivants"],
    157: ["Biopsie", "Prélèvement d'un fragment de tissu pour analyse"],
    158: ["Bradycardie", "Ralentissement du rythme cardiaque"],
    159: ["Bronchiolite", "Inflammation des bronchioles"],
    160: ["Bronchite", "Inflammation des bronches"],
    161: ["Bronchorrhée", "Augmentation de l'écoulement du mucus bronchique"],

    162: ["Cachexie", "Amaigrissement extrême et affaiblissement général"],
    163: ["Cardiomyopathie", "Affection du muscle cardiaque"],
    164: ["Carence", "Manque d'un ou plusieurs nutriments essentiels"],
    165: ["Cellule", "Unité structurale et fonctionnelle de l'organisme"],
    166: ["Céphalée", "Douleur localisée au niveau de la tête"],
    167: ["Cerveau", "Organe du système nerveux central"],
    168: ["Cyanose", "Coloration bleutée de la peau"],

    169: ["Déglutition", "Action d'avaler"],
    170: ["Déshydratation", "Diminution de la quantité d'eau dans l'organisme"],    
    171: ["Diarrhée", "Émission de selles liquides"],
    172: ["Diastole", "Phase de relâchement du cœur"],
    173: ["Digestion", "Transformation des aliments en nutriments"],
    174: ["Dyspnée", "Difficulté respiratoire"],

    175: ["ECG", "Enregistrement de l'activité électrique du cœur"],
    176: ["Embolie", "Obstruction brutale d'un vaisseau par un caillot"],
    177: ["Encéphale", "Partie du système nerveux contenue dans le crâne"],
    178: ["Enzyme", "Protéine accélérant une réaction chimique"],
    179: ["Épithélium", "Tissu constitué de cellules jointives"],
    180: ["Expectoration", "Rejet de sécrétions par les voies respiratoires"],

    181: ["Fibrose", "Formation excessive de tissu fibreux"],
    182: ["Fréquence cardiaque", "Nombre de battements du cœur par minute"],

    183: ["Glycémie", "Concentration de glucose dans le sang"],
    184: ["Glande", "Organe produisant une substance"],
    185: ["Glucose", "Sucre simple utilisé comme source d'énergie"],

    186: ["Hématose", "Échanges gazeux entre l'air et le sang"],
    187: ["Hémorragie", "Écoulement de sang hors des vaisseaux"],
    188: ["Hypertension", "Augmentation de la pression artérielle"],
    189: ["Hypoxie", "Diminution de l'apport en oxygène aux tissus"],

    190: ["Inflammation", "Réaction de défense de l'organisme"],
    191: ["Insuline", "Hormone hypoglycémiante produite par le pancréas"],
    192: ["Ischémie", "Diminution de l'apport sanguin à un tissu"],

    193: ["Lipide", "Molécule organique hydrophobe"],
    194: ["Lymphe", "Liquide circulant dans les vaisseaux lymphatiques"],

    195: ["Métabolisme", "Ensemble des réactions chimiques de l'organisme"],
    196: ["Mitochondrie", "Organite produisant l'énergie cellulaire"],

    197: ["Nécrose", "Mort d'un tissu"],
    198: ["Neurone", "Cellule nerveuse spécialisée"],

    199: ["Œdème", "Accumulation de liquide dans un tissu"],
    200: ["Organe", "Ensemble de tissus assurant une fonction"],

    201: ["Pathologie", "Étude des maladies"],
    202: ["Phagocytose", "Destruction d'éléments étrangers par une cellule"],
    203: ["Pouls", "Perception des battements artériels"],

    204: ["Respiration", "Ensemble des échanges gazeux"],
    205: ["Rythme cardiaque", "Succession des contractions du cœur"],

    206: ["Système", "Ensemble d'organes ayant une fonction commune"],
    207: ["Systole", "Phase de contraction du cœur"],

    208: ["Thrombose", "Formation d'un caillot dans un vaisseau"],
    209: ["Tissu", "Ensemble de cellules spécialisées"],

    210: ["Ultrastructure", "Organisation fine des éléments cellulaires"],
    211: ["Vaisseau", "Conduit transportant le sang ou la lymphe"],
    212: ["Ventilation", "Renouvellement de l'air dans les poumons"]
}

if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = {}
if "dico_reponses" not in st.session_state:
    st.session_state.dico_reponses = {}
if "current" not in st.session_state:
    st.session_state.current = None
if "step" not in st.session_state:
    st.session_state.step = "question"
if "end" not in st.session_state:
    st.session_state.end = {}
if "dico" not in st.session_state:
    st.session_state.dico = dico.copy()
if "indice" not in st.session_state:
    st.session_state.current = None
if "indice2" not in st.session_state:
    st.session_state.current = None

st.title("Quiz Terminologie")

if st.session_state.step == "question":
    st.session_state.reponse = ""
    if len(st.session_state.questions.keys()) >= len(st.session_state.dico.keys()):
        st.session_state.step = "fin"
        st.rerun()
    tab_indices = []
    for cle in st.session_state.dico.keys():
        tab_indices.append(cle)
    i = randint(0, len(tab_indices) - 1)
    while tab_indices[i] in st.session_state.end.keys():
        i = randint(0, len(tab_indices) - 1)
    indice = tab_indices[i]
    st.session_state.indice = indice
    st.session_state.step = "reponse"
    st.rerun()

if st.session_state.step == "reponse":
    indice2 = randint(0,len(st.session_state.dico[st.session_state.indice])-1)
    st.session_state.indice2 = indice2
    question = st.session_state.dico[st.session_state.indice][st.session_state.indice2]
    st.session_state.questions[st.session_state.indice] = question
    st.write("Question : "+question)
    with st.form("form_reponse"):
        reponse = st.text_input("Écris ta réponse", key="reponse_input")
        validee = st.form_submit_button("Valider")

    if st.button("Stop"):
        st.session_state.step = "fin"

    elif validee:
        st.session_state.step = "feedback"
        st.session_state.reponse = reponse
        st.session_state.dico_reponses[indice] = reponse
        st.rerun()

if st.session_state.step == "feedback":
    chaine = ""
    for car in st.session_state.dico[st.session_state.indice]:
        chaine += car + " "
    st.write("La réponse était : "+chaine)
    st.write("Ta réponse était : "+st.session_state.reponse)
    vrai_faux = st.radio("Tu as eu :", ["Vrai", "Faux"], horizontal=True)

    if st.button("Continuer"):
        if vrai_faux == "Vrai":
            st.session_state.score += 1
        elif vrai_faux == "Faux":
            st.session_state.end[st.session_state.indice] = st.session_state.dico[st.session_state.indice]
        st.session_state.step = "question"
        st.rerun()

if st.session_state.step == "fin":
    st.write("C'est fini ! Ton score est de : "+str(st.session_state.score)+"/"+str(len(st.session_state.dico_reponses.keys()))+ " Bravo mon coeur t'es trop forte !")
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
    if st.button("Refaire"):
        st.session_state.score = 0
        st.session_state.questions = {}
        st.session_state.end = {}
        st.session_state.current = None
        st.session_state.step = "question"
        st.session_state.dico = dico.copy()
        st.session_state.indice = None
        st.session_state.indice2 = None
        st.session_state.reponse = ""
        st.session_state.dico_reponses = {}
        st.rerun()
    elif st.button("Refaire avec tes erreurs"):
        if len(st.session_state.end) > 0:
            st.session_state.questions = {}
            st.session_state.score = 0
            st.session_state.current = None
            st.session_state.step = "question"
            st.session_state.dico = st.session_state.end.copy()
            st.session_state.end = {}
            st.session_state.indice = None
            st.session_state.indice2 = None
            st.session_state.reponse = ""
            st.session_state.dico_reponses = {}
            st.rerun()
        else:
            st.warning("Tu n'as aucune erreur à refaire.")


